#!/usr/bin/env python3
import os
import sys
import json
import datetime
import webbrowser
import subprocess

def importJson():
	global data
	with open('api.json') as data_file:    
		data = json.load(data_file)

	# end of importJson


def extractJson():
	global djName
	djName = data['main']['dj']['djname']

	global djImage
	djImage = data['main']['dj']['djimage']

	global djDescription
	djDescription = data['main']['dj']['djtext']

	global isAfkStream
	isAfkStream = data['main']['isafkstream']

	global threadUrl
	threadUrl = data['main']['thread']

	global listeners
	listeners = data['main']['listeners']

	global songTitle
	songTitle = data['main']['np']

	global requesting
	requesting = data['main']['requesting']

	global startTime
	startTime = data['main']['start_time']

	global endTime
	endTime = data['main']['end_time']

	global currentTime
	currentTime = data['main']['current']

	# end of extractJson


def functionJson():
	global isAfkStreamStr

	if isAfkStream == True:
		isAfkStreamStr = "AFK Stream"
	else:
		isAfkStreamStr = ""

	global isThreadUp

	if threadUrl == (""):
		isThreadUp = (False)
	else:
		if djName == ("Hanyuu-sama"):
			isThreadUp = (False)
		else:
			isThreadUp = (True)

	# end of functionJson


def timerFormat():
	global songLengthSeconds
	songLengthSeconds = jsonread.endTime - jsonread.startTime

	global currentSongcTime
	currentSongcTime = jsonread.endTime - jsonread.currentTime

	readableSongLength = str(
		datetime.timedelta(seconds=songLengthSeconds))

	readableCurrentSongcTime = str(
		datetime.timedelta(seconds=currentSongcTime))

	tempSongLength = readableSongLength[2:3]
	global totalSongTime
	if tempSongLength == 0:
		totalSongTime = readableSongLength[2:7]
	else:
		totalSongTime = readableSongLength[3:7]

	tempCurrentSongcTime = readableCurrentSongcTime[2:3]
	if tempCurrentSongcTime == 0:
		formattedCurrentSongcTime = readableCurrentSongcTime[2:7]
	else:
		formattedCurrentSongcTime = readableCurrentSongcTime[3:7]

	formattedCurrentSongcTime = ("%s/%s") % (formattedCurrentSongcTime, totalSongTime)

	global currentSongTime
	currentSongTime = formattedCurrentSongcTime

	# currentSongTime is the real current time
	# totalSongTime is final song length

	# end of timeFormat


def openThread():
	if jsonread.threadUp:
		if sys.platform == 'darwin':	#osx
			subprocess.Popen(['open', jsonread.threadUrl])
		else:
			webbrowser.get('firefox').open(jsonread.threadUrl)
	else:
		print()
		print("Sorry, thread is not up.")
		print()

		# end of openThread


def start():
	importJson()

	extractJson()

	functionJson()

	timerFormat()

if __name__ == "__main__":
	start()
