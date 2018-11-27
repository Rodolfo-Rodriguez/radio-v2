#!/usr/bin/python2

# This Python file uses the following encoding: utf-8

from app import app

HOST = '0.0.0.0'
PORT = 8080
#DEBUG = False 
DEBUG = True 

if __name__ == "__main__":
    app.run(host=HOST,port=PORT,debug=DEBUG)
