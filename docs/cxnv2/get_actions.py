#!/usr/bin/python2

import sys, os
import xml.etree.ElementTree as ET

if len(sys.argv) < 2:
  print '[ERROR] Uso: {} <xml_file>'.format(sys.argv[0])
  sys.exit(2)

xml_file = sys.argv[1]

tree = ET.parse(xml_file)
root = tree.getroot()

action_list = root[2]

for action in action_list:
 	name = action[0] 
 	print name.text