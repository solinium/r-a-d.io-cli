#!/usr/bin/env python3
import sys
#import jsonread
import webbrowser
import subprocess

threadUrl = ("https://8ch.net/a/res/686749.html")
djName = ("dank")

def open():
	url = threadUrl
	if sys.platform == 'darwin':	#osx
		subprocess.Popen(['open', url])
	else:
		webbrowser.get('firefox').open(url)

if __name__ == "__main__":
	open()