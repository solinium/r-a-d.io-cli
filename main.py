#!/usr/bin/env python3
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

	#thread.open()

	#mpv.playRadio()

def clearScreen():
	print ("\033[2J" * 10)

clearScreen()

if __name__ == "__main__":
	start()