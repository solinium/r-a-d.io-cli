#!/usr/bin/env python3
#import thread
import jsonread
import songtime

def start():
	jsonread.importJson()

	jsonread.extractJson()

	songtime.timerFormat()

if __name__ == "__main__":
	start()