#!/usr/bin/python2

import requests	
import xml.etree.cElementTree as ET

cnx_server = "192.168.1.4"
cnx_port = "8050"
cnx_id = "9ffd0730-00fb-455b-aa2f-8fc8df0c268f"
url_endpoint = 'RecivaRadio'

URL = 'http://{}:{}/{}/{}/invoke'.format(cnx_server, cnx_port, cnx_id, url_endpoint)

SOAPAction = '"urn:UuVol-com:service:UuVolControl:5#GetPowerState"'

xml_body = """<u:GetPowerState xmlns:u="urn:UuVol-com:service:UuVolControl:5"></u:GetPowerState>"""

xml = """
<?xml vesion="1.0" encoding="UTF-8"?>
<s:Envelope 
	s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" 
	xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
	<s:Body>{}</s:Body>
</s:Envelope>
""".format(xml_body)

headers = { 
			"Content-Type" : "text/xml", 
			"SOAPAction" : SOAPAction,
			"User-Agent" : "CambridgeConnect/3.2.1 (iOS) UPnP/1.0 DLNADOC/1.50 Platinum/1.0.4.11",
			}

response = requests.post(URL, data=xml, headers=headers)

root = ET.fromstring(response.content.decode('UTF-8'))

body = root[0][0][0]


print body.tag
print body.text



# print response.content.decode('UTF-8')

# for child in root:
# 	print child.tag, child.attrib

# ps = root.findall('RetPowerStateValue')
# print ps


