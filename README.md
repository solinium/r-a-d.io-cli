# **a lightweight command-line client for [r/a/dio](https://r-a-d.io)** 

[![Build Status](https://travis-ci.org/solinium/r-a-d.io-cli.svg?branch=master)](https://travis-ci.org/solinium/r-a-d.io-cli)

Written in Python 3 using r/a/dio's [API](https://r-a-d.io/api).

At the moment, this is only tested on Linux.

### Installation

##### Debian & Ubuntu:
```
sudo apt-get install python3-pip mpv curl
sudo pip3 install -U requests
bash <(curl -s https://raw.githubusercontent.com/solinium/r-a-d.io-cli/master/install.sh)
```

##### Fedora:
```
sudo dnf install python3-pip mpv curl
sudo pip3 install -U requests
bash <(curl -s https://raw.githubusercontent.com/solinium/r-a-d.io-cli/master/install.sh)
```

##### Arch Linux:
```
sudo pacman -S python-pip mpv curl
sudo pip install -U requests
bash <(curl -s https://raw.githubusercontent.com/solinium/r-a-d.io-cli/master/install.sh)
```

### Uninstall
`bash <(curl -s https://raw.githubusercontent.com/solinium/r-a-d.io-cli/master/uninstall.sh)`

### Issues
You may notice the timer jumping frequently. That's because by default API requests are being sent every 7 seconds, so it is likely that either your connection or r/a/dio is being slow. I will work on implementing custom request times.

### Contributing
Unstable or testing commits are made in the development branch. Follow PEP8.
