import os
import sys
import json
import time
import logging
import requests
import subprocess

# Default configuration values
DEFAULT_CONF = {
    "freq": 60,
    "gist_id": "your-gist-id-here",
    "token": "your-github-token-here",
    "interface": "eth0"
}

# Paths
conf_file = os.path.expanduser("/etc/.wirefox.conf")
log_file = os.path.expanduser("/var/.wirefox.log")
service_file = "/etc/systemd/system/wirefox.service"

# Ensure configuration file exists and is valid
if not os.path.exists(conf_file) or os.stat(conf_file).st_size == 0:
    with open(conf_file, 'w') as f:
        json.dump(DEFAULT_CONF, f, indent=4)
    print(f"Default configuration created at {conf_file}")
    config = DEFAULT_CONF
else:
    try:
        with open(conf_file, 'r') as f:
            config = json.load(f)
    except json.JSONDecodeError:
        print(f"Malformed configuration file at {conf_file}. Resetting to defaults.")
        with open(conf_file, 'w') as f:
            json.dump(DEFAULT_CONF, f, indent=4)
        config = DEFAULT_CONF

# Ensure the log file exists
log_dir = os.path.dirname(log_file)
if not os.path.exists(log_dir):
    os.makedirs(log_dir, exist_ok=True)

if not os.path.exists(log_file):
    with open(log_file, 'w') as f:
        f.write("")

# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)

logging.info("Wirefox script started.")

def install_service():
    """Install the script as a systemd service."""
    service_contents = f"""[Unit]
Description=Wirefox IP Updater
After=network.target

[Service]
ExecStart=/usr/bin/python3 {os.path.abspath(__file__)}
Restart=always
User={os.getenv('USER')}
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
"""
    try:
        with open(service_file, 'w') as f:
            f.write(service_contents)

        subprocess.run(["systemctl", "daemon-reload"], check=True)
        subprocess.run(["systemctl", "enable", "wirefox"], check=True)
        subprocess.run(["systemctl", "start", "wirefox"], check=True)
        print("Wirefox service installed and started successfully.")
    except Exception as e:
        print(f"Failed to install the service: {e}")

def get_ips(interface):
    """Get the local and public IP addresses."""
    try:
        local_ip = os.popen(f"ip -4 addr show {interface} | grep inet | awk '{{print $2}}' | cut -d'/' -f1").read().strip()
        logging.info(f"Local IP for {interface}: {local_ip}")
        public_ip = requests.get("https://api.ipify.org").text.strip()
        logging.info(f"Public IP: {public_ip}")
        return local_ip, public_ip
    except Exception as e:
        logging.error(f"Failed to get IP addresses: {e}")
        return None, None

def update_gist(gist_id, token, local_ip, public_ip):
    """Update the GitHub Gist with the current IPs."""
    gist_url = f"https://api.github.com/gists/{gist_id}"

    try:
        headers = {"Authorization": f"token {token}"}
        response = requests.get(gist_url, headers=headers)
        response.raise_for_status()
        gist_data = response.json()

        file_content = next(iter(gist_data["files"].values()))["content"]

        last_line = file_content.strip().split("\n")[-1]
        if local_ip in last_line and public_ip in last_line:
            logging.info("IPs unchanged, skipping update.")
            return

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        new_content = file_content + f"\n[{timestamp}] Local: {local_ip}, Public: {public_ip}"

        payload = {
            "files": {
                list(gist_data["files"].keys())[0]: {"content": new_content}
            }
        }
        update_response = requests.patch(gist_url, headers=headers, json=payload)
        update_response.raise_for_status()

        logging.info("Gist updated successfully.")
    except Exception as e:
        logging.error(f"Failed to update gist: {e}")

def main():
    freq = config.get("freq", 60)
    gist_id = config["gist_id"]
    token = config["token"]
    interface = config.get("interface", "eth0")

    while True:
        local_ip, public_ip = get_ips(interface)
        if local_ip and public_ip:
            update_gist(gist_id, token, local_ip, public_ip)
        else:
            logging.error("Could not retrieve IP addresses, skipping update.")

        time.sleep(freq)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--install-service":
        install_service()
    else:
        main()

