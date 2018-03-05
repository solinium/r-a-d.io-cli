# **a lightweight command-line client for [r/a/dio](https://r-a-d.io)** 

Written in python3 using r/a/dio's [api](https://r-a-d.io/api) and [mpv](https://mpv.io) for playback.
At the moment, this is only tested on debian.
### Installing

If you are not using X, don't install xdg-utils. You will not be able to open the thread. (If you are unsure, this probably doesn't apply to you.)

##### Debian & Ubuntu
```
sudo apt-get install python3 python3-pip xdg-utils mpv curl
sudo pip3 install -U requests
curl https://raw.githubusercontent.com/solinium/r-a-d.io-cli/master/install.sh > /tmp/install.sh; sh /tmp/install.sh
```

##### MacOS
```
brew install python pip mpv curl
sudo pip install -U requests
curl https://raw.githubusercontent.com/solinium/r-a-d.io-cli/master/install.sh > /tmp/install.sh; sh /tmp/install.sh
```
##### Fedora
```
sudo dnf install python3 python3-pip xdg-utils mpv curl
sudo pip3 install -U requests
curl https://raw.githubusercontent.com/solinium/r-a-d.io-cli/master/install.sh > /tmp/install.sh; sh /tmp/install.sh
```

##### Arch Linux
```
sudo pacman -S python python-pip xdg-utils mpv curl
sudo pip install -U requests
curl https://raw.githubusercontent.com/solinium/r-a-d.io-cli/master/install.sh > /tmp/install.sh; sh /tmp/install.sh
```

##### CentOS
```
sudo yum install python3 python3-pip xdg-utils mpv curl
sudo pip3 install -U requests
curl https://raw.githubusercontent.com/solinium/r-a-d.io-cli/master/install.sh > /tmp/install.sh; sh /tmp/install.sh
```

### Uninstalling
```
curl https://raw.githubusercontent.com/solinium/r-a-d.io-cli/master/uninstall.sh > /tmp/uninstall.sh; sh /tmp/uninstall.sh
```

### Usage
Call radiocli with -u and a number to choose the interval in which the timer updates, use -t to open the thread (if it exists), and use -h for help. If you are testing, use -d to run in the current directory. All flags are optional.

Example:
`radiocli -t -u 10`

### Issues
You may notice the timer jumping frequently. That's because by default api requests are being sent every 5 seconds, so it is likely that either your connection or r/a/dio is being slow. You can call radiocli with the -u option to specify how often it updates.