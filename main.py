#!/usr/bin/env python3
import mpv
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
	
	#mpv.playRadio()

def clearScreen():
	print ("\n" * 200)

clearScreen()

if __name__ == "__main__":
	start()