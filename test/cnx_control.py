#!/usr/bin/python2

import sys, os

base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

sys.path.append(base_path)

from app.cxn_client import CXNClient 

cxn_server = "192.168.1.4"
cxn_port = "8050"
cxn_id = "9ffd0730-00fb-455b-aa2f-8fc8df0c268f"

cxn_client = CXNClient(cxn_server, cxn_port, cxn_id)

res = cxn_client.get_preset_list()

print res

