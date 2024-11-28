#!/bin/bash

# Installer for Wirefox Services

# Check if pip/python is installed
which python3
if [ $? -ne 0 ]; then
    echo "Error: Python3 is not installed"
    exit 1
fi

which pip3
if [ $? -ne 0 ]; then
    echo "Error: Pip3 is not installed"
    exit 1
fi

pip3 install requests -q

# Download the script
curl https://raw.githubusercontent.com/jleuth/wirefox/refs/heads/main/wirefox.py > wirefox.py
chmod +x wirefox.py
echo "We need to root for the rest of the install, please enter your password"
sudo mv wirefox.py /usr/bin/wirefox

sudo wirefox --install-service
sudo systemctl start wirefox
sudo systemctl enable wirefox

echo "Wirefox has been installed and started as a service. Edit the configuration file at /etc/wirefox.conf to add your Gist and PAT."
