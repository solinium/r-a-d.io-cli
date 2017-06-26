#!/usr/bin/env python3
import gettime as getTime

getTime.start()

def extractQueue():
	global queueTitle1
	queueTitle1 = getTime.api['main']['queue']['0']['meta']

	global queueTime1
	queueTime1 = getTime.api['main']['queue']['0']['timestamp']

	global queueTitle2
	queueTitle2 = getTime.api['main']['queue']['1']['meta']

	global queueTime2
	queueTime2= getTime.api['main']['queue']['1']['timestamp']

	global queueTitle3
	queueTitle3 = getTime.api['main']['queue']['2']['meta']

	global queueTime3
	queueTime1 = getTime.api['main']['queue']['2']['timestamp']

	global queueTitle4
	queueTitle4 = getTime.api['main']['queue']['3']['meta']

	global queueTime4
	queueTime1 = getTime.api['main']['queue']['3']['timestamp']

	global queueTitle5
	queueTitle4 = getTime.api['main']['queue']['4']['meta']

	global queueTime5
	queueTime1 = getTime.api['main']['queue']['4']['timestamp']

def calculateQueueTime(x, y):
	if y == (1):
		global queueStartSecs1
		queueStartSecs1 = (x - getTime.currentTime)
	elif y == (2):
		global queueStartSecs2
		queueStartSecs2 = (x - getTime.currentTime)
	elif y == (3):
		global queueStartSecs3
		queueStartSecs3 = (x - getTime.currentTime)
	elif y == (4):
		global queueStartSecs4
		queueStartSecs4 = (x - getTime.currentTime)
	elif y == (5):
		global queueStartSecs5
		queueStartSecs5 = (x - getTime.currentTime)

extractQueue()

calculateQueueTime(queueTime1, 1)
calculateQueueTime(queueTime2, 2)
calculateQueueTime(queueTime3, 3)
calculateQueueTime(queueTime4, 4)
calculateQueueTime(queueTime5, 5)