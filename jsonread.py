#!/usr/bin/env python3
import os
import json
from time import sleep

def clearscreen():
	print ("\n" * 100)

clearscreen()


def importjson():
	radio = json.loads(open('test.json').read())
	global data

	with open('test.json') as data_file:
		data = json.load(data_file)

def extractjson():
	global djname
	djname = data['main']['dj']['djname']

	global djimage
	djimage = data['main']['dj']['djimage']

	global djdescription
	djdescription = data['main']['dj']['djtext']

	global isafkstream
	isafkstream = data['main']['isafkstream']

	global threadurl
	threadurl = data['main']['thread']

	global listeners
	listeners = data['main']['listeners']

	global songtitle
	songtitle = data['main']['np']

	global isafkstreamstr
	if isafkstream == True:
		isafkstreamstr = "AFK Stream"
	else:
		isafkstreamstr = ""

clearscreen()