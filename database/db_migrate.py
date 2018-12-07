#!/usr/bin/python

import sys, os

base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(base_path)

from app import manager

if __name__ == '__main__':
    manager.run()
