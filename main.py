#!/usr/bin/env python
import json 
from time import sleep

def clearscreen():
	print ("\n" * 100)

clearscreen()

radio = json.loads(open('test.json').read())

print(radio)
sleep(10)
clearscreen()
print(radio["dj"])