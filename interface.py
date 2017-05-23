#!/usr/bin/env python3
import curses
import jsonread

#48 rows, 190 columns on f11 idle

def clearScreen():
	print ("\n" * 200)

def cursesfunctions():
	global clearcurses
	def clearcurses():
		mainwindow.clear()

	global endcurses
	def endcurses():
		curses.nocbreak()
		mainwindow.keypad(False)
		curses.echo()
		curses.endwin()

def maincurses():
	clearScreen()

	#init curses
	mainwindow = curses.initscr()

	#turn off screen echoing of keys
	curses.noecho()

	#don't require enter to be pressed for input
	curses.cbreak()

	#parse special keys
	mainwindow.keypad(True)

	mainwindow.addstr(12, 25, jsonread.djname)

	mainwindow.refresh()