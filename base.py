#!/usr/bin/env python3
import os
import sys
import json
import requests
import datetime
#import pprint
import webbrowser
import subprocess

def importAPI():
	global api
	apiraw = requests.get(url='https://r-a-d.io/api', headers={'User-agent': 'Mozilla/5.0'})
	api = apiraw.json()

def extractJson():
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

#def extractQueue():


	#test arrays

	#pprint.pprint(api)

	#global queueTitle1
	#queueTitle1 = api['main']['queue']['0']['meta']

	#global queueTime1
	#queueTime1 = api['main']['queue']['0']['timestamp']

	#global queueTitle2
	#queueTitle2 = api['main']['queue']['1']['meta']

	#global queueTime2
	#queueTime2= api['main']['queue']['1']['timestamp']
	
	#global queueTitle3
	#queueTitle3 = api['main']['queue']['2']['meta']

	#global queueTime3
	#queueTime1 = api['main']['queue']['2']['timestamp']

	#global queueTitle4
	#queueTitle4 = api['main']['queue']['3']['meta']

	#global queueTime4
	#queueTime1 = api['main']['queue']['3']['timestamp']

	#global queueTitle5
	#queueTitle4 = api['main']['queue']['4']['meta']

	#global queueTime5
	#queueTime1 = api['main']['queue']['4']['timestamp']

#def calculateQueueTime(x, y):
#	if y == (1):
#		global queueStartSecs1
#		queueStartSecs1 = (x - currentTime)
#	elif y == (2):
#		global queueStartSecs2
#		queueStartSecs2 = (x - currentTime)
#	elif y == (3):
#		global queueStartSecs3
#		queueStartSecs3 = (x - currentTime)
#	elif y == (4):
#		global queueStartSecs4
#		queueStartSecs = (x - currentTime)
#	elif y == (5):
#		global queueStartSecs5
#		queueStartSecs5= (x - currentTime)

def functionJson():
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

	#calculateQueueTime(queueTime1, 1)
	#calculateQueueTime(queueTime2, 2)
	#calculateQueueTime(queueTime3, 3)
	#calculateQueueTime(queueTime4, 4)
	#calculateQueueTime(queueTime5, 5)

def songTimeLength():
	global songLengthSeconds
	songLengthSeconds = (endTime - startTime)

	readableSongLength = str(
		datetime.timedelta(seconds=songLengthSeconds))

	tempSongLength = readableSongLength[2:3]
	global totalSongTime
	if tempSongLength == (0):
		totalSongTime = readableSongLength[2:7]
	else:
		totalSongTime = readableSongLength[3:7]

def songTimeLeft():
	global currentSongcTimeLeft
	currentSongcTimeLeft = endTime - currentTime

	readableCurrentSongcTimeLeft = str(
		datetime.timedelta(seconds=currentSongcTimeLeft))

	tempCurrentSongcTimeLeft = readableCurrentSongcTimeLeft[2:3]

	if tempCurrentSongcTimeLeft == (0):
		formattedCurrentSongcTimeLeft = readableCurrentSongcTimeLeft[2:7]
	else:
		formattedCurrentSongcTimeLeft = readableCurrentSongcTimeLeft[3:7]

	formattedCurrentSongcTimeLeft = ("%s/%s") % (
		formattedCurrentSongcTimeLeft, totalSongTime)

	global currentSongTimeLeft
	currentSongTimeLeft = formattedCurrentSongcTimeLeft

def songTimeCurrent():
	global currentSongcTime
	currentSongcTime = (songLengthSeconds - currentSongcTimeLeft)

	readableCurrentSongcTime = str(
		datetime.timedelta(seconds=currentSongcTime))

	tempCurrentSongcTime = readableCurrentSongcTime[2:3]

	if tempCurrentSongcTime == (0):
		formattedCurrentSongcTime = readableCurrentSongcTime[2:7]
	else:
		formattedCurrentSongcTime = readableCurrentSongcTime[3:7]

	formattedCurrentSongcTime = ("%s/%s") % (
		formattedCurrentSongcTime, totalSongTime)

	global currentSongTime
	currentSongTime = formattedCurrentSongcTime
	
	# totalSongTime is song length
	# currentSongTime is how far in the song
	# currentSongTimeLeft is how much time is left
	print(songTitle)
	print(totalSongTime)
	print(currentSongTime)
	print(currentSongTimeLeft)

def openThread():
	global thread
	if isOldThread == (False):
		if sys.platform == ('darwin'):	#osx
			subprocess.Popen(['open', threadUrl])
		else:
			webbrowser.get('firefox').open(threadUrl)
	else:
		print()
		print("Sorry, thread is not up.")
		print()

def start():
	importAPI()

	extractJson()

	#extractQueue()

	functionJson()

	songTimeLength()

	songTimeLeft()

	songTimeCurrent()

if __name__ == ("__main__"):
	start()
