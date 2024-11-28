#!/bin/bash

# Installer for Wirefox Services

# Check if the script is being run as root
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# Check if pip/python is installed
which python3
if [ $? -ne 0 ]; then
    echo "Error: Python3 is not installed"
    exit 1
fi

pip install requests

# Download the script
curl https://raw.githubusercontent.com/jleuth/wirefox/refs/heads/main/wirefox.py > wirefox.py
chmod +x wirefox.py
mv wirefox.py /usr/bin/wirefox

sudo wirefox --install-service
sudo systemctl start wirefox
sudo systemctl enable wirefox

echo "Wirefox has been installed and started as a service. Edit the configuration file at /etc/wirefox.conf to add your Gist and PAT."