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
  cat /etc/wirefox.conf
  ```
  
- **IPs Not Uploading**:  
  Ensure the Gist ID, Gist filename, and GitHub token are correct. Confirm the token has appropriate permissions.

- **IP Not Changing**:  
  Wirefox skips uploads if the IP addresses remain the same as the last recorded entry. If it still dosen't change after a reboot, check if you have a static IP set, or that the service is valid and running.

- **Permission Errors**:  
  Check that Wirefox has read/write permissions for the configuration file and network interface.
