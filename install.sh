#!/bin/sh

cd $HOME
git clone https://github.com/solinium/r-a-d.io-cli.git
sudo mkdir -p /opt/r-a-d.io-cli/
sudo cp $HOME/r-a-d.io-cli/cli.py /opt/r-a-d.io-cli/cli.py
sudo cp $HOME/r-a-d.io-cli/audio.py /opt/r-a-d.io-cli/audio.py

ret=`python -c 'import sys; print("%i" % (sys.hexversion<0x03000000))'`

if [ $ret -eq 0 ]; then
	sudo cp $HOME/r-a-d.io-cli/install/p2 /usr/bin/radiocli
else 
	sudo cp $HOME/r-a-d.io-cli/install/p3 /usr/bin/radiocli
fi

sudo chmod +x /usr/bin/radiocli
rm -rf $HOME/r-a-d.io-cli/
clear
echo 'Install Completed! Launch r/a/dio-cli with "radiocli".'