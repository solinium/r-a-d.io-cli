#!/usr/bin/env python3
import json
from requests import get

def importAPI():
	global api
	apiraw = get(url='https://r-a-d.io/api', headers={'User-agent': 'Mozilla/5.0'})
	api = apiraw.json()

def extractQueue():
	global currentTime
	currentTime = api['main']['current']
	
	global queueTitle1
	queueTitle1 = api['main']['queue']['0']['meta']

	global queueTime1
	queueTime1 = api['main']['queue']['0']['timestamp']

	global queueTitle2
	queueTitle2 = api['main']['queue']['1']['meta']

	global queueTime2
	queueTime2= api['main']['queue']['1']['timestamp']

	global queueTitle3
	queueTitle3 = api['main']['queue']['2']['meta']

	global queueTime3
	queueTime1 = api['main']['queue']['2']['timestamp']

	global queueTitle4
	queueTitle4 = api['main']['queue']['3']['meta']

	global queueTime4
	queueTime1 = api['main']['queue']['3']['timestamp']

	global queueTitle5
	queueTitle4 = api['main']['queue']['4']['meta']

	global queueTime5
	queueTime1 = api['main']['queue']['4']['timestamp']

def calculateQueueTime(x, y):
	if y == (1):
		global queueStartSecs1
		queueStartSecs1 = (x - currentTime)
	elif y == (2):
		global queueStartSecs2
		queueStartSecs2 = (x - currentTime)
	elif y == (3):
		global queueStartSecs3
		queueStartSecs3 = (x - currentTime)
	elif y == (4):
		global queueStartSecs4
		queueStartSecs4 = (x - currentTime)
	elif y == (5):
		global queueStartSecs5
		queueStartSecs5 = (x - currentTime)


importAPI()
extractQueue()

calculateQueueTime(queueTime1, 1)
calculateQueueTime(queueTime2, 2)
calculateQueueTime(queueTime3, 3)
calculateQueueTime(queueTime4, 4)
calculateQueueTime(queueTime5, 5)