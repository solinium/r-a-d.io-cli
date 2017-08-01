# **a lightweight command-line client for [r/a/dio](https://r-a-d.io)** 

[![Build Status](https://travis-ci.org/solinium/r-a-d.io-cli.svg?branch=master)](https://travis-ci.org/solinium/r-a-d.io-cli)

Written in Python 3 using r/a/dio's [API](https://r-a-d.io/api).

At the moment, this is only tested on Linux.

### Installing

If you are not using X, don't install xdg-utils. You will not be able to open the thread. (If you are unsure, this probably doesn't apply to you.)

##### Debian & Ubuntu
```
sudo apt-get install python3-pip xdg-utils mpv curl
sudo pip3 install -U requests
bash <(curl -s https://raw.githubusercontent.com/solinium/r-a-d.io-cli/master/install.sh)
```

##### Fedora
```
sudo dnf install python3-pip xdg-utils mpv curl
sudo pip3 install -U requests
bash <(curl -s https://raw.githubusercontent.com/solinium/r-a-d.io-cli/master/install.sh)
```

##### Arch Linux

```
sudo pacman -S python-pip xdg-utils mpv curl
sudo pip install -U requests
bash <(curl -s https://raw.githubusercontent.com/solinium/r-a-d.io-cli/master/install.sh)
```

##### CentOS
```
sudo yum install python3-pip xdg-utils mpv curl
sudo pip3 install -U requests
bash <(curl -s https://raw.githubusercontent.com/solinium/r-a-d.io-cli/master/install.sh)
```

### Uninstalling
```
bash <(curl -s https://raw.githubusercontent.com/solinium/r-a-d.io-cli/master/uninstall.sh)
```

### Usage
Call radiocli with -u and a number to choose the interval in which the timer updates, use -t to open the thread (if it exists), and use -h for help. All flags are optional.

Example:
`radiocli -t -u 10`

### Issues
You may notice the timer jumping frequently. That's because by default API requests are being sent every 5 seconds, so it is likely that either your connection or r/a/dio is being slow. You can call radiocli with the -u option to specify how often it updates.


### Contributing
Unstable or testing commits are made in the development branch. Follow PEP8.
