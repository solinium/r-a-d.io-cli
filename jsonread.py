#!/usr/bin/env python
import os
import sys
import json
from pprint import pprint
from time import sleep

def clearscreen():
	print ("\n" * 100)

clearscreen()

radio = json.loads(open('test.json').read())

with open('test.json') as data_file:
	data = json.load(data_file)

djname = data['main']['dj']['djname']

djimage = data['main']['dj']['djimage']

djdescription = data['main']['dj']['djtext']

isafkstream = data['main']['isafkstream']

threadurl = data['main']['thread']

listeners = data['main']['listeners']

songtitle = data['main']['np']


if isafkstream == True:
	isafkstreamstr = "AFK Stream"
else:
	isafkstreamstr = ""

os.system("mpv https://relay0.r-a-d.io/main.mp3")
clearscreen()