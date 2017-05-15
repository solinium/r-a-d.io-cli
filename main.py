#!/usr/bin/env python3`
import jsonread
import interface

global start
def start():
	jsonread.importjson()

	jsonread.extractjson()

	interface.cursesfunctions()

	interface.maincurses()

if __name__ == "__main__":
	start()