#!/usr/bin/python2

import sys, os
import xml.etree.ElementTree as ET

if len(sys.argv) < 3:
  print '[ERROR] Uso: {} <xml_file> <xml_command>'.format(sys.argv[0])
  sys.exit(2)

xml_file = sys.argv[1]
xml_command = sys.argv[2]

tree = ET.parse(xml_file)
root = tree.getroot()

action_list = root[2]

for action in action_list:
	name = action[0].text
	if xml_command in name:
		print '-----> {}'.format(name)
		argument_list = action[1]
		for argument in argument_list:
			print '* {} [ {} ] [ {} ]'.format(argument[0].text, argument[1].text, argument[2].text)
