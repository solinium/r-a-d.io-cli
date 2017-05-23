#!/usr/bin/env python3
import jsonread
import datetime
from time import sleep

def clearScreen():
	print ("\n" * 200)

#temporary workaround (terrible hack) (but it works tho)
def timerFormat():
	global songLengthSeconds
	songLengthSeconds = jsonread.endTime - jsonread.startTime

	global currentSongTime
	currentSongTime = jsonread.current

	readableSongLength = str(datetime.timedelta(seconds=songLengthSeconds))

	testSongLength = readableSongLength[2:3]
	global formattedSongLength
	if testSongLength == 0:
		formattedSongLength = readableSongLength[2:7]
	else:
		formattedSongLength = readableSongLength[3:7]

	#global currentSongTime
	#currentSongTime = 0

	print(jsonread.songTitle)
	print()
	print(formattedSongLength)

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

	clearScreen()