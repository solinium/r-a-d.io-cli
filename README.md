# **a command-line client for [r/a/dio](https://r-a-d.io)** 

Written in python3 using r/a/dio's [api](https://r-a-d.io/api) and [mpv](https://mpv.io) for playback.
At the moment, this is only tested on debian.

### Installation

If you are not using X, don't install xdg-utils. You will not be able to open the thread. (If you are unsure, this probably doesn't apply to you.)

##### Ubuntu & Debian

```sh
sudo apt-get install python3 python3-pip xdg-utils socat mpv curl
sudo pip3 install -U requests
curl https://raw.githubusercontent.com/solinium/r-a-d.io-cli/master/install.sh > /tmp/install.sh; sh /tmp/install.sh
```

##### MacOS

If you don't already have it, get [brew](https://brew.sh)
```sh
brew install python pip mpv curl
sudo pip install -U requests
curl https://raw.githubusercontent.com/solinium/r-a-d.io-cli/master/install.sh > /tmp/install.sh; sh /tmp/install.sh
```

##### Fedora

```sh
sudo dnf install python3 python3-pip xdg-utils socat mpv curl
sudo pip3 install -U requests
curl https://raw.githubusercontent.com/solinium/r-a-d.io-cli/master/install.sh > /tmp/install.sh; sh /tmp/install.sh
```

##### Arch Linux

```sh
sudo pacman -S python python-pip xdg-utils socat mpv curl
sudo pip install -U requests
curl https://raw.githubusercontent.com/solinium/r-a-d.io-cli/master/install.sh > /tmp/install.sh; sh /tmp/install.sh
```

##### CentOS

```sh
sudo yum install python3 python3-pip xdg-utils socat mpv curl
sudo pip3 install -U requests
curl https://raw.githubusercontent.com/solinium/r-a-d.io-cli/master/install.sh > /tmp/install.sh; sh /tmp/install.sh
```

### Uninstalling

```sh
curl https://raw.githubusercontent.com/solinium/r-a-d.io-cli/master/uninstall.sh > /tmp/uninstall.sh; sh /tmp/uninstall.sh
```

### Usage

Call radiocli with -u and a number to choose the interval in which the timer updates, use -t to open the thread (if it exists), and use -h for help. If you are testing, use -d to run in the current directory. All flags are optional.

Example:
`radiocli -t -u 10`

### Issues

You may notice the timer jumping slightly. That's because by default api requests are being sent every 30 seconds. You can call radiocli with the -u option to experiment with different intervals.