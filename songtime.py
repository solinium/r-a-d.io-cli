#!/usr/bin/env python3	
import jsonread
import datetime
from time import sleep

def clearScreen():
	print ("\n" * 200)

def timerFormat():
	global songLengthSeconds
	songLengthSeconds = jsonread.endTime - jsonread.startTime 

	global currentSongcTime
	currentSongcTime = jsonread.endTime - jsonread.currentTime

	readableSongLength = str(datetime.timedelta(seconds=songLengthSeconds))

	readableCurrentSongcTime = str(datetime.timedelta(seconds=currentSongcTime))

	tempSongLength = readableSongLength[2:3]
	global formattedSongLength
	if tempSongLength == 0:
		formattedSongLength = readableSongLength[2:7]
	else:
		formattedSongLength = readableSongLength[3:7]

	tempCurrentSongcTime = readableCurrentSongcTime[2:3]
	global formattedSongLength
	if tempCurrentSongcTime == 0:
		formattedCurrentSongcTime = readableCurrentSongcTime[2:7]
	else:
		formattedCurrentSongcTime = readableCurrentSongcTime[3:7]
	formattedCurrentSongcTime = ("%s/%s") % (formattedCurrentSongcTime, formattedSongLength)
	

	#global currentSongTime
	#currentSongTime = 0

	print(jsonread.songTitle)
	print()
	print(formattedSongLength)
	print()
	print(currentSongcTime)
	print()
	print(formattedCurrentSongcTime)

	sleep(5)
	#while songLengthSeconds > currentSongTime:
	#sleep(1)
	#currentSongTime = currentSongTime + 1
	#songTimeMins, songTimeSecs = divmod(currentSongTime, 60)
	#if songTimeSecs < 10
	#global formattedCurrentSongTime
	#formattedCurrentSongTime = "%s:%s" % (songTimeMins, songTimeSecs)
	#if len(formattedCurrentSongTime) == 3:
		#formattedCurrentSongTime = (formattedCurrentSongTime[0:2] + "0" + formattedCurrentSongTime[2:3])
	#print(currentSongTime)
	print()