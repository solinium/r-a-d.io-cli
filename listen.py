#!/usr/bin/env python3
import mpv

def play():
	global player
	player = mpv.MPV(ytdl=False)
	player.play('https://relay0.r-a-d.io/main.mp3')

if __name__ == ("__main__"):
	play()