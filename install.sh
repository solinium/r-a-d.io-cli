#!/bin/sh

cd $HOME
git clone https://github.com/solinium/r-a-d.io-cli.git
sudo mkdir -p /opt/r-a-d.io-cli/
sudo cp $HOME/r-a-d.io-cli/cli.py /opt/r-a-d.io-cli/cli.py
sudo cp $HOME/r-a-d.io-cli/audio.py /opt/r-a-d.io-cli/audio.py
sudo cp $HOME/r-a-d.io-cli/start.sh /usr/bin/radiocli
sudo chmod +x /usr/bin/radiocli
rm -rf $HOME/r-a-d.io-cli/
clear
echo 'Install Completed! Launch r/a/dio-cli with "radiocli".'