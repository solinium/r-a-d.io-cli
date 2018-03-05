#!/bin/sh

sudo clear
git clone https://github.com/solinium/r-a-d.io-cli.git /tmp/r-a-d.io-cli
sudo mkdir /opt/r-a-d.io-cli/
sudo cp /tmp/r-a-d.io-cli/radio.py /opt/r-a-d.io-cli/radio.py
sudo cp start.sh /usr/bin/radiocli
sudo chmod +x /usr/bin/radiocli
rm -rf /tmp/r-a-d.io-cli/
clear
echo 'Install Completed! Launch r/a/dio-cli with "radiocli".'