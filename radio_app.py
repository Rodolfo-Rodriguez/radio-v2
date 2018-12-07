#!/usr/bin/python2

# This Python file uses the following encoding: utf-8

import sys
from app import app

list_argv = sys.argv
num_argv = len(list_argv)

if num_argv < 2:	 
	debug_mode = False 
else:
	debug_mode = sys.argv[1]

HOST = '0.0.0.0'
PORT = 8080

if __name__ == "__main__":
    app.run(host=HOST,port=PORT,debug=debug_mode)
