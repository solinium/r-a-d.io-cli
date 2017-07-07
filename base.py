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

	if tempCurrentSongcTime == (0):
		formattedCurrentSongcTime = readableCurrentSongcTime[2:7]
	else:
		formattedCurrentSongcTime = readableCurrentSongcTime[3:7]

	formattedCurrentSongcTime = ("%s/%s") % (
		formattedCurrentSongcTime, songLength)

	global currentSongTime
	currentSongTime = formattedCurrentSongcTime

	# songLength is song length
	# currentSongTime is how far in the song
	# songTimeLeft is how much time is left


def testing():
	from os import system
	from sys import platform

	if platform == ('darwin'):
		system('clear')
	elif platform == ('posix'):
		system('clear')
	elif platform == ('linux'):
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


def start():
	getAPI()

	getSongLength()

	getSongTimeLeft()

	getSongTimeCurrent()

	# testing()


if __name__ == ("__main__"):
	start()
