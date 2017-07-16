#!/usr/bin/env python3


def getPlatform():
	from os import environ
	from sys import platform

	global unix
	if platform.startswith('linux') == (True) or (
		platform.startswith('darwin')) == (True) or (
			platform.startswith('freebsd')) == (True) or (
				platform.startswith('openbsd')) == (True) or (
					platform.startswith('cygwin')) == (True) or (
						platform.startswith('posix')) == (True):
							unix = (True)
	else:
		unix = (False)

	global isTravis
	isTravis = 'TRAVIS' in environ


def keyboard():
	if isTravis != (True):
		from keyboard import wait
		print("Press space to start!")
		wait('space')


def getAPI():
	from requests import get

	apiurl = ("https://r-a-d.io/api")
	useragent = ("Mozilla/5.0")
	apiraw = get(url=apiurl, headers={'User-agent': useragent})

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
	if isAfkStream == (True):
		global isAfkStreamStr
		isAfkStreamStr = ("Automated Stream")

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

	global tempTitle
	tempTitle = songTitle


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
	from time import sleep
	from datetime import timedelta

	global timerCurrent
	global timerCurrentSeconds

	timerCurrentSeconds = (currentSongcTime)
	timerMax = songLengthSeconds

	if unix == (True):
		system('clear')
	else:
		system('cls')

	while (timerCurrentSeconds < timerMax):
		timerCurrentSeconds = (timerCurrentSeconds + 1)

		if (timerCurrentSeconds % 5) == (0) or timerCurrentSeconds == (
			timerMax) or tempTitle != (
				songTitle):
					getAPI()
					functionAPI()
					getSongLength()
					getSongTimeLeft()
					getSongTimeCurrent()
					timerCurrentSeconds = (currentSongcTime)
					timerMax = songLengthSeconds

		timerCurrentReadable = str(
			timedelta(seconds=timerCurrentSeconds))

		timerCurrentTemp = timerCurrentReadable[2:3]

		if timerCurrentTemp == (0):
			timerCurrent = timerCurrentReadable[2:7]
		else:
			timerCurrent = timerCurrentReadable[3:7]

		timerCurrent = ("%s/%s") % (
			timerCurrent, songLength)

		if unix == (True):
			system('clear')
		elif unix == (False):
			system('cls')

		print(songTitle)
		print()
		print(timerCurrent)
		print("\n" * 5)
		print(djName)

		try:
			print(isAfkStreamStr)
			print()
		except:
			print()

		print("Listeners: %s" % (listeners))
		sleep(1)

# songLength is song length
# currentSongTime is how far in the song
# songTimeLeft is how much time is left
# timerCurrent is current song time (hybrid)


def start():
	getPlatform()

	keyboard()

	trueBool = (True)
	while trueBool == (True):
		getAPI()

		functionAPI()

		getSongLength()

		getSongTimeLeft()

		getSongTimeCurrent()

		hybridTimer()


if __name__ == ("__main__"):
	start()
