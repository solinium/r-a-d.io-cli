#!/usr/bin/env python3
import jsonread
import datetime

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