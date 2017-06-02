#!/usr/bin/env python3
import sys
import jsonread
import webbrowser
import subprocess


def open():
	if jsonread.threadUp:
		if sys.platform == 'darwin':	#osx
			subprocess.Popen(['open', jsonread.threadUrl])
		else:
			webbrowser.get('firefox').open(jsonread.threadUrl)
	else:
		print()
		print("Sorry, thread is not up.")
		print()

if __name__ == "__main__":
	open()