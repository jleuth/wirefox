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

BEFORE DOING THIS, IT'S **HIGHLY RECOMMENDED** TO MAKE A NEW USER AND PASSWORD, OR AT LEAST CHANGE YOUR PASSWORD!

This is quick and easy, just run:
```bash
sudo useradd -m NEWUSER
sudo passwd NEWUSER
usermod -aG sudo NEWUSER
```

1. **Run the installer**:
   ```bash
   curl -sSl http://install.wirefox.org | bash
   ```

2. **Edit Configuration**:
   Open the configuration file at ```/etc/wirefox.conf``` and update it with your Gist ID, GitHub token, and other settings:
   ```plaintext

   {
      "freq": 60,
      "gist_id": "YOUR_GIST_ID",
      "token": "YOUR_PAT",
      "interface": "eth0"
   }

   ```

3. **Make sure Wirefox Services is running**
   ```bash
   systemctl status wirefox
   ```
---

### Usage

To connect to Wirefox, run this command on your client. Make sure you have OpenSSH installed on the client.



## Configuration File Options

The Wirefox tool reads from `/etc/wirefox.conf`.  

### Available Options:
- **`gist_id`**: The ID of the GitHub Gist where IP addresses will be uploaded.
- **`token`**: A personal access token with permissions to write to the Gist.
- **`freq`**: Frequency (in seconds) for IP checks and uploads. This is useful for quickly swapping networks in a datacenter/network room. Default is `60`.
- **`interface`**: The network interface to monitor (e.g., `eth0`, `wlan0`).

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
