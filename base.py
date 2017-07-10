#!/usr/bin/env python3


def getAPI():
	from requests import get

	apiurl = ("https://r-a-d.io/api")
	apiraw = get(url=apiurl, headers={'User-agent': 'Mozilla/5.0'})
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
	global isAfkStreamStr
	if isAfkStream == (True):
		isAfkStreamStr = ("AFK Stream")
	else:
		isAfkStreamStr = ("")

	global isOldThread
	if threadUrl != (""):
		if djName == ("Hanyuu-sama"):
			isOldThread = (True)
		else:
			isOldThread = (False)

	global isThreadUp
	if isOldThread == (False):
		isThreadUp = (True)
	else:
		isThreadUp = (False)


def getSongLength():
	from datetime import timedelta

	global songLengthSeconds
	songLengthSeconds = (endTime - startTime)

	readableSongLength = str(
		timedelta(seconds=songLengthSeconds))

	tempSongLength = readableSongLength[2:3]

	global songLength
	if tempSongLength == (0):
		songLength = readableSongLength[2:7]
	else:
		songLength = readableSongLength[3:7]


def getSongTimeLeft():
	from datetime import timedelta

	global songcTimeLeft
	songcTimeLeft = endTime - currentTime

	readableSongcTimeLeft = str(
		timedelta(seconds=songcTimeLeft))

	tempSongcTimeLeft = readableSongcTimeLeft[2:3]

	if tempSongcTimeLeft == (0):
		formattedSongcTimeLeft = readableSongcTimeLeft[2:7]
	else:
		formattedSongcTimeLeft = readableSongcTimeLeft[3:7]

	formattedSongcTimeLeft = ("%s/%s") % (
		formattedSongcTimeLeft, songLength)

	global songTimeLeft
	songTimeLeft = formattedSongcTimeLeft


def getSongTimeCurrent():
	from datetime import timedelta

	global currentSongcTime
	currentSongcTime = (songLengthSeconds - songcTimeLeft)

	readableCurrentSongcTime = str(
		timedelta(seconds=currentSongcTime))

	tempCurrentSongcTime = readableCurrentSongcTime[2:3]

	global currentSongTime
	if tempCurrentSongcTime == (0):
		currentSongTime = readableCurrentSongcTime[2:7]
	else:
		currentSongTime = readableCurrentSongcTime[3:7]

	currentSongTime = ("%s/%s") % (
		currentSongTime, songLength)


def hybridTimer():
	from os import system
	from sys import platform
	from time import sleep
	from time import timedelta

	global timerCurrent
	global timerCurrentSeconds

	timerCurrentSeconds = (0)
	timerMax = songLengthSeconds
	tempTitle = songTitle

	while (timerCurrentSeconds < timerMax):
		timerCurrentSeconds = (timerCurrentSeconds + 1)

		if (timerCurrentSeconds % 5) == (0) or timerCurrentSeconds == (
			timerMax):
			getAPI()
			getSongLength()
			getSongTimeLeft()
			getSongTimeCurrent()
			if tempTitle != songTitle:
				timerCurrentSeconds = (0)
			timerMax = songLengthSeconds
			tempTitle = songTitle

		timerCurrentReadable = str(
			timedelta(seconds=timerCurrentSeconds))

		timerCurrentTemp = timerCurrentReadable[2:3]

		if timerCurrentTemp == (0):
			timerCurrent = timerCurrentReadable[2:7]
		else:
			timerCurrent = timerCurrentReadable[3:7]

		timerCurrent = ("%s/%s") % (
			timerCurrent, songLength)

		if platform == ('linux') or ('darwin') or ('posix'):
			system('clear')
		else:
			system('cls')

		print("Title:")
		print(songTitle)
		print()
		print("Length:")
		print(songLength)
		print()
		print("Current Time:")
		print(currentSongTime)
		print()
		print("Time Left:")
		print(songTimeLeft)
		print()
		print("Hybrid Time Left:")
		print(timerCurrent)
		sleep(1)

# songLength is song length
# currentSongTime is how far in the song
# songTimeLeft is how much time is left
# timerCurrent is current song time (hybrid)


def start():
	getAPI()

	functionAPI()

	getSongLength()

	getSongTimeLeft()

	getSongTimeCurrent()

	hybridTimer()


if __name__ == ("__main__"):
	start()
