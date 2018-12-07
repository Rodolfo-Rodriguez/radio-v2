#!/usr/bin/python

import sys, os

base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(base_path)

from app import db_manager

db_manager.export_csv_data()
