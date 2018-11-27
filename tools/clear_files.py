#!/usr/bin/python2

import os
import sys

if len(sys.argv) < 2:
  print '[ERROR] Uso: ' + sys.argv[0] + ' <root-dir>'
  sys.exit(2)

root_dir = sys.argv[1]

del_files = []

for root, dirs, files in os.walk(root_dir):
  for filename in files:
    if filename.startswith('._') or filename.startswith('.DS_Store'):
      del_files.append(os.path.join(root, filename))

print "----------------------------------------------------------------------------------"
print "Deleting"
print "----------------------------------------------------------------------------------"

for file in del_files:
  print file
  os.remove(file)

print "----------------------------------------------------------------------------------"
