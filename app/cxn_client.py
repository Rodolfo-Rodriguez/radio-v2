import requests 
import xml.etree.cElementTree as ET

# source-type
# 0 - custom url
# 1 - internet radio
# 3 - internal file

cxn_command_data = {
  'VOL_UP':'1010',
  'VOL_DOWN':'1011',
  'POWER_ON':'106e',
  'POWER_OFF':'106f'
}

################################################################################################################################################################
# CXN Client
################################################################################################################################################################

class CXNClient:
  server_name = ''
  server_port = ''
  server_id = ''

  def __init__(self, name='cxn', port='8050', cxn_id='9ffd0730-00fb-455b-aa2f-8fc8df0c268f'):
    self.server_name = name
    self.server_port = port
    self.server_id = cxn_id
    self.playback_details = {}

  def update_server(self, name, port, cxn_id):
    self.server_name = name
    self.server_port = port
    self.server_id = cxn_id
    self.playback_details = self.get_playback_details()

  def update_playback_details(self):
    self.playback_details = self.get_playback_details()

################################################################################################################################################################
# Player
################################################################################################################################################################

  # --> Power CXN and Amp
  def power(self):
    power_state = self.get_power_state()
    if power_state == 'ON':
      self.send_command('POWER_OFF')
    else:
      self.send_command('POWER_ON')
      
    self.press_remote_key('POWER','SHORT')

  def vol_up(self):
    self.send_command('VOL_UP')

  def vol_down(self):
    self.send_command('VOL_DOWN')

  def vol_mute(self):
    self.press_remote_key('MUTE','SHORT')

  def play_preset(self, preset):
    if (preset > 0) and (preset < 21):
      self.play_preset(radio.preset)

  def play_pause(self):
    self.press_remote_key('PLAY_PAUSE','SHORT')
          
  def play(self):
    self.press_remote_key('PLAY_PAUSE','SHORT')

  def stop(self):
    self.press_remote_key('STOP','SHORT')

  def pause(self):
    self.press_remote_key('PLAY_PAUSE','SHORT')

  def next(self):
    self.press_remote_key('SKIP_NEXT','SHORT')

  def previous(self):
    self.press_remote_key('SKIP_PREVIOUS','SHORT')

################################################################################################################################################################
# CXN Status
################################################################################################################################################################

  def find_xml_text(self, root, xml_tag, def_value=''):

    tag_info = root.findall(xml_tag)
    if tag_info:
      return tag_info[0].text
    else:
      return def_value

  #--> Get Playack Details
  def get_playback_details(self):

    soap_endpoint = 'RecivaRadio'
    soap_command = 'GetPlaybackDetails'
    soap_action = '"urn:UuVol-com:service:UuVolControl:5#GetPlaybackDetails"'

    xml_body = """<u:GetPlaybackDetails xmlns:u="urn:UuVol-com:service:UuVolControl:5">
      <NavigatorId>1f7b553f-0934-4d56-9f42-245d86307af9</NavigatorId>
    </u:GetPlaybackDetails>
    """

    response = self.post(soap_endpoint, soap_action, xml_body)

    root = ET.fromstring(response)
    root = ET.fromstring(root[0][0][0].text)
    
    details = {}

    details['state'] = self.find_xml_text(root[0],'state')

    # --> Format Info
    format_info = root[0].findall('format')
    if format_info:
      format_attrib = format_info[0].attrib
      details['codec'] = format_attrib['codec']
      details['bit-rate'] = int(float(format_attrib['bit-rate']) / 1000)
      details['sample-rate'] = int(float(format_attrib['sample-rate']) / 1000)
      details['bit-depth'] = format_attrib['bit-depth']

    # --> Playlist Info
    playlist_info = root[0].findall('playlist-entry')
    if playlist_info:
      playlist = playlist_info[0]     
      details['pl_title'] = self.find_xml_text(playlist,'title')
      details['pl_artist'] = self.find_xml_text(playlist,'artist')
      details['pl_album'] = self.find_xml_text(playlist,'album')

    # --> Stream Info
    stream_info = root[0].findall('stream')
    if stream_info:
      stream = stream_info[0]
      details['source-name'] = self.find_xml_text(stream,'source-name')
      details['source-type'] = self.find_xml_text(stream,'source-type')
      details['url'] = self.find_xml_text(stream,'url')
      details['title'] = self.find_xml_text(stream,'title')
      details['album-art-url'] = self.find_xml_text(stream,'album-art-url','/static/images/radios/unknown.png')

    return details

  #--> Get Power State
  def get_power_state(self):

    soap_endpoint = 'RecivaRadio'
    soap_action = '"urn:UuVol-com:service:UuVolControl:5#GetPowerState"'

    xml_body = """<u:GetPowerState xmlns:u="urn:UuVol-com:service:UuVolControl:5"></u:GetPowerState>"""

    response = self.post(soap_endpoint, soap_action, xml_body)

    root = ET.fromstring(response)

    state = root[0][0][0].text  

    return state

################################################################################################################################################################
# CXN Control
################################################################################################################################################################

  #--> Post to CXN
  def post(self, soap_endpoint, soap_action, xml_body):

    headers = { 
                "Content-Type" : "text/xml", 
                "User-Agent" : "CambridgeConnect/3.2.1 (iOS) UPnP/1.0 DLNADOC/1.50 Platinum/1.0.4.11"
              }
    headers['SOAPAction'] = soap_action

    url = 'http://{}:{}/{}/{}/invoke'.format(self.server_name, self.server_port, self.server_id, soap_endpoint)

    xml = """
    <?xml vesion="1.0" encoding="UTF-8"?>
      <s:Envelope 
        s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" 
        xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
      <s:Body>{}</s:Body>
    </s:Envelope>
    """.format(xml_body)

    response = requests.post(url, data=xml, headers=headers)

    return response.content.decode('utf-8')

  #--> Press Remote Key
  def press_remote_key(self, key, duration):

    soap_endpoint = 'RecivaSimpleRemote'
    soap_action = '"urn:UuVol-com:service:UuVolSimpleRemote:1#KeyPressed"'

    xml_body = """
    <u:KeyPressed xmlns:u="urn:UuVol-com:service:UuVolSimpleRemote:1">
      <Key>{}</Key>
      <Duration>{}</Duration>
    </u:KeyPressed>   
    """.format(key, duration)

    response = self.post(soap_endpoint, soap_action, xml_body)

  #--> Play Preset
  def play_preset(self, preset_id):
    
    soap_endpoint = 'RecivaRadio'
    soap_action = '"urn:UuVol-com:service:UuVolControl:5#PlayPreset"'

    xml_body = """
    <u:PlayPreset xmlns:u="urn:UuVol-com:service:UuVolControl:5">
      <NewPresetNumberValue>{}</NewPresetNumberValue>
    </u:PlayPreset>   
    """.format(preset_id)

    response = self.post(soap_endpoint, soap_action, xml_body)

  #--> Play Radio ID
  def play_radio(self, radio_id):
    
    soap_endpoint = 'RecivaRadio'
    soap_action = '"urn:UuVol-com:service:UuVolControl:5#SetStationId"'

    xml_body = """
    <u:SetStationId xmlns:u="urn:UuVol-com:service:UuVolControl:5">
      <NewStationIdValue>{}</NewStationIdValue>
    </u:SetStationId>   
    """.format(radio_id)

    response = self.post(soap_endpoint, soap_action, xml_body)


  #--> Send Command
  def send_command(self, command):

    command_code = '1072'
    soap_endpoint = 'StreamMagic6'
    soap_action = '"urn:UuVol-com:service:StreamMagic6:1#SendCommand"'

    xml_body = """
    <u:SendCommand xmlns:u="urn:UuVol-com:service:StreamMagic6:1">
      <Command>{}</Command>
      <Data>{}</Data>
    </u:SendCommand>   
    """.format(command_code, cxn_command_data[command])

    response = self.post(soap_endpoint, soap_action, xml_body)


################################################################################################################################################################
# Presets
################################################################################################################################################################

  #--> Delete Preset
  def delete_preset(self, preset_id):
    
    soap_endpoint = 'RecivaRadio'
    soap_action = '"urn:UuVol-com:service:UuVolControl:5#DeletePreset"'

    xml_body = """
    <u:DeletePreset xmlns:u="urn:UuVol-com:service:UuVolControl:5">
      <PresetNumber>{}</PresetNumber>
    </u:PlayPreset>
    """.format(preset_id)

    response = self.post(soap_endpoint, soap_action, xml_body)


  #--> Set Preset
  def set_preset(self, preset_id, station_id):
    
    soap_endpoint = 'RecivaRadio'
    soap_action = '"urn:UuVol-com:service:UuVolControl:5#SetPreset"'

    xml_body = """
    <u:SetPreset xmlns:u="urn:UuVol-com:service:UuVolControl:5">
      <NewPresetNumberValue>{}</NewPresetNumberValue>
      <NewPresetStationIdValue>{}</NewPresetStationIdValue>
      <NewPresetMenuIdValue>-5</NewPresetMenuIdValue>
    </u:SetPreset>
    """.format(preset_id, station_id)

    response = self.post(soap_endpoint, soap_action, xml_body)

  #--> Get Preset List
  def get_preset_list(self):
    
    soap_endpoint = 'RecivaRadio'
    soap_action = '"urn:UuVol-com:service:UuVolControl:5#GetPresetList"'

    xml_body = """
    <u:GetPresetList xmlns:u="urn:UuVol-com:service:UuVolControl:5">
      <Start>1</Start>
      <End>20</End>
    </u:GetPresetList>
    """

    response = self.post(soap_endpoint, soap_action, xml_body)

    root = ET.fromstring(response)
    root = ET.fromstring(root[0][0][0].text)

    preset_list = {}
    for preset in root.iter('preset'):
      preset_list[preset.attrib['id']] = self.find_xml_text(preset,'title')

    return preset_list

################################################################################################################################################################
# Search
################################################################################################################################################################

  def search_radio(self, name, location):

    soap_endpoint = 'SMSearch'
    soap_action = '"urn:UuVol-com:service:SMSearch:1#Search"'

    xml_body = """
    <u:Search xmlns:u="urn:UuVol-com:service:SMSearch:1">
      <NameFilter>{}</NameFilter>
      <CodecFilter>-1</CodecFilter>
      <LocationIDFilter>{}</LocationIDFilter>
      <GenreIDFilter>-1</GenreIDFilter>
      <MinBitrateFilter>0</MinBitrateFilter>
    </u:Search>
    """.format(name, location)

    response = self.post(soap_endpoint, soap_action, xml_body)

    root = ET.fromstring(response)
    root = ET.fromstring(root[0][0][0].text)

    radio_list = {}
    for station in root.iter('station'):
      radio_list[station.attrib['id']] = station.text

    return radio_list

  def locations(self):

    soap_endpoint = 'SMSearch'
    soap_action = '"urn:UuVol-com:service:SMSearch:1#GetLocationList"'

    xml_body = """
    <u:GetLocationList xmlns:u="urn:UuVol-com:service:SMSearch:1"></u:GetLocationList>
    """

    response = self.post(soap_endpoint, soap_action, xml_body)

    root = ET.fromstring(response)
    root = ET.fromstring(root[0][0][0].text)

    location_list = {}
    for station in root.iter('location'):
      location_list[station.attrib['id']] = station.text

    return location_list

  def list_radios_in_location(self, location_id):

    soap_endpoint = 'SMSearch'
    soap_action = '"urn:UuVol-com:service:SMSearch:1#Search"'

    xml_body = """
    <u:Search xmlns:u="urn:UuVol-com:service:SMSearch:1">
      <NameFilter></NameFilter>
      <CodecFilter>-1</CodecFilter>
      <LocationIDFilter>{}</LocationIDFilter>
      <GenreIDFilter>-1</GenreIDFilter>
      <MinBitrateFilter>0</MinBitrateFilter>
    </u:Search>
    """.format(location_id)

    response = self.post(soap_endpoint, soap_action, xml_body)

    root = ET.fromstring(response)
    root = ET.fromstring(root[0][0][0].text)

    radio_list = {}
    for station in root.iter('station'):
      radio_list[station.attrib['id']] = station.text

    return radio_list

  def genre_list(self):

    soap_endpoint = 'SMSearch'
    soap_action = '"urn:UuVol-com:service:SMSearch:1#GetGenreList"'

    xml_body = """
    <u:GetGenreList xmlns:u="urn:UuVol-com:service:SMSearch:1"></u:GetGenreList>
    """

    response = self.post(soap_endpoint, soap_action, xml_body)

    root = ET.fromstring(response)
    root = ET.fromstring(root[0][0][0].text)

    genre_list = {}
    for station in root.iter('genre'):
      genre_list[station.attrib['id']] = station.text

    return genre_list


  def list_radios_in_genre(self, genre_id):

    soap_endpoint = 'SMSearch'
    soap_action = '"urn:UuVol-com:service:SMSearch:1#Search"'

    xml_body = """
    <u:Search xmlns:u="urn:UuVol-com:service:SMSearch:1">
      <NameFilter></NameFilter>
      <CodecFilter>-1</CodecFilter>
      <LocationIDFilter>-1</LocationIDFilter>
      <GenreIDFilter>{}</GenreIDFilter>
      <MinBitrateFilter>0</MinBitrateFilter>
    </u:Search>
    """.format(genre_id)

    response = self.post(soap_endpoint, soap_action, xml_body)

    root = ET.fromstring(response)
    root = ET.fromstring(root[0][0][0].text)

    radio_list = {}
    for station in root.iter('station'):
      radio_list[station.attrib['id']] = station.text

    return radio_list

