#!/usr/bin/env python3
import os
#import mpv
#import thread
import jsonread
import songtime
#import interface

global start
def start():
	jsonread.importJson()

	jsonread.extractJson()

	#interface.cursesfunctions()

	#interface.maincurses()

	songtime.timerFormat()

	#thread.init()

	#thread.open()

	os.system("python3 /home/canary/Projects/Programming/Python/r-a-d.io\ client/thread.py")

	#mpv.playRadio()

def clearScreen():
	print ("\n" * 200)

clearScreen()

if __name__ == "__main__":
	start()