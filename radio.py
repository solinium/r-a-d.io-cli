#!/usr/bin/env python3

from datetime import timedelta
from os import environ, system
from sys import exit, platform, stdout
from time import sleep
from requests import get as rget
from requests import ConnectionError


def audio():
    audiourl = 'https://relay0.r-a-d.io/main.mp3'
    ipcfile = '--input-ipc-server=/tmp/mpvsocket'
    miscparams = '--pause --no-video --really-quiet'
    system('mpv %s %s %s &' % (miscparams, ipcfile, audiourl))
    global socketPause
    socketPause = '''echo '{ "command": ["set_property", "pause", %s] }' | socat - /tmp/mpvsocket; clear'''


def getPlatform():
    global darwin
    if platform.startswith('darwin'):
        darwin = True
    else:
        darwin = False
    global updateTime
    try:
        if environ['frequency'] != "":
            updateTime = int(environ['updatetime'])
    except KeyError:
        updateTime = 5
    global openThread
    try:
        if environ['openthread'] == "true":
            openThread = True
    except KeyError:
        openThread = False
    global updateFrequencyFunction
    updateFrequencyFunction = 100


def getAPI():
    apiurl = 'https://r-a-d.io/api'
    useragent = 'Mozilla/5.0'
    try:
        apiraw = rget(url=apiurl, headers={'User-agent': useragent})
    except ConnectionError:
        system(socketPause % "true")
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
        isAfkStreamStr = "Automated Stream"
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
    formattedSongcTimeLeft = "%s/%s" % formattedSongcTimeLeft, songLength
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
    currentSongTime = "%s/%s" % currentSongTime, songLength


def hybridTimer():
    global timerMax
    global timerCurrentSeconds
    global tempTitle
    timerCurrentSeconds = currentSongcTime
    timerMax = songLengthSeconds
    tempTitle = songTitle
    system('clear')
    if darwin:
        print("MacOS detected.")
    print("Press ctrl+c to exit.")
    if openThread:
        if not(isThreadUp):
            print("\nOpening thread...")
            if darwin:
                system('open %s' % threadUrl)
            else:
                system('xdg-open %s' % threadUrl)
        else:
            print("\nSorry, the thread is probably not up.")
    else:
        if isThreadUp:
            print("Thread is online.")
        else:
            print("Thread is probably not up.")
    sleep(3)
    system('clear')
    while True:
        if timerCurrentSeconds % updateTime == 0 or timerCurrentSeconds == timerMax or tempTitle != songTitle:
            updateAPI()
            stdout.write('\x1b]2;%s\x07' % songTitle)
        else:
            timerCurrentSeconds = timerCurrentSeconds + 1
            timerCurrentReadable = str(timedelta(seconds=timerCurrentSeconds))
            timerCurrentTemp = timerCurrentReadable[2:3]
            if timerCurrentTemp == 0:
                timerCurrent = timerCurrentReadable[2:7]
            else:
                timerCurrent = timerCurrentReadable[3:7]
            timerCurrent = "%s/%s" % timerCurrent, songLength
            system('clear')
            print(songTitle)
            print(timerCurrent + "\n")
            print("DJ: %s" % djName)
            if isAfkStream:
                print(isAfkStreamStr)
            print("\nListeners: %s" % listeners)
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
    stdout.write("\x1b]2;r-a-d.io-cli\x07")
    updateAPI()
    functionAPI()
    system(socketPause % "false")
    hybridTimer()


if __name__ == "__main__":
    try:
        getPlatform()
        audio()
        main()
    except (KeyboardInterrupt):
        system('clear')
        exit()
