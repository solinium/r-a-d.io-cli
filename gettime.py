#!/usr/bin/env python3
from requests import get

def start():
	apiraw = get(url='https://r-a-d.io/api', headers={'User-agent': 'Mozilla/5.0'})
	global api
	api = apiraw.json()
	global currentTime
	currentTime = api['main']['current']