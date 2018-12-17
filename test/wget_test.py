#!/usr/bin/python2

import wget
import os

import subprocess

url = 'https://audios.oceanofm.com/programas/DeArribaunRayo/18-12-11ernestoelbello.mp3'
file = 'erneto.mp3'

def down_progess(process):

	return 100


process = subprocess.Popen(['wget', url, '-O', file], stderr=subprocess.PIPE)

started = False
for line in process.stderr:
	line = line.decode("utf-8", "replace")
	if started:
		if '%' in line:
			out_list = line.split('%')
			parameter = out_list[0].split(' ')[-1]
			print(parameter)
	elif line == os.linesep:
		started = True