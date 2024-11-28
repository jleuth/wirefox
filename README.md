# Wirefox

**Wirefox** is a compact, headless device based on the Luckfox Pico Plus/Pro/Max, designed for SecOps professionals and pentesters. It simplifies setting up a proxy by automatically configuring itself when connected to power and Ethernet.  

**Wirefox Services** is the backbone of this system, enabling users to retrieve the device's local and public IPs effortlessly without network scanning. This makes managing headless devices seamless and efficient.

---

## Features

- **Automatic IP Discovery**: Detects and uploads local and public IPv4 addresses to a GitHub Gist.
- **Duplicate Prevention**: Ensures only new IP addresses are uploaded.
- **Timestamps**: Includes a log of when each IP was recorded.
- **Configurable**: Easily customize behavior with a `.wirefox.conf` file.
- **System Service**: Runs at boot for plug-and-play usability.

---

## Setting Up Wirefox Services

### Prerequisites

- Python 3.8+ installed on your Wirefox device.
- A GitHub account with a personal access token that includes Gist permissions.
- A pre-created GitHub Gist to store IP logs.

### Setting up the Gist and PAT
1. **Make the Gist**:
   Visit https://gists.github.com and create a new gist. The file *MUST* be named "wirefox_ips.txt*. For your security, make sure the gist is a Secret Gist and don't share the link with ANYONE.

2. **Make your PAT**:
   Go to https://github.com/settings/tokens?type=beta, make sure you're creating a Fine-Grained token. Click ```Generate New Token```, and input your MFA code if needed.
   Don't grant access to repositories. We need to grant access to an account setting, so scroll down to ```Account Permissions```, find ```Gists``` and change the access setting to ```Read and Write```
   Copy your token, and paste it in a safe place. You can only view it once, and we will need it in a minute.

### Installing Wirefox Service

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<username>/wirefox.git
   cd wirefox
   ```

4. **Edit Configuration**:
   Open the configuration file and update it with your Gist ID, GitHub token, and other settings:
   ```plaintext
   {
       "gist_id": "YOUR_GIST_ID",
       "github_token": "YOUR_GITHUB_PERSONAL_ACCESS_TOKEN",
       "check_frequency": 60,
       "network_interface": "eth0"
   }
   ```

5. **Register Wirefox as a Service**:
   Install and enable Wirefox to run at boot:
   ```bash
   sudo wirefox --install-service
   sudo systemctl start wirefox
   sudo systemctl enable wirefox
   ```

---

## Configuration File Options

The Wirefox tool reads from `~/.wirefox.conf` (or `/etc/wirefox.conf` for system-wide setups).  

### Available Options:
- **`gist_id`**: The ID of the GitHub Gist where IP addresses will be uploaded.
- **`github_token`**: A personal access token with permissions to write to the Gist.
- **`check_frequency`**: Frequency (in seconds) for IP checks and uploads. Default is `60`.
- **`network_interface`**: The network interface to monitor (e.g., `eth0`, `wlan0`).

---

## Usage

### Running Manually
To test the Wirefox Python tool:
```bash
wirefox
```

### Viewing Logs
If running as a service, check logs to diagnose issues:
```bash
journalctl -u wirefox.service
```

---

## Troubleshooting

- **Service Not Starting**:  
  Verify the configuration file exists and is correctly formatted as valid JSON.
  ```bash
  cat ~/.wirefox.conf
  ```
  
- **IPs Not Uploading**:  
  Ensure the Gist ID and GitHub token are correct. Confirm the token has appropriate permissions.

- **IP Not Changing**:  
  Wirefox skips uploads if the IP addresses remain the same as the last recorded entry.

- **Permission Errors**:  
  Check that Wirefox has read/write permissions for the configuration file and network interface.

---

## About Wirefox

Wirefox is an all-in-one solution for simplifying remote proxy setup. With its lightweight design and powerful Python backend, Wirefox is the ideal tool for SecOps and pentesting professionals needing quick and reliable IP discovery.

Whether you're using it for remote operations or as part of a broader infrastructure, Wirefox delivers ease of use, reliability, and precision.
