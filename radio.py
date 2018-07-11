#!/usr/bin/env python3

from time import sleep
from shutil import which
from datetime import timedelta
from os import system, remove, environ
from sys import exit, platform, stdout
from requests import ConnectionError, get as rget


def audio():
    audiourl = 'https://relay0.r-a-d.io/main.mp3'
    ipcfile = '--input-ipc-server=/tmp/mpvsocket'
    parameters = '--pause --player-operation-mode=cplayer --no-config --no-video --no-msg-color --terminal --really-quiet --no-input-default-bindings --input-conf=/tmp/mpvbinds'
    system('mpv %s %s %s &' % (parameters, ipcfile, audiourl))


def getVars():
    global updateTime
    try:
        if environ['updatetime'] != "":
            updateTime = int(environ['updatetime'])
    except KeyError:
        updateTime = 30
    global openThread
    try:
        if environ['openthread'] == "true":
            openThread = True
    except KeyError:
        openThread = False
    global volume
    volume = 100
    try:
        if environ['radiovolume'] != "":
            if int(environ['radiovolume']) < 1 or int(environ['radiovolume']) > 100:
                print('volume must be 1-100!')
                sleep(2)
            else:
                volume = int(environ['radiovolume'])
    except KeyError:
        pass
    global updateFrequencyFunction
    updateFrequencyFunction = 100


def getAPI():
    apiurl = 'https://r-a-d.io/api'
    useragent = 'Mozilla/5.0'
    try:
        apiraw = rget(url=apiurl, headers={'User-agent': useragent})
    except ConnectionError:
        system(socketPause)
        system('clear')
        stdout.write("\x1b]2;r-a-d.io-cli\x07")
        print("Connection error, retrying in 5 seconds...")
        sleep(5)
        main()
    global api
    api = apiraw.json()
    global djName
    djName = api['main']['dj']['djname']
    global djImage
    djImage = api['main']['dj']['djimage']
    global djDescription
    djDescription = api['main']['dj']['djtext']
    global isAfkStream
    isAfkStream = api['main']['isafkstream']
    global threadUrl
    threadUrl = api['main']['thread']
    global listeners
    listeners = api['main']['listeners']
    global songTitle
    songTitle = api['main']['np']
    global requesting
    requesting = api['main']['requesting']
    global startTime
    startTime = api['main']['start_time']
    global endTime
    endTime = api['main']['end_time']
    global currentTime
    currentTime = api['main']['current']


def functionAPI():
    if isAfkStream:
        global isAfkStreamStr
        isAfkStreamStr = "(Automated Stream)"
    global isThreadUp
    if (threadUrl != "" and threadUrl != "none") or djName != "Hanyuu-sama":
        isThreadUp = True
    else:
        isThreadUp = False


def getSongLength():
    global songLengthSeconds
    songLengthSeconds = endTime - startTime
    readableSongLength = str(timedelta(seconds=songLengthSeconds))
    tempSongLength = readableSongLength[2:3]
    global songLength
    if tempSongLength == 0:
        songLength = readableSongLength[2:7]
    else:
        songLength = readableSongLength[3:7]


def getSongTimeLeft():
    global songcTimeLeft
    songcTimeLeft = endTime - currentTime
    readableSongcTimeLeft = str(timedelta(seconds=songcTimeLeft))
    tempSongcTimeLeft = readableSongcTimeLeft[2:3]
    if tempSongcTimeLeft == 0:
        formattedSongcTimeLeft = readableSongcTimeLeft[2:7]
    else:
        formattedSongcTimeLeft = readableSongcTimeLeft[3:7]
    formattedSongcTimeLeft = "%s/%s" % (formattedSongcTimeLeft, songLength)
    global songTimeLeft
    songTimeLeft = formattedSongcTimeLeft


def getSongTimeCurrent():
    global currentSongcTime
    currentSongcTime = songLengthSeconds - songcTimeLeft
    readableCurrentSongcTime = str(timedelta(seconds=currentSongcTime))
    tempCurrentSongcTime = readableCurrentSongcTime[2:3]
    global currentSongTime
    if tempCurrentSongcTime == 0:
        currentSongTime = readableCurrentSongcTime[2:7]
    else:
        currentSongTime = readableCurrentSongcTime[3:7]
    currentSongTime = "%s/%s" % (currentSongTime, songLength)


def hybridTimer():
    global timerMax
    global timerCurrentSeconds
    global tempTitle
    timerCurrentSeconds = currentSongcTime
    timerMax = songLengthSeconds
    tempTitle = songTitle
    system('clear')
    if platform.startswith('darwin'):
        print("MacOS detected.")
    print(
        "\u001b[32;1mwelcome to r/a/dio-cli!\033[0m\npress ctrl+c to exit,\npress space to pause.\n")
    if isThreadUp:
        print("\u001b[32;1mmeguca thread is online.\033[0m")
    else:
        print("meguca thread is probably not up.")
    if openThread:
        if isThreadUp:
            print("\nopening thread...")
            if platform.startswith('darwin'):
                system('open %s' % threadUrl)
            else:
                if which('xdg-open') == None:
                    print(
                        'warning: xdg-utils is not installed! you will not be able to open the thread.')
                else:
                    system('xdg-open %s' % threadUrl)
    sleep(4)
    stdout.write('\x1b]2;%s\x07' % songTitle)
    system('clear')
    while True:
        if timerCurrentSeconds % updateTime == 0 or timerCurrentSeconds >= timerMax or tempTitle != songTitle:
            updateAPI()
            stdout.write('\x1b]2;%s\x07' % songTitle)
        else:
            timerCurrentSeconds = timerCurrentSeconds + 1
            if str(timedelta(seconds=timerCurrentSeconds))[2:3] == 0:
                timerCurrent = str(timedelta(seconds=timerCurrentSeconds))[2:7]
            else:
                timerCurrent = str(timedelta(seconds=timerCurrentSeconds))[3:7]
            timerCurrent = "%s/%s" % (timerCurrent, songLength)
            system('clear')
            print("\u001b[32;1m%s\033[0m" % songTitle + '|')
            if len(timerCurrent) > len(songTitle):
                print(timerCurrent + '|')
            else:
                print(timerCurrent +
                      (' ' * (len(songTitle) - len(timerCurrent))) + '|')
            print(' ' * len(songTitle) + '|')
            if (len(djName) + 4) > len(songTitle):
                print("DJ: %s" % djName + '|')
            else:
                print("DJ: %s" % djName +
                      (' ' * (len(songTitle) - (len(djName) + 4))) + '|')
            if isAfkStream:
                if len(isAfkStreamStr) > len(songTitle):
                    print(isAfkStream + '|')
                else:
                    print(isAfkStreamStr +
                          (' ' * (len(songTitle) - len(isAfkStreamStr))) + '|')
            print(' ' * len(songTitle) + '|')
            if (len(str(listeners)) + 11) > len(songTitle):
                print("Listeners: %s" % listeners + '|')
            else:
                print("Listeners: %s" % listeners + (' ' *
                                                     (len(songTitle) - (len(str(listeners)) + 11))) + '|')
            print('-' * (len(songTitle) + 1))
            sleep(1)


def updateAPI():
    getAPI()
    getSongLength()
    getSongTimeLeft()
    getSongTimeCurrent()
    global timerMax
    global timerCurrentSeconds
    global tempTitle
    timerCurrentSeconds = currentSongcTime
    timerMax = songLengthSeconds
    tempTitle = songTitle
    if timerCurrentSeconds % 100 == 0:
        functionAPI()


def main():
    print('\33]0;r-a-d.io-cli\a', end='', flush=True)
    updateAPI()
    functionAPI()
    system(socketPause)
    system(socketVolume % volume)
    hybridTimer()


if __name__ == "__main__":
    def checkInstall(dependencies):
        depsInstalled = True
        for dep in dependencies:
            if which(dep) == None:
                print("%s is not installed!" % dep)
                depsInstalled = False
        if not(depsInstalled):
            exit(1)
    dependencies = ['mpv', 'curl', 'socat']
    checkInstall(dependencies)
    binds = 'SPACE cycle "pause"'
    with open('/tmp/mpvbinds', "w") as mpvbinds:
        print(binds, file=mpvbinds)
    global socketPause
    global socketVolume
    socketPause = '''echo '{ "command": ["cycle", "pause"] }' | socat - /tmp/mpvsocket; clear'''
    socketVolume = '''echo '{ "command": ["set_property", "volume", %s] }' | socat - /tmp/mpvsocket; clear'''
    try:
        getVars()
        audio()
        main()
    except (KeyboardInterrupt):
        remove('/tmp/mpvbinds')
        system('clear')
