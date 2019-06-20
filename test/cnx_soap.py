#!/usr/bin/python2

import requests	

cnx_server = "192.168.1.4"
cnx_port = "8050"
cnx_id = "9ffd0730-00fb-455b-aa2f-8fc8df0c268f"
url_endpoint = '/RecivaSimpleRemote/invoke'

URL = 'http://' + cnx_server + ':' + cnx_port + '/' + cnx_id + url_endpoint

SOAPAction = '"urn:UuVol-com:service:UuVolSimpleRemote:1#KeyPressed"'

xml_body = """
<u:KeyPressed xmlns:u="urn:UuVol-com:service:UuVolSimpleRemote:1">
	<Key>PLAY_PAUSE</Key>
	<Duration>SHORT</Duration>
</u:KeyPressed>
"""

xml = """
<?xml vesion="1.0" encoding="UTF-8"?>
<s:Envelope 
	s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" 
	xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
	<s:Body>
""" + xml_body + """
	</s:Body>
</s:Envelope>
"""

headers = { "Content-Type" : "text/xml", 
			"SOAPAction" : SOAPAction,
			"User-Agent" : "CambridgeConnect/3.2.1 (iOS) UPnP/1.0 DLNADOC/1.50 Platinum/1.0.4.11",
			"Host" : cnx_server }

response = requests.post(URL, data=xml, headers=headers)

print response.status_code
print response.text

