#!/usr/bin/env python3
import os
import jsonread
from time import sleep

#play
def playRadio():
	songLengthSeconds2 = jsonread.endTime - jsonread.startTime
	os.system("mpv -terminal=no --no-config https://relay0.r-a-d.io/main.mp3")
	sleep(songLengthSeconds2)