var aTexts = {
  OK: "OK",
  Cancel: "Cancel",
  Yes: "Yes",
  No: "No",
  Skip: "Skip",
  Continue: "Continue",
  // xgettext: Save settings
  Save: "Save",
  // xgettext: Title for error box
  Error: "Error",
  PleaseWait: "Please wait",
  Loading: "Loading",
  // xgettext: Webpage loading done
  Done: "Done",
  // xgettext: Title for information box, informs the webpage has been disconnected
  Disconnected: "Disconnected",
  // xgettext: Describes why the webpage has been disconnected
  UnitTurnedOff: "The unit has been turned off",
  // xgettext: Describes why the webpage has been disconnected
  ConnectionLost: "Connection with the unit has been lost",
  TryAndReloadPage: "You can try and reload the page",
  // xgettext: Button title for webpage reload
  Reload: "Reload",
  // xgettext: Webpage reloading message
  Reloading: "Reloading...",
  // xgettext: No signal on digital input
  NoSignal: "No signal",
  status: {
    // xgettext: Name of the section with current state of the unit
    CurrentStatus: "Current status",
    // xgettext: Indicates wired, wireless or AP connection
    ConnectionMode: "Connection mode:",
    // xgettext: Name of the Wi-Fi network the unit is connected to
    NetworkName: "Network name",
    // xgettext: Signal strength of Wi-Fi connection
    SignalStrength: "Signal strength:",
    IPAddress: "IP Address",
    IPv6Address: "IPv6 Address",
    // xgettext: Current source
    Source: "Source:",
  },
  product: {
    // xgettext: Name of the section to set friendly name of the unit
    RenameYourUnit: "Rename your unit",
    // xgettext: Hint for product name input field
    ProductName: "Unit name",
    // xgettext: Product name not entered
    NameNotEntered: "No name entered",
    // xgettext: Leave PRODUCT, as it will be replaced by the product name by the software
    CustomiseTheName: "Customise the name of your PRODUCT",
    // xgettext: Describes the use of unit friendly name. Leave GOOGLE_CAST, as it will be replaced by chromecast name by the software
    DescriptionAirplaySpotifyCast: "This name will appear in the AirPlay drop-down list, Spotify Connect device list and GOOGLE_CAST device list.",
    // xgettext: Describes the use of unit friendly name
    DescriptionAirplaySpotify: "This name will appear in the AirPlay drop-down list and Spotify Connect device list.",
    // xgettext: Describes the use of unit friendly name
    DescriptionSpotify: "This name will appear in the Spotify Connect device list.",
  },
  network: {
    // xgettext: Name of network settings section
    NetworkSettings: "Network settings",
    // xgettext: Add custom wireless network
    AddNetwork: "Add network",
    // xgettext: Manually configure network settings
    ConfigureManually: "Configure manually",
    // xgettext: Whether to use static IP address configuration or a DHCP server to get IP addresses.
    StaticIPConfig: "Static IP address configuration",
    // xgettext: Refresh list of Wi-Fi networks
    Refresh: "Refresh",
    // xgettext: Wired (Ethernet) connection
    Wired: "Wired",
    // xgettext: Wi-Fi connection - no need to translate Wi-Fi
    Wireless: "Wi-Fi",
    // xgettext: Host Access Point connection
    AccessPoint: "Access point",
    // xgettext: Select Wi-Fi network
    SelectNetwork: "Select Network",
    // xgettext: Hint of Wi-Fi network drop-down list
    Network: "Network",
    // xgettext: No Wi-Fi network is selected
    NetworkNotSelected: "Network not selected",
    // xgettext: No Wi-Fi networks available
    NoNetworksAvailable: "No networks available",
    // xgettext: Name of Wi-Fi network
    NetworkName: "Network name",
    // xgettext: Wi-Fi network name not entered
    NetworkNameNotEntered: "Network name not entered",
    // xgettext: Select encryption for Wi-Fi network
    SelectEncryption: "Select encryption",
    // xgettext: Encryption for Wi-Fi network
    Encryption: "Encryption",
    // xgettext: Encryption for Wi-Fi network is not selected
    EncryptionNotSelected: "Encryption not selected",
    // xgettext: Enter password for wireless network
    Passphrase: "Wi-Fi Passphrase",
    // xgettext: Title of a check-box to show Wi-Fi password
    ShowPassphrase: "Show Wi-Fi passphrase",
    // xgettext: No Wi-Fi password entered
    NoPassphraseEntered: "No Wi-Fi passphrase",
    // xgettext: Unit will try and use previous stored password to connect to Wi-Fi network
    NoPassphraseInfo: "Unit will use previous passphrase to connect",
    // xgettext: Signal strength of Wi-Fi network the unit is connected to
    Signal: "Signal",
    // xgettext: Static IP address
    IPAddress: "IP address",
    // xgettext: Invalid network (IP) address entered
    InvalidAddressEntered: "Invalid address",
    // xgettext: Subnet mask when using a static IP address
    SubnetMask: "Subnet mask",
    // xgettext: Default gateway when using a static IP address
    DefaultGateway: "Default gateway",
    // xgettext: Primary DNS server when using a static IP address
    PrimaryDNSServer: "Primary DNS server",
    // xgettext: Secondary DNS server when using a static IP address
    SecondaryDNSServer: "Secondary DNS server",
    // xgettext: Leave PRODUCT, as it will be replaced by the product name by the software
    SetupYourProduct: "Set-up your PRODUCT to join your network. Using the drop-down box, select the network to which the PRODUCT should connect.",
  },
  power: {
    // xgettext: Name of power settings section
    PowerSettings: "Power settings",
    // xgettext: Power standby mode
    StandbyMode: "Standby Mode",
    // xgettext: Eco (deep) standby mode
    ECOMode: "ECO Mode",
    // xgettext: Standby mode with network active
    NetworkStandby: "Network Standby",
    // xgettext: Automatic power-down settings
    AutoPowerDown: "Automatic Power-down",
    // xgettext: Automatic power-down turned off
    AutoPowerDownOff: "Off",
  },
  volume: {
    // xgettext: Name of volume settings section
    VolumeSettings: "Volume settings",
    // xgettext: Describes the volume limit setting
    VolumeLimit: "This limits the maximum volume that other applications can attain",
    // xgettext: Describes to what external controls the volume limit applies
    DescriptionLimit: "When active only the volume control or remote control can set the volume higher than the limit",
    // xgettext: Describes to what external controls the volume limit applies
    DescriptionLimitEdge: "When active only the volume control, remote control or Edge Remote app can set the volume higher than the limit",
  },
  timezone: {
    // xgettext: Name of timezone section
    Timezone: "Timezone",
    // xgettext: Select timezone to use
    SelectTimezone: "Select timezone",
  },
  firmware: {
    // xgettext: Name of firmware section
    Firmware: "Firmware",
    // xgettext: Current version of software pack
    CurrentVersion: "Current version:",
    // xgettext: Current version of MCU software
    MCUVersion: "MCU version:",
    // xgettext: Unit identification
    UnitID: "Unit ID:",
    // xgettext: Allow users to select more frequent firmware updates
    EarlyUpdate: "Early update",
    // xgettext: Describes the action of a check-box on the form
    EarlyDescription: "Tick this box to try out the latest software",
    // xgettext: Update firmware
    Update: "Update",
    // xgettext: Check for new firmware and update if something is available
    Check: "Check and update",
    // xgettext: New software is available for the unit
    NewFirmwareAvailable: "New firmware is available",
    // xgettext: No new software is available for the unit
    NoFirmwareAvailable: "No firmware update available",
    // xgettext: Title for information box, informs firmware update progress
    FirmwareUpdate: "Firmware update",
    // xgettext: Starting software update
    Starting: "Starting...",
    // xgettext: Explanation of Early Updates feature, and what happens with feedback from the forms in the associated mobile app
    EarlyNotification: "Thanks for choosing to try out our latest, pre-release software. If you have problems just un-tick 'Early Update' to go back to the current general-release software. Please do leave feedback using the 'Contact Us' form in the Cambridge Connect app, but for pre-release software, we'll only contact you directly if we need more information.",
  },
  cast: {
    // xgettext: Name of chromecast section
    Cast: "Chromecast built-in",
    // xgettext: Button title for chromecast setup
    Setup: "Setup",
    // xgettext: Displayed when chromecast hasn't yet been configured. No need to translate 'Chromecast built-in'
    NeedSetup: "To start using Chromecast built-in you'll need to set it up first",
    // xgettext: Title for chromecast setup box
    CastSetup: "Chromecast built-in",
    // xgettext: Chromecast Accept button title
    Accept: "Accept",
    // xgettext: Chromecast Decline button title
    Decline: "Decline",
    // xgettext: Google Terms of Service (ToS), leave GOOGLE_PRIVACY and GOOGLE_TERMS, as they will be replaced by the software
    TermsAndConditions: "The <GOOGLE_PRIVACY>Google Privacy Policy</a> describes the information that Google collects during your set-up and use of Chromecast. You can modify your device's Chromecast built-in privacy policy settings, such as whether it sends usage data and crash reports to Google, after you have set up your device by accessing the device settings in this application.<br/><br/>By pressing &quot;Accept&quot; below, you acknowledge that you agree to the <GOOGLE_TERMS>Google Terms of Service</a> and <GOOGLE_PRIVACY>Google Privacy Policy</a>.",
    // xgettext: Hyperlink to an external source (google webpage), also part of google ToS
    TermsOfService: "Google Terms of Service",
    // xgettext: Hyperlink to an external source (google webpage), also part of google ToS
    PrivacyPolicy: "Google Privacy Policy",
    // xgettext: Hyperlink to an external source (google webpage)
    OpenSourceLicenses: "Open-source licences",
    // xgettext: Chromecast version number
    Version: "Chromecast built-in version:",
    // xgettext: Title of a check-box to enable sharing usage data
    ShareUsageData: "Share usage data",
    // xgettext: Hyperlink to an external source (google webpage)
    LearnAboutCastPolicy: "Find out about Chromecast built-in Privacy",
    // xgettext: Hyperlink to an external source (google webpage)
    HowToCast: "Find out how to Cast",
    // xgettext: Hyperlink to an external source (google webpage)
    EnabledApps: "Chromecast enabled apps",
    // xgettext: Hyperlink to an external source (google webpage)
    LearnAboutMultiroom: "Find out about cast groups",
    // xgettext: Title for chromecast tutorial box. No need to translate 'Chromecast built-in'
    CastTutorial: "Chromecast built-in tutorial",
    // xgettext: Chromecast tutorial wording, leave PRODUCT, as it will be replaced by the product name by the software
    TutorialDescription: "Cast your favourite music and radio apps from your phone or tablet to your PRODUCT.",
    // xgettext: Button title for chromecast tutorial
    LearnMore: "Find out more",
    // xgettext: Button title for chromecast tutorial
    NoThanks: "No thanks",
  },
  services: {
    // xgettext: Name of section for configuring Streaming services (e.g. Pandora)
    Services: "Services",
    // xgettext: Link streaming service account to this unit
    Link: "Link",
    // xgettext: Unlink streaming service account from this unit
    Unlink: "Unlink",
    // xgettext: Leave SERVICE, as it will be replaced by the name of the streaming service (e.g. Pandora) by the software
    LinkService: "Link SERVICE service",
    // xgettext: Leave SERVICE, as it will be replaced by the name of the streaming service (e.g. Pandora) by the software
    UnlinkService: "Unlink SERVICE service",
    // xgettext: Enter username for the streaming service account
    EnterUsername: "Username",
    // xgettext: No username for the streaming service account entered
    UsernameNotEntered: "No username",
    // xgettext: Enter password for the streaming service account
    EnterPassword: "Password",
    // xgettext: No password for the streaming service account entered
    PasswordNotEntered: "No password",
    // xgettext: Displayed while the unit is trying to link streaming service account
    Linking: "Linking...",
    // xgettext: Couldn't link streaming service account to unit
    UnableToLink: "Unable to link the service",
    // xgettext: Displayed to confirm unlinking the streaming service
    UnlinkInfo: "You're about to unlink the service",
    // xgettext: Displayed while the unit is trying to unlink streaming service account
    Unlinking: "Unlinking...",
    // xgettext: Couldn't unlink streaming service account from unit
    UnableToUnlink: "Unable to unlink service",
  },
  podcasts: {
    // xgettext: Name of the section with list of podcasts the user has subscribed to
    Podcasts: "Personal podcasts",
    AddNewPodcast: "Add new podcast",
    EnterPodcastName: "Name",
    // xgettext: No podcast name entered
    NameNotEntered: "No name entered",
    EnterPodcastAddress: "URL",
    // xgettext: No URL entered
    AddressNotEntered: "No URL entered",
    // xgettext: Displayed while adding podcast to 'Personal Podcasts' list
    Adding: "Adding...",
    // xgettext: Couldn't add podcast to 'Personal Podcasts' list
    UnableToAdd: "Unable to add podcast",
    // xgettext: Button title for podcast removal
    Remove: "Remove",
    // xgettext: Title for podcast removal confirmation box
    RemovePodcast: "Remove podcast",
    // xgettext: Displayed to confirm removal of the podcast
    RemoveInfo: "You're about to remove the podcast",
    // xgettext: Displayed while removing podcast from 'Personal Podcasts' list
    Removing: "Removing...",
    // xgettext: Couldn't remove podcast from 'Personal Podcasts' list
    UnableToRemove: "Unable to remove podcast",
  },
  presets: {
    // xgettext: Name of the section with presets
    Presets: "Presets",
    AddNewPreset: "Add new preset",
    // xgettext: Title for new preset dialogue box
    NewPreset: "New preset",
    // xgettext: Select position/number to store the preset
    SelectPresetPosition: "Select preset position",
    // xgettext: Hint for preset position drop-down list
    PresetPosition: "Preset position",
    InvalidPresetPositionSelected: "Invalid preset position",
    EnterPresetName: "Name",
    // xgettext: Hint for preset name input field
    PresetName: "Preset name",
    InvalidPresetNameEntered: "No name entered",
    EnterPresetAddress: "URL",
    // xgettext: Hint for preset address input field
    PresetAddress: "URL",
    // xgettext: No URL entered
    InvalidPresetAddressEntered: "No URL entered",
    // xgettext: Button title for preset rename
    Rename: "Rename",
    // xgettext: Title for rename preset dialogue box
    RenamePreset: "Rename preset",
    // xgettext: Button title for preset removal
    Remove: "Remove",
    // xgettext: Title for preset removal confirmation box
    RemovePreset: "Remove preset",
    // xgettext: Displayed to confirm removal of the preset, leave PRESET_ID, as it will be replaced by the software
    RemoveInfo: "Preset PRESET_ID will be removed",
    // xgettext: Button title for preset play
    Play: "Play",
    // xgettext: Button title for preset play when the preset is currently playing
    Playing: "Playing",
  },
  wizard: {
    // xgettext: Title for setup wizard box
    Welcome: "Welcome",
    // xgettext: Leave PRODUCT, as it will be replaced by the product name by the software
    WelcomeDescription: "This wizard will guide you through the basic setup of your PRODUCT:",
    // xgettext: Internet connection setup, displayed as part of setup wizard
    SetupInternet: "Set-up internet connection",
    // xgettext: Title for IP address configuration
    IPAddresses: "IP addresses",
    // xgettext: Firmware update, displayed as part of setup wizard
    FirmwareUpdate: "Firmware update",
    // xgettext: Setup of the rest (product name, standby mode, chromecast), displayed as part of setup wizard
    SetupRest: "Set-up the rest",
    // xgettext: Title for setting friendly name
    RenameYourUnit: "Rename your unit",
    // xgettext: Leave PRODUCT, as it will be replaced by the product name by the software
    RenameDescription: "Customise the name of your PRODUCT",
    // xgettext: Title of a check-box to enable network standby mode
    NetworkStandby: "Network standby",
    // xgettext: Displayed when applying settings of setup wizard
    ApplyingSettings: "Applying settings",
    // xgettext: Leave NETWORK, as it will be replaced by the network name by the software
    ConnectToNetwork: "Connect to NETWORK to continue.",
  },
  init: function() {
    var elms = {
      cast: [
        "TermsAndConditions", "LearnAboutCastPolicy",
        "Version",
      ],
      product: [
        "DescriptionAirplaySpotifyCast",
      ],
    };
    for(var key in elms)
      for(var i = 0; i < elms[key].length; i++)
        aTexts[key][elms[key][i]] = aTexts[key][elms[key][i]].replace(/GOOGLE_CAST/g, aTexts.cast.Cast);
  },
};

var log = {
  _enabled: true,
  _fnStack: [],
  _ind: function(text) {
    for(var i = log._fnStack.length; i--; )
      text = "  " + text;
    return text;
  },
  deb: function(text) {
    if(!log._enabled)
      return;
    console.log(log._ind(text));
  },
  fnEntry: function(text) {
    if(!log._enabled)
      return;
    log.deb(text + " ---->");
    log._fnStack.push(text);
  },
  fnExit: function() {
    if(!log._enabled)
      return;
    log.deb("<---- " + log._fnStack.pop());
  },
};

function createHref(url) {
  return "<a href=\"" + url + "\" target=\"_blank\">";
}

function createLink(obj) {
  var txt = "<a";
  if(obj.url)
    txt += " href=\"" + obj.url + "\" target=\"_blank\"";
  if(obj.onclick)
    txt += " onclick=\"" + obj.onclick + "\"";
  txt += ">" + obj.txt + "</a>";
  return txt;
}

function newHTTPRequest() {
  var req = window.XMLHttpRequest
          ? new XMLHttpRequest()
          : new ActiveXObject("Microsoft.XMLHTTP");

  req.sendGet = function(url, params) {
    if(params)
    {
      var i = 0;
      for(var key in params)
      {
        url += (!i++) ? "?" : "&";
        url += key + "=" + encodeURIComponent(params[key]);
      }
    }
    this.open("GET", "/" + url, true);
    this.send();
    return this;
  };

  req.sendPost = function(url, params) {
    this.open("POST", "/" + url, true);
    if(params.headers)
      for(var key in params.headers)
        this.setRequestHeader(key, params.headers[key]);
    this.send(params.body);
  };

  req.onreadystatechange = function() {
    switch(this.readyState)
    {
      case 4:
        if(this.onReadyDone)
          this.onReadyDone(this.status, this.responseText);
        break;
    }
  };

  return req;
}

var WS = function() {
  var priv = {
    handle: null,
    callbacks: {
      onopen: [],
      onclose: [],
      onmessage: [],
    },
  };
  function onopen() {
    log.fnEntry("WS.onopen");
    for(var i = priv.callbacks.onopen.length; i--; )
      priv.callbacks.onopen[i]();
    log.fnExit();
  }
  function onclose(event) {
    log.fnEntry("WS.onclose "
          + "(code: " + event.code + ", "
          + "reason: '" + event.reason + "')");
    for(var i = priv.callbacks.onclose.length; i--; )
      priv.callbacks.onclose[i](event.code, event.reason);
    priv.handle = null;
    log.fnExit();
  }
  function onmessage(message) {
    log.fnEntry("WS.onmessage "
          + "(length: " + message.data.length + " bytes)");
    for(var i = priv.callbacks.onmessage.length; i--; )
      priv.callbacks.onmessage[i](message.data);
    log.fnExit();
  }
  function connectCallback(dest, callback) {
    priv.callbacks[dest].push(callback);
  }
  function disconnectCallback(dest, callback) {
    for(var i = priv.callbacks[dest].length; i--; )
      if(priv.callbacks[dest][i] == callback) {
        priv.callbacks[dest].splice(i, 1);
        break;
      }
  }
  return {
    open: function(address) {
      log.fnEntry("WS.open");
      if(!priv.handle)
      {
        var proto = (window.location.protocol === "https:")
                  ? "wss" : "ws";
        address = proto + "://" + address;
        priv.handle = new WebSocket(address);
        log.deb("Address: '" + address + "'");
        priv.handle.onclose = onclose;
        priv.handle.onopen = onopen;
        priv.handle.onmessage = onmessage;
      }
      log.fnExit();
    },
    close: function() {
      log.fnEntry("WS.close");

      if(priv.handle)
        priv.handle.close(1000);

      log.fnExit();
    },
    send: function(message) {
      log.fnEntry("WS.send");
      if(priv.handle)
        priv.handle.send(message);
      log.fnExit();
    },
    connectOpenCallback: function(callback) {
      connectCallback("onopen", callback);
    },
    disconnectOpenCallback: function(callback) {
      disconnectCallback("onopen", callback);
    },
    connectCloseCallback: function(callback) {
      connectCallback("onclose", callback);
    },
    disconnectCloseCallback: function(callback) {
      disconnectCallback("onclose", callback);
    },
    connectMessageCallback: function(callback) {
      connectCallback("onmessage", callback);
    },
    disconnectMessageCallback: function(callback) {
      disconnectCallback("onmessage", callback);
    },
  };
};

var SMoIP = function() {
  var priv = {
    WSHandle: null,
    tagID: 0,
    commands: {
      presets: {
        list: {
          path: "/presets/list",
          params: {
            update: 1,
          },
        },
      },
      system: {
        info: {
          path: "/system/info",
          params: {
            update: 1,
          },
        },
        network: {
          path: "/system/network",
          params: {
            update: 1,
          },
        },
        networkWireless: {
          path: "/system/network/wireless",
          params: {
            update: 1,
          },
        },
        power: {
          path: "/system/power",
          params: {
            update: 1,
          },
        },
        powerSpec: {
          path: "/system/power/spec",
        },
        sources: {
          path: "/system/sources",
          params: {
            update: 1,
          },
        },
        sourcesCast: {
          path: "/system/sources/CAST",
          params: {
            update: 1,
          },
        },
        update: {
          path: "/system/update",
          params: {
            update: 1,
          },
        },
      },
      zone: {
        audio: {
          path: "/zone/audio",
          params: {
            update: 1,
          },
        },
        audioSpec: {
          path: "/zone/audio/spec",
        },
        play_state: {
          path: "/zone/play_state",
          params: {
            zone: "ZONE1",
            update: 1,
          },
        },
      },
    },
    current: {
      system: {
        power: { },
        update: { },
      },
      zone: {
        play_state: { },
      },
    },
    callbacks: { },
    requests: { },
  };
  function send(command) {
    log.fnEntry("SMoIP.send");
    if(priv.WSHandle) {
      var message = JSON.stringify(command);
      log.deb("Message follows:\n" + message);
      priv.WSHandle.send(message);
    }
    log.fnExit();
  }
  function sendCB(callback, command, preNotify) {
    if(!command.params)
      command.params = { };

    var tag = "TAG" + (++priv.tagID);
    command.params.tag = tag;
    priv.requests[tag] = {
      callback: callback,
      preNotify: preNotify,
    };

    send(command);
  }
  function invokeCallback(name, params) {
    if(!priv.callbacks[name])
      return;

    var cb = (priv.callbacks[name].constructor === Array)
           ? priv.callbacks[name]
           : [ priv.callbacks[name] ];

    for(var i = 0; i < cb.length; i++)
      cb[i].apply(this, params);
  }
  function parsePresets(path, params) {
    log.fnEntry("SMoIP.parsePresets");
    if(params && params.data)
    {
      switch(path[2])
      {
        case "list":
          if(params.data.max_presets != null)
            invokeCallback("onPresetsMaxValue", [ params.data.max_presets ]);
          invokeCallback("onPresetsList", [ params.data.presets ]);
          break;
      }
    }
    log.fnExit();
  }
  function parseSystem(path, params) {
    log.fnEntry("SMoIP.parseSystem");
    if(params && params.data)
    {
      switch(path[2])
      {
        case "info":
          switch(path[3])
          {
            case undefined:
              if(params.data.hcv || params.data.model)
                invokeCallback("onInfoModel", [ params.data.model ]);
              if(params.data.name)
                invokeCallback("onInfoName", [ params.data.name ]);
              if(params.data.versions)
                invokeCallback("onInfoVersions", [ params.data.versions ]);
              if(params.data.unit_id)
                invokeCallback("onInfoUnitID", [ params.data.unit_id ]);
              if(params.data.timezone)
                invokeCallback("onInfoTimezone", [ params.data.timezone ]);
              break;
          }
          break;
        case "network":
          switch(path[3])
          {
            case undefined:
              if(params.data.connection)
                invokeCallback("onNetworkConnection", [ params.data.connection ]);
              if(params.data.ip_info)
                invokeCallback("onNetworkIPInfo", [ params.data.ip_info ]);
              break;
            case "wireless":
              invokeCallback("onNetworkWireless", [ params.data ]);
              break;
          }
          break;
        case "power":
          switch(path[3])
          {
            case "spec":
              if(params.data.standby_mode)
                invokeCallback("onStandbyModeValues", [ params.data.standby_mode ]);
              if(params.data.auto_power_down)
                invokeCallback("onStandbyAPDValues", [ params.data.auto_power_down ]);
              break;
            case undefined:
              if(params.data.standby_mode != priv.current.system.power.standby_mode)
              {
                priv.current.system.power.standby_mode = params.data.standby_mode;
                invokeCallback("onStandbyModeChange", [ priv.current.system.power.standby_mode ]);
              }
              if(params.data.auto_power_down != priv.current.system.power.auto_power_down)
              {
                priv.current.system.power.auto_power_down = params.data.auto_power_down;
                invokeCallback("onStandbyAPDChange", [ priv.current.system.power.auto_power_down ]);
              }
              break;
          }
          break;
        case "sources":
          switch(path[3])
          {
            case "CAST":
              invokeCallback("onSourceCast", [ params.data ]);
              break;
            case undefined:
              if(params.data.sources)
                invokeCallback("onSourceValues", [ params.data.sources ]);
              break;
          }
          break;
        case "update":
          if((params.data.early_update != null)
          && (params.data.early_update != priv.current.system.update.early_update))
          {
            priv.current.system.update.early_update = params.data.early_update;
            invokeCallback("onUpdateEarlyChange", [ priv.current.system.update.early_update ]);
          }
          if((params.data.update_available != null)
          && (params.data.update_available != priv.current.system.update.update_available))
          {
            priv.current.system.update.update_available = params.data.update_available;
            invokeCallback("onUpdateAvailableChange", [ priv.current.system.update.update_available ]);
          }
          if(params.data.updating)
          {
            invokeCallback("onUpdateStart", [ ]);
          }
          break;
      }
    }
    log.fnExit();
  }
  function parseZone(path, params) {
    log.fnEntry("SMoIP.parseZone");
    if(params)
    {
      switch(path[2])
      {
        case "audio":
          switch(path[3])
          {
            case "spec":
              if(params.data.volume_limit_percent)
                invokeCallback("onVolumeLimitValues", [ params.data.volume_limit_percent ]);
              break;
            case undefined:
              if(params.data.volume_limit_percent)
                invokeCallback("onVolumeLimitChange", [ params.data.volume_limit_percent ]);
              break;
          }
          break;
        case "play_state":
          var source = null;
          if(params.data && params.data.metadata)
          {
            var metadata = params.data.metadata;
            invokeCallback("onPSMetadataChange", [ metadata ]);
            source = metadata.source;
          }
          if(priv.current.zone.play_state.source != source)
          {
            priv.current.zone.play_state.source = source;
            invokeCallback("onSourceChange", [ source ]);
          }
          break;
      }
    }
    log.fnExit();
  }
  function onWSOpen() {
    log.fnEntry("SMoIP.onWSOpen");

    invokeCallback("onConnectionOpen", [ ]);

    var cmds = [
      // {
      //   cmd: priv.commands.system.info,
      //   msg: "SystemInfo",
      // },
      // {
      //   cmd: priv.commands.system.network,
      //   msg: "NetworkSettings",
      // },
      // {
      //   cmd: priv.commands.system.networkWireless,
      //   msg: "WirelessSettings",
      // },
      // {
      //   cmd: priv.commands.system.powerSpec,
      //   msg: "PowerSpec",
      // },
      // {
      //   cmd: priv.commands.system.power,
      //   msg: "PowerSettings",
      // },
      // {
      //   cmd: priv.commands.system.sources,
      //   msg: "AvailableSources",
      // },
      // {
      //   cmd: priv.commands.system.sourcesCast,
      //   msg: "GoogleCastSettings",
      // },
      // {
      //   cmd: priv.commands.system.update,
      //   msg: "FirmwareUpdates",
      // },
      // {
      //   cmd: priv.commands.zone.audioSpec,
      //   msg: "AudioSpec",
      // },
      // {
      //   cmd: priv.commands.zone.audio,
      //   msg: "AudioSettings",
      // },
      // {
      //   cmd: priv.commands.zone.play_state,
      //   msg: "PlayState",
      // },
      {
        cmd: priv.commands.presets.list,
        msg: "Presets",
      },
    ];
    var p = 0;
    var cb = function(ret) {
      var l = cmds.length - 1;
      invokeCallback("onStartProgress", [ l - p, cmds[p].msg ]);
      p++;
    };

    for(var i = 0; i < cmds.length; i++)
      sendCB(cb, cmds[i].cmd, true);

    log.fnExit();
  }
  function onWSClose(code, reason) {
    log.fnEntry("SMoIP.onWSClose");
    invokeCallback("onConnectionClose", [ code, reason ]);
    log.fnExit();
  }
  function onWSMessage(message) {
    log.fnEntry("SMoIP.onWSMessage");

    var resp = null;
    try
    {
      resp = JSON.parse(message);
    }
    catch(err)
    {
      log.deb("Error: " + err.message);
    }

    var req = (resp && resp.params && resp.params.tag)
            ? priv.requests[resp.params.tag]
            : null;

    while(resp) {
      log.deb("Message follows:\n" + JSON.stringify(resp, null, 2));

      if(req && req.preNotify && req.callback)
        req.callback(resp.result == 200);

      if(resp.result && (resp.result != 200))
      {
        log.deb("'result' != 200");
        break;
      }
      if(!resp.path)
      {
        log.deb("'path' missing");
        break;
      }
      var path = resp.path.split("/");
      if(path.length <= 1)
      {
        log.deb("Invalid 'path'");
        break;
      }
      switch(path[1]) {
        case "presets":
          parsePresets(path, resp.params);
          break;
        case "system":
          parseSystem(path, resp.params);
          break;
        case "zone":
          parseZone(path, resp.params);
          break;
      }

      break;
    }

    if(req && !req.preNotify && req.callback)
      req.callback(resp.result == 200);

    if(req)
      priv.requests[resp.params.tag] = null;

    log.fnExit();
  }
  return {
    start: function() {
      log.fnEntry("SMoIP.start");
      if(!priv.WSHandle)
      {
        priv.WSHandle = new WS();
        priv.WSHandle.open("192.168.1.4/smoip");
        priv.WSHandle.connectOpenCallback(onWSOpen);
        priv.WSHandle.connectCloseCallback(onWSClose);
        priv.WSHandle.connectMessageCallback(onWSMessage);
      }
      log.fnExit();
    },  
    setProductName: function(callback, name) {
      if(!priv.WSHandle)
        return;

      sendCB(callback, {
        path: "/system/info",
        params: {
          name: name,
        },
      }, false);
    },
    setTimezone: function(callback, timezone) {
      if(!priv.WSHandle)
        return;

      sendCB(callback, {
        path: "/system/info",
        params: {
          timezone: timezone,
        },
      }, false);
    },
    setStandbyModeAndAPD: function(callback, mode, apd) {
      if(!priv.WSHandle || ((mode == null) && (apd == -1)))
        return;

      var cmd = {
        path: "/system/power",
        params: { },
      };

      if((mode != null) && (mode != priv.current.system.power.standby_mode))
        cmd.params.standby_mode = mode;
      if((apd != -1) && (apd != priv.current.system.power.auto_power_down))
        cmd.params.auto_power_down = apd;

      sendCB(callback, cmd, false);
    },
    setVolumeLimit: function(callback, limit) {
      var cmd = {
        path: "/zone/audio",
        params: {
          volume_limit_percent: limit,
        },
      };
      sendCB(callback, cmd, false);
    },
    refreshWireless: function(callback) {
      if(!priv.WSHandle)
        return;

      sendCB(callback, {
        path: "/system/network/wireless",
        params: {
          scan: true,
        },
      }, false);
    },
    setNetwork: function(callback, obj) {
      if(!priv.WSHandle)
        return;

      var cmd = {
        path: "/system/network",
        params: { },
      };

      for(var key in obj)
        cmd.params[key] = obj[key];

      sendCB(callback, cmd, false);
    },
    firmwareCheck: function(callback, early) {
      if(!priv.WSHandle)
        return;

      var cmd = {
        path: "/system/update",
        params: {
          action: "CHECK",
        },
      };

      if(early != null)
        cmd.params.early_update = !!early;

      sendCB(callback, cmd, false);
    },
    firmwareUpdate: function(callback) {
      if(!priv.WSHandle)
        return;

      sendCB(callback, {
        path: "/system/update",
        params: {
          action: "UPDATE",
        },
      }, false);
    },
    setCast: function(callback, obj) {
      if(!priv.WSHandle)
        return;

      var cmd = {
        path: "/system/sources/CAST",
        params: { },
      };

      for(var key in obj)
        cmd.params[key] = obj[key];

      sendCB(callback, cmd, false);
    },
    addPreset: function(callback, obj) {
      if(!priv.WSHandle)
        return;

      var cmd = {
        path: "/stream/radio",
        params: { },
      };

      for(var key in obj)
        cmd.params[key] = obj[key];

      sendCB(callback, cmd, false);
    },
    removePreset: function(callback, id) {
      if(!priv.WSHandle)
        return;

      sendCB(callback, {
        path: "/presets/delete",
        params: {
          preset: id,
        },
      }, false);
    },
    renamePreset: function(callback, obj) {
      if(!priv.WSHandle)
        return;

      var cmd = {
        path: "/presets/rename",
        params: { },
      };

      for(var key in obj)
        cmd.params[key] = obj[key];

      sendCB(callback, cmd, false);
    },
    playPreset: function(callback, id) {
      if(!priv.WSHandle)
        return;

      sendCB(callback, {
        path: "/zone/recall_preset",
        params: {
          preset: id,
        },
      }, false);
    },
    connectCallbacks: function(obj) {
      for(var key in obj)
        priv.callbacks[key] = obj[key];
    },
  };
};

var smoip = null;

var UUI = function() {
  var priv = {
    WSHandle: null,
    tries: -1,
    open: false,
    address: null,
    callbacks: { },
  };
  function onWSOpen() {
    log.fnEntry("UUI.onWSOpen");
    log.deb("UUI open");
    priv.open = true;
    if(priv.callbacks["onConnectionOpen"])
      priv.callbacks["onConnectionOpen"]();
    log.fnExit();
  }
  function onWSClose(code, reason) {
    log.fnEntry("UUI.onWSClose");
    if(!priv.open)
    {
      if(priv.tries--)
      {
        log.deb("Trying to reopen in a sec (" + priv.tries + ")");
        setTimeout(function() { priv.WSHandle.open(priv.address); }, 1000);
      }
    }
    else
    {
      priv.closing = false;
      priv.open = false;
      priv.tries = -1;

      if(priv.callbacks["onConnectionClose"])
        priv.callbacks["onConnectionClose"](code, reason);
    }
    log.fnExit();
  }
  function onWSMessage(message) {
    log.fnEntry("UUI.onWSMessage");
    var items = message.split("\0");
    log.deb("Data: " + items[0] + ", " + items[1] + ", " + items[2]);

    var output = items[1];
    if(output.length)
    {
      if(parseInt(items[2]) > -1)
        output += ": " + items[2] + "%";
    }
    else
    {
      output = aTexts.PleaseWait;
    }

    if(priv.callbacks["onMessage"])
      priv.callbacks["onMessage"](output);

    log.fnExit();
  }
  return {
    start: function() {
      log.fnEntry("UUI.start");
      if(!priv.WSHandle) {
        log.deb("UUI opening...");
        priv.tries = 30;
        priv.address = window.location.host + ":81/uui";
        priv.WSHandle = new WS();
        priv.WSHandle.connectOpenCallback(onWSOpen);
        priv.WSHandle.connectCloseCallback(onWSClose);
        priv.WSHandle.connectMessageCallback(onWSMessage);
        priv.WSHandle.open(priv.address);
      }
      log.fnExit();
    },
    connectCallbacks: function(obj) {
      for(var key in obj)
        priv.callbacks[key] = obj[key];
    },
  };
};

var uui = null;

var element = {
  getByID: function(id) {
    return document.getElementById(id);
  },
  create: function(name) {
    return document.createElement(name);
  },
  addChildrenS: function(el, suffix, ids) {
    if(ids.constructor !== Array)
      ids = [ ids ];
    if((suffix === undefined) || (suffix === null))
      suffix = "";
    var c = el.children;
    for(var i = 0; c && (i < c.length); i++)
    {
      if(ids.indexOf(c[i].id) >= 0)
      {
        c[i].id += suffix;
        this[c[i].id] = c[i];
      }
      this.addChildrenS(c[i], suffix, ids);
    }
  },
  addChildren: function(el, ids) {
    this.addChildrenS(el, null, ids);
  },
  disableArray: function(el) {
    if(el.constructor !== Array)
      el = [ el ];
    for(var i = 0; i < el.length; i++)
      el[i].disabled = true;
  },
  enableArray: function(el) {
    if(el.constructor !== Array)
      el = [ el ];
    for(var i = 0; i < el.length; i++)
      el[i].disabled = false;
  },
  visibleArray: function(el, val) {
    for(var i = 0; i < el.length; i++)
      el[i].style.display = val ? "block" : "none";
  },
  _add: function(el, force) {
    var isArray = el.constructor === Array;
    if(!isArray)
      el = [ el ];
    var output = [ ];
    for(var i = 0; i < el.length; i++)
    {
      if(force || !this[el[i]])
        this[el[i]] = this.getByID(el[i]);
      output.push(this[el[i]]);
    }
    return isArray ? output : output[0];
  },
  replace: function(el) {
    return this._add(el, true);
  },
  add: function(el) {
    return this._add(el, false);
  },
  check: function(el, val) {
    this.add(el).checked = val;
  },
  isChecked: function(el) {
    return this.add(el).checked;
  },
  enable: function(el, val) {
    this.add(el).disabled = !val;
  },
  focus: function(el) {
    this.add(el).focus();
  },
  styles: function(el, val) {
    this.add(el);
    for(var key in val)
      this[el].style[key] = val[key];
  },
  display: function(el, val) {
    this.styles(el, { display: val });
  },
  visible: function(el, val) {
    this.display(el, val ? "block" : "none");
  },
  visibleV: function(el, val) {
    if(val)
    {
      this.styles(el, {
        transition: "visibility 0s, opacity 1s ease-out",
        visibility: "visible",
        opacity: 1,
      });
    }
    else
    {
      this.styles(el, {
        transition: "visibility 1s, opacity 1s ease-in",
        visibility: "hidden",
        opacity: 0,
      });
    }
  },
  hide: function(el) {
    element.visible(el, false);
  },
  show: function(el) {
    element.visible(el, true);
  },
  setValue: function(el, val) {
    this.add(el);
    if("value" in this[el])
      this[el].value = val;
    else
      this[el].innerHTML = val;
  },
  setInnerHTML: function(el, val) {
    this.add(el).innerHTML = val;
  },
  getValue: function(el) {
    this.add(el);
    if("value" in this[el])
      return this[el].value;
    else
      return this[el].innerHTML;
  },
  setTitle: function(el, val) {
    this.add(el).title = val;
  },
  setPlaceholder: function(el, val) {
    this.add(el).placeholder = val;
  },
  setValueAndTitle: function(el, val) {
    this.setValue(el, val);
    this.setTitle(el, val);
  },
  setPseudoStyles: function(el, ba, styles) {
    this.add(el);
    if(!this["stylePseudoStyles"])
    {
      if(!this["head"])
        this["head"] = document.head || document.getElementsByTagName("head")[0];

      this["stylePseudoStyles"] = this.create("style");
      this["head"].appendChild(this["stylePseudoStyles"]);
    }
    if(!this["pseudoStyles"])
      this["pseudoStyles"] = { _index: 0 };

    var classes = this[el].className.split(" ");
    var pseudoStyle = null;
    for(var i = 0; i < classes.length; i++)
      if(classes[i].indexOf("pseudoStyle") >= 0)
      {
        pseudoStyle = classes[i];
        break;
      }

    if(!pseudoStyle)
    {
      pseudoStyle = "pseudoStyle" + this["pseudoStyles"]._index++;
      this[el].className += " " + pseudoStyle;
    }

    if(!this["pseudoStyles"][pseudoStyle])
      this["pseudoStyles"][pseudoStyle] = { };

    if(!this["pseudoStyles"][pseudoStyle][ba])
      this["pseudoStyles"][pseudoStyle][ba] = { };

    for(var key in styles)
      this["pseudoStyles"][pseudoStyle][ba][key] = styles[key];

    var txt = "\n";
    // iterate style names (pseudoStyleX)
    for(var key1 in this["pseudoStyles"])
    {
      // skip control properties
      if(key1.charAt(0) == "_")
        continue;
      // iterate before/after (pseudoStyleX:before/after)
      for(var key2 in this["pseudoStyles"][key1])
      {
        txt += "." + key1 + ":" + key2 + "{";
        // iterate properties (pseudoStyleX:before/after{property:value})
        for(var key3 in this["pseudoStyles"][key1][key2])
          txt += key3 + ":" + this["pseudoStyles"][key1][key2][key3] + ";";
        txt += "}\n";
      }
    }
    this["stylePseudoStyles"].innerHTML = txt;
  },
};

var popup = {
  aElements: Object.create(element),
  oParams: { },
  _preventDefault: function(e) {
    e = e || window.event;
    if(e.preventDefault)
      e.preventDefault();
    e.returnValue = false;
  },
  _preventDefaultKeys: function(e) {
    var keys = { 37: 1, 38: 1, 39: 1, 40: 1 };
    if((e.target === document.body) && keys[e.keyCode])
    {
      popup._preventDefault(e);
      return false;
    }
  },
  _disableScroll: function() {
    var el = popup.aElements;
    el.styles("body", {
      height: "100%",
      overflow: "hidden",
    });
    el.styles("contScrollHelper", { "margin-right": "" });
    el.styles("contHeaderContent", { "margin-right": "" });
//    if(window.addEventListener)
//      window.addEventListener("DOMMouseScroll", popup._preventDefault, false);
//    window.onwheel = popup._preventDefault;
//    window.onmousewheel = document.onmousewheel = popup._preventDefault;
//    window.ontouchmove = popup._preventDefault;
//    document.onkeydown = popup._preventDefaultKeys;
  },
  _enableScroll: function() {
    var el = popup.aElements;
    var widthHeader = el.add("contHeader").clientWidth;
    el.styles("body", {
      height: "",
      overflow: "",
    });
    var widthHelper = el.add("contScrollHelper").clientWidth;
    if(widthHeader > widthHelper)
    {
      var val = (widthHelper - widthHeader) + "px";
      el.styles("contScrollHelper", { "margin-right": val });
      el.styles("contHeaderContent", { "margin-right": val });
    }

//    if(window.removeEventListener)
//      window.removeEventListener("DOMMouseScroll", popup._preventDefault, false);
//    window.onmousewheel = document.onmousewheel = null;
//    window.onwheel = null;
//    window.ontouchmove = null;
//    document.onkeydown = null;
  },
  _showMainContainer: function() {
    var el = popup.aElements;
    popup._disableScroll();
    el.styles("contPopup", {
      transition: "visibility 0s",
      visibility: "visible",
    });
    el.display("contPopupContent", "inline-block");
    el.styles("divPopupBack", {
      transition: "opacity 1s",
      opacity: "0.5",
    });
    el.focus("aPopupDefocuser");
  },
  _hideMainContainer: function() {
    var el = popup.aElements;
    el.hide("contPopupContent");
    el.styles("divPopupBack", {
      transition: "opacity 1s",
      opacity: "0",
    });
    el.styles("contPopup", {
      transition: "visibility 1s",
      visibility: "hidden",
    });
    popup._enableScroll();
  },
  updateParams: function(params, keepOld) {
    if(!params)
      params = { };
    if(keepOld)
      for(var key in params)
        popup.oParams[key] = params[key];
    else
      popup.oParams = params;
  },
  _updateButtonsContainer: function() {
    var el = popup.aElements;
    var title = popup.oParams.title;
    var content = popup.oParams.content;
    var text = popup.oParams.text;
    el.setValue("valPopupButtonsHeader", title ? title : "");
    el.setValue("valPopupButtonsText", text ? text : "");
    if(!text && content)
      while(content.childNodes.length > 0)
        el["valPopupButtonsText"].appendChild(content.firstChild);
  },
  _hideButtonsContainer: function(hide, descend) {
    var el = popup.aElements;
    if(!hide)
    {
      var params = popup.oParams;
      if(params.title)
        el.setValue("valPopupButtonsHeader", params.title);
      if(params.text)
        el.setValue("valPopupButtonsText", params.text);
      if(params.delay)
      {
        setTimeout(function() { popup._hideButtonsContainer(true, true); }, params.delay);
        return;
      }
    }
    el.hide("contPopupButtons");
    el.hide("contBtnPopupOK");
    el.hide("contBtnPopupYesNo");
    if(descend)
      popup._hideMainContainer();
  },
  _showButtonsContainer: function() {
    var el = popup.aElements;
    popup._hideButtonsContainer(true, false);
    popup._updateButtonsContainer();
    popup._showMainContainer();
    el.show("contPopupButtons");
  },
  btnOKOKClick: function() {
    var el = popup.aElements;
    el.add("contBtnPopupOKOK");
    var params = popup.oParams;
    if(params.keep)
    {
      if(params.callbackSpinOK)
        spin.invokeButtonAction({
          elements: [
            el["btnPopupOKOK"],
          ],
          container: el["contBtnPopupOKOK"],
          action: params.callbackSpinOK,
        });
    }
    else
    {
      popup.hide();
    }
    if(params.callbackOK)
      params.callbackOK();
  },
  showOK: function(params) {
    var el = popup.aElements;
    popup.updateParams(params, false);
    popup._showButtonsContainer();
    params = popup.oParams;
    el.setInnerHTML("btnPopupOKOK", params.buttonOK ? params.buttonOK : aTexts.OK);
    el.show("contBtnPopupOK");
    if((params.focus == null) || (params.focus == "OK"))
      el.focus("btnPopupOKOK");
    else if(params.content)
    {
      if(params.focus.focus)
      {
        params.focus.focus();
      }
      else
      {
        var toFocus = document.getElementById(params.focus);
        if(toFocus)
          toFocus.focus();
      }
    }
  },
  getOKButton: function() {
    return popup.aElements.add("btnPopupOKOK");
  },
  showError: function(params) {
    params.title = aTexts.Error;
    popup.showOK(params);
  },
  btnYesNoYesClick: function() {
    var params = popup.oParams;
    if(!params.keep)
      popup.hide();
    if(params.callbackYes)
      params.callbackYes();
    if(params.callbackYesNo)
      params.callbackYesNo(true);
  },
  btnYesNoNoClick: function() {
    var params = popup.oParams;
    if(!params.keep)
      popup.hide();
    if(params.callbackNo)
      params.callbackNo();
    if(params.callbackYesNo)
      params.callbackYesNo(false);
  },
  showYesNo: function(params) {
    var el = popup.aElements;
    popup.updateParams(params, false);
    params = popup.oParams;
    if(params.withContinue)
      params.text += "<br/>" + aTexts.Continue + "?";
    popup._showButtonsContainer();
    var txtYes = params.buttonYes ? params.buttonYes : aTexts.Yes;
    var txtNo = params.buttonNo ? params.buttonNo : aTexts.No;
    el.setInnerHTML("btnPopupYesNoYes", txtYes);
    el.setInnerHTML("btnPopupYesNoNo", txtNo);
    el.show("contBtnPopupYesNo");
    if((params.focus == null) || (params.focus == txtYes))
      el.focus("btnPopupYesNoYes");
    else if(params.focus == txtNo)
      el.focus("btnPopupYesNoNo");
    else if(params.content)
    {
      if(params.focus.focus)
      {
        params.focus.focus();
      }
      else
      {
        var toFocus = document.getElementById(params.focus);
        if(toFocus)
          toFocus.focus();
      }
    }
  },
  getYesButton: function() {
    return popup.aElements.add("btnPopupYesNoYes");
  },
  getNoButton: function() {
    return popup.aElements.add("btnPopupYesNoNo");
  },
  showMessage: function(params) {
    popup.updateParams(params, false);
    popup._showButtonsContainer();
  },
  updateMessage: function(params, keepOld) {
    popup.updateParams(params, keepOld);
    popup._updateButtonsContainer();
  },
  hideMessage: function(params, keepOld) {
    popup.updateParams(params, keepOld);
    popup._hideButtonsContainer(false, true);
  },
  hide: function() {
    popup._hideButtonsContainer(true, true);
  },
};

var secSource = {
  aElements: Object.create(element),
  currNowPlaying: { art: "", },
  escapeHTMLEntities: function(text) {
    if(!text)
      return "";
    var entityTable = {
        34: 'quot',     38: 'amp',      39: 'apos',     60: 'lt',
        62: 'gt',      160: 'nbsp',    161: 'iexcl',   162: 'cent',
       163: 'pound',   164: 'curren',  165: 'yen',     166: 'brvbar',
       167: 'sect',    168: 'uml',     169: 'copy',    170: 'ordf',
       171: 'laquo',   172: 'not',     173: 'shy',     174: 'reg',
       175: 'macr',    176: 'deg',     177: 'plusmn',  178: 'sup2',
       179: 'sup3',    180: 'acute',   181: 'micro',   182: 'para',
       183: 'middot',  184: 'cedil',   185: 'sup1',    186: 'ordm',
       187: 'raquo',   188: 'frac14',  189: 'frac12',  190: 'frac34',
       191: 'iquest',  192: 'Agrave',  193: 'Aacute',  194: 'Acirc',
       195: 'Atilde',  196: 'Auml',    197: 'Aring',   198: 'AElig',
       199: 'Ccedil',  200: 'Egrave',  201: 'Eacute',  202: 'Ecirc',
       203: 'Euml',    204: 'Igrave',  205: 'Iacute',  206: 'Icirc',
       207: 'Iuml',    208: 'ETH',     209: 'Ntilde',  210: 'Ograve',
       211: 'Oacute',  212: 'Ocirc',   213: 'Otilde',  214: 'Ouml',
       215: 'times',   216: 'Oslash',  217: 'Ugrave',  218: 'Uacute',
       219: 'Ucirc',   220: 'Uuml',    221: 'Yacute',  222: 'THORN',
       223: 'szlig',   224: 'agrave',  225: 'aacute',  226: 'acirc',
       227: 'atilde',  228: 'auml',    229: 'aring',   230: 'aelig',
       231: 'ccedil',  232: 'egrave',  233: 'eacute',  234: 'ecirc',
       235: 'euml',    236: 'igrave',  237: 'iacute',  238: 'icirc',
       239: 'iuml',    240: 'eth',     241: 'ntilde',  242: 'ograve',
       243: 'oacute',  244: 'ocirc',   245: 'otilde',  246: 'ouml',
       247: 'divide',  248: 'oslash',  249: 'ugrave',  250: 'uacute',
       251: 'ucirc',   252: 'uuml',    253: 'yacute',  254: 'thorn',
       255: 'yuml',    338: 'OElig',   339: 'oelig',   352: 'Scaron',
       353: 'scaron',  376: 'Yuml',    402: 'fnof',    710: 'circ',
       732: 'tilde',   913: 'Alpha',   914: 'Beta',    915: 'Gamma',
       916: 'Delta',   917: 'Epsilon', 918: 'Zeta',    919: 'Eta',
       920: 'Theta',   921: 'Iota',    922: 'Kappa',   923: 'Lambda',
       924: 'Mu',      925: 'Nu',      926: 'Xi',      927: 'Omicron',
       928: 'Pi',      929: 'Rho',     931: 'Sigma',   932: 'Tau',
       933: 'Upsilon', 934: 'Phi',     935: 'Chi',     936: 'Psi',
       937: 'Omega',   945: 'alpha',   946: 'beta',    947: 'gamma',
       948: 'delta',   949: 'epsilon', 950: 'zeta',    951: 'eta',
       952: 'theta',   953: 'iota',    954: 'kappa',   955: 'lambda',
       956: 'mu',      957: 'nu',      958: 'xi',      959: 'omicron',
       960: 'pi',      961: 'rho',     962: 'sigmaf',  963: 'sigma',
       964: 'tau',     965: 'upsilon', 966: 'phi',     967: 'chi',
       968: 'psi',     969: 'omega',   977: 'thetasym',978: 'upsih',
       982: 'piv',    8226: 'bull',   8230: 'hellip', 8242: 'prime',
      8243: 'Prime',  8254: 'oline',  8260: 'frasl',  8472: 'weierp',
      8465: 'image',  8476: 'real',   8482: 'trade',  8501: 'alefsym',
      8592: 'larr',   8593: 'uarr',   8594: 'rarr',   8595: 'darr',
      8596: 'harr',   8629: 'crarr',  8656: 'lArr',   8657: 'uArr',
      8658: 'rArr',   8659: 'dArr',   8660: 'hArr',   8704: 'forall',
      8706: 'part',   8707: 'exist',  8709: 'empty',  8711: 'nabla',
      8712: 'isin',   8713: 'notin',  8715: 'ni',     8719: 'prod',
      8721: 'sum',    8722: 'minus',  8727: 'lowast', 8730: 'radic',
      8733: 'prop',   8734: 'infin',  8736: 'ang',    8743: 'and',
      8744: 'or',     8745: 'cap',    8746: 'cup',    8747: 'int',
      8756: 'there4', 8764: 'sim',    8773: 'cong',   8776: 'asymp',
      8800: 'ne',     8801: 'equiv',  8804: 'le',     8805: 'ge',
      8834: 'sub',    8835: 'sup',    8836: 'nsub',   8838: 'sube',
      8839: 'supe',   8853: 'oplus',  8855: 'otimes', 8869: 'perp',
      8901: 'sdot',   8968: 'lceil',  8969: 'rceil',  8970: 'lfloor',
      8971: 'rfloor', 9001: 'lang',   9002: 'rang',   9674: 'loz',
      9824: 'spades', 9827: 'clubs',  9829: 'hearts', 9830: 'diams',
      8194: 'ensp',   8195: 'emsp',   8201: 'thinsp', 8204: 'zwnj',
      8205: 'zwj',    8206: 'lrm',    8207: 'rlm',    8211: 'ndash',
      8212: 'mdash',  8216: 'lsquo',  8217: 'rsquo',  8218: 'sbquo',
      8220: 'ldquo',  8221: 'rdquo',  8222: 'bdquo',  8224: 'dagger',
      8225: 'Dagger', 8240: 'permil', 8249: 'lsaquo', 8250: 'rsaquo',
      8364: 'euro',
    };
    return text.replace(/[\u00a0-\u2666"\&'<>]/g, function(c) {
      return "&" + (entityTable[c.charCodeAt(0)] || "#" + c.charCodeAt(0)) + ";";
    });
  },
  updateSourceItems: function(obj) {
    secSource.aSources = obj;
  },
  updatePSMetadata: function(metadata) {
    var el = secSource.aElements;
    var aat = [ null, null, null]; // album, artist, title
    var art = null;
    var idx = 0;
    switch(metadata.class)
    {
      case "md.radio":
      case "md.radio.airable":
        aat[idx++] = metadata.station;
        aat[idx++] = metadata.artist;
        aat[idx++] = metadata.title;
        art = metadata.art_url;
        break;
      case "md.input":
        if(metadata.signal)
        {
          if(metadata.sample_rate)
            aat[idx++] = (metadata.sample_rate / 1000).toFixed(1) + "kHz";
        }
        else
        {
          aat[idx++] = aTexts.NoSignal;
        }
        break;
      case "md.bluetooth":
        if(metadata.signal)
        {
          if(metadata.album)
            aat[idx++] = metadata.album;
          else if(metadata.device)
            aat[idx++] = metadata.device;

          if(metadata.artist)
            aat[idx++] = metadata.artist;
          if(metadata.title)
            aat[idx++] = metadata.title;

          if(idx < 3)
            if(metadata.sample_rate)
            {
              var tmp = (metadata.sample_rate / 1000).toFixed(1) + "kHz";
              if(metadata.codec)
                tmp += " " + metadata.codec;
              aat[idx++] = tmp;
            }
            else if(metadata.codec)
            {
              aat[idx++] = metadata.codec;
            }
        }
        else
        {
          aat[idx++] = aTexts.NoSignal;
        }
        break;
      case "md.track":
      case "md.track.library":
      case "md.track.spotify":
        aat[idx++] = metadata.album;
        aat[idx++] = metadata.artist;
        aat[idx++] = metadata.title;
        art = metadata.art_url;
        break;
      case "md.track.cast":
        aat[idx++] = metadata.album
                   ? metadata.album
                   : metadata.device;
        aat[idx++] = metadata.artist;
        aat[idx++] = metadata.title;
        art = metadata.art_url;
        break;
      case "md.track.pandora":
        aat[idx++] = metadata.album
                   ? metadata.album
                   : metadata.station;
        aat[idx++] = metadata.artist;
        aat[idx++] = metadata.title;
        art = metadata.art_url;
        break;
      case "md.advert.pandora":
        aat[idx++] = metadata.station;
        aat[idx++] = metadata.company;
        aat[idx++] = metadata.advert;
        art = metadata.art_url;
        break;
    }
    var np = secSource.currNowPlaying;
    if(np.title != aat[2])
    {
      np.title = aat[2];
      el.setValue("valNowPlayingTitle", secSource.escapeHTMLEntities(np.title));
      el.setTitle("valNowPlayingTitle", np.title);
    }
    if(np.artist != aat[1])
    {
      np.artist = aat[1];
      el.setValue("valNowPlayingArtist", secSource.escapeHTMLEntities(np.artist));
      el.setTitle("valNowPlayingArtist", np.artist);
    }
    if(np.album != aat[0])
    {
      np.album = aat[0];
      el.setValue("valNowPlayingAlbum", secSource.escapeHTMLEntities(np.album));
      el.setTitle("valNowPlayingAlbum", np.album);
    }
    if(np.art != art)
    {
      np.art = art;
      var dummyArt = "images/DummyAlbumArt.png";
      var src = art ? art : dummyArt;
      var img = new Image();
      img.onload = function() {
        el.styles("contNowPlayingArt", {
          backgroundImage: "url('" + src + "')",
        });
        img = null;
      };
      img.onerror = function() {
        el.styles("contNowPlayingArt", {
          backgroundImage: "url('" + dummyArt + "')",
        });
        img = null;
      };
      img.src = src;
    }
  },
  updateSource: function(src) {
    var el = secSource.aElements;
    if(!secSource.aSources)
      return;

    if(!src)
    {
      el.setValue("valStatusCurrentSource", "N/A");
      el.hide("contSourceInfo");
    }
    else
    {
      for(var i = 0; i < secSource.aSources.length; i++)
      {
        if(secSource.aSources[i].id == src)
        {
          el.setValue("valStatusCurrentSource", secSource.aSources[i].name);
          var w = 180 + (el["valStatusCurrentSource"].offsetWidth / 2);
          el.styles("contNowPlaying", { marginLeft: -w + "px", });
          element.setPseudoStyles("contNowPlaying", "after", { "left": w + "px" });
          break;
        }
      }
      el.display("contSourceInfo", "inline-block");
    }
  },
  btnNowPlayingClick: function() {
    var el = secSource.aElements;

    secSource.nowPlayingShown = !secSource.nowPlayingShown;

    el.visibleV("contNowPlaying", secSource.nowPlayingShown);
  },
};

var secStatus = {
  aElements: Object.create(element),
  aConnections: {
    "wired": {
      name: aTexts.network.Wired,
      show: [ ],
    },
    "wireless": {
      name: aTexts.network.Wireless,
      show: [ "NetworkName", "SignalStrength" ],
    },
    "ap": {
      name: aTexts.network.AccessPoint,
      show: [ "NetworkName" ],
    },
  },
  updateConnection: function(conn) {
    var el = secStatus.aElements;
    var txt = "";
    var show = [ ];
    if(secStatus.aConnections[conn])
    {
      txt = secStatus.aConnections[conn].name;
      show = secStatus.aConnections[conn].show;
    }
    el.setValue("valStatusConnection", txt);
    el.visible("contStatusNetworkName", show.indexOf("NetworkName") >= 0);
    el.visible("contStatusSignalStrength", show.indexOf("SignalStrength") >= 0);
  },
  updateIPAddress: function(obj) {
    var el = secStatus.aElements;
    if(obj.ipv4 && obj.ipv4.address)
      el.setValue("valStatusIPAddress", obj.ipv4.address);
    if(obj.ipv6 && obj.ipv6.address)
    {
      el.setValue("valStatusIPv6Address", obj.ipv6.address);
      el.show("contStatusIPv6Address");
    }
  },
  updateCurrentNetwork: function(obj) {
    var el = secStatus.aElements;
    if(obj && obj.current)
    {
      el.setValue("valStatusSignalStrength", obj.current.signal
                                           ? (obj.current.signal + "%")
                                           : "");
      el.setValue("valStatusNetworkName", secNetwork.hex2text(obj.current.ssid));
    }
  },
  init: function() {
    var el = secStatus.aElements;
    var txt = aTexts.status;
    var obj = {
      "valStatusHeader":            txt.CurrentStatus,
      "valStatusHdrConnection":     txt.ConnectionMode,
      "valStatusHdrNetworkName":    txt.NetworkName + ":",
      "valStatusHdrSignalStrength": txt.SignalStrength,
      "valStatusHdrIPAddress":      txt.IPAddress + ":",
      "valStatusHdrIPv6Address":    txt.IPv6Address + ":",
      "valStatusHdrSource":         txt.Source,
    };
    for(var key in obj)
      el.setInnerHTML(key, obj[key]);
  },
};

var secProduct = {
  aElements: Object.create(element),
  _availSources: { },
  _sourceAvailCallbacks: [ ],
  _modelCallbacks: [ ],
  _updateDescription: function() {
    var el = secProduct.aElements;
    var d = "";
    if(secProduct.description)
      d += secProduct.description;

    var id = "Description";
    if(secProduct._availSources["airplay"])
      id += "Airplay";
    if(secProduct._availSources["spotify"])
      id += "Spotify";
    if(secProduct._availSources["cast"])
      id += "Cast";

    d += " " + aTexts.product[id];
    el.setValue("valProductDesc", d);
  },
  _getModel: function(model) {
    if(!secProduct.oModel)
    {
      var pretty_name = model;
      var d = "";
      switch(model) {
        case "Edge NQ":
          pretty_name = "<b>Edge</b> NQ";
          d = "Network Preamplifier";
          break;
        case "CXN":
          pretty_name = "<b>CX</b>N";
          d = "Network Player";
          break;
        case "CXNv2":
          pretty_name = "<b>CX</b>N v2";
          d = "Network Player";
          break;
        case "CXR200":
          pretty_name = "<b>CX</b>R200";
          d = "200W AV Receiver";
          break;
        case "CXR120":
          pretty_name = "<b>CX</b>R120";
          d = "120W AV Receiver";
          break;
        case "851N":
          pretty_name = "<b>Azur</b> 851N";
          d = "Network Player, DAC & Preamplifier";
          break;
        case "Stream Magic 6v2":
          pretty_name = "<b>Stream Magic</b> 6 v2";
          d = "Upsampling Network Player";
          break;
      }
      secProduct.oModel = {
        name: model,
        name_html: pretty_name,
        description: d,
      };
    }
    return secProduct.oModel;
  },
  updateModel: function(model) {
    var m = secProduct._getModel(model);
    for(var i = 0; i < secProduct._modelCallbacks.length; i++)
      secProduct._modelCallbacks[i](m);
  },
  _loadName: function() {
    var el = secProduct.aElements;
    el.setPlaceholder("inpProductName", aTexts.product.ProductName);
    el.setTitle("inpProductName", aTexts.product.ProductName);
  },
  updateName: function(name) {
    var el = secProduct.aElements;
    el.setValue("inpProductName", name);
  },
  updateSources: function(sources) {
    var isAvail = {
      airplay: false,
      spotify: false,
      cast: false,
    };
    for(var i = 0; i < sources.length; i++)
    {
      if(sources[i].id === "AIRPLAY")
        isAvail["airplay"] = true;
      if(sources[i].id === "SPOTIFY")
        isAvail["spotify"] = true;
      if(sources[i].id === "CAST")
        isAvail["cast"] = true;
    }
    for(var i = 0; i < secProduct._sourceAvailCallbacks.length; i++)
      secProduct._sourceAvailCallbacks[i](isAvail);
  },
  connectSourceAvailCallback: function(cb) {
    secProduct._sourceAvailCallbacks.push(cb);
  },
  connectModelCallback: function(cb) {
    secProduct._modelCallbacks.push(cb);
  },
  btnSaveClick: function() {
    var el = secProduct.aElements;
    var productName = el.getValue("inpProductName");
    if(!productName.length)
    {
      popup.showError({
        text: aTexts.product.NameNotEntered,
        callbackOK: function() {
          el.focus("inpProductName");
        },
      });
    }
    else
    {
			secCast.updateName(productName);
      spin.invokeButtonAction({
        elements: el.add([ "inpProductName", "btnProductSave" ]),
        container: el["contBtnProductSave"],
        action: smoip.setProductName,
        params: [ productName ],
      });
    }
  },
  init: function() {
    var el = secProduct.aElements;
    var txt = aTexts.product;
    var obj = {
      "valProductHeader": txt.RenameYourUnit,
      "btnProductSave":   aTexts.Save,
    };
    for(var key in obj)
      el.setInnerHTML(key, obj[key]);

    secProduct._loadName();

    secProduct.connectModelCallback(function(model) {
      document.title = model.name + " Webmin";
      el.setValue("valHeaderProductModel", model.name_html);
      el.setValue("valHeaderProductDesc", model.description);
      secProduct.description = aTexts.product.CustomiseTheName.replace(/PRODUCT/g, model.name);
      secProduct._updateDescription();
    });
    secProduct.connectSourceAvailCallback(function(sources) {
      secProduct._availSources = sources;
      secProduct._updateDescription();
    });
  },
};

var secNetwork = {
  aElements: Object.create(element),
  aEncryptions: [
    {
      type: [ "none" ],
      name: "None",
      hint: null,
      title: null,
      show: null,
      error: null,
      q: null,
    },
    {
      type: [ "wep" ],
      name: "WEP",
      hint: aTexts.network.Passphrase,
      title: aTexts.network.Passphrase,
      show: aTexts.network.ShowPassphrase,
      error: aTexts.network.NoPassphraseEntered,
      q: {
        title: aTexts.network.NoPassphraseEntered,
        text: aTexts.network.NoPassphraseInfo,
      },
    },
    {
      type: [ "wpa-tkip", "wpa-ccmp" ],
      name: "WPA",
      hint: aTexts.network.Passphrase,
      title: aTexts.network.Passphrase,
      show: aTexts.network.ShowPassphrase,
      error: aTexts.network.NoPassphraseEntered,
      q: {
        title: aTexts.network.NoPassphraseEntered,
        text: aTexts.network.NoPassphraseInfo,
      },
    },
    {
      type: [ "wpa2-tkip", "wpa2-ccmp" ],
      name: "WPA2",
      hint: aTexts.network.Passphrase,
      title: aTexts.network.Passphrase,
      show: aTexts.network.ShowPassphrase,
      error: aTexts.network.NoPassphraseEntered,
      q: {
        title: aTexts.network.NoPassphraseEntered,
        text: aTexts.network.NoPassphraseInfo,
      },
    },
    {
      type: [ "wpa" ],
      name: "WPA/WPA2",
      hint: aTexts.network.Passphrase,
      title: aTexts.network.Passphrase,
      show: aTexts.network.ShowPassphrase,
      error: aTexts.network.NoPassphrase,
      q: {
        title: aTexts.network.NoPassphraseEntered,
        text: aTexts.network.NoPassphraseInfo,
      },
    },
  ],
  aIPElements: [
    {
      id: "inpIPAddress",
      hint: aTexts.network.IPAddress,
      title: aTexts.network.IPAddress,
      error: aTexts.network.InvalidAddressEntered,
    },
    {
      id: "inpIPSubnet",
      hint: aTexts.network.SubnetMask,
      title: aTexts.network.SubnetMask,
      error: aTexts.network.InvalidAddressEntered,
    },
    {
      id: "inpIPGateway",
      hint: aTexts.network.DefaultGateway,
      title: aTexts.network.DefaultGateway,
      error: aTexts.network.InvalidAddressEntered,
    },
    {
      id: "inpIPPrimaryDNS",
      hint: aTexts.network.PrimaryDNSServer,
      title: aTexts.network.PrimaryDNSServer,
      error: aTexts.network.InvalidAddressEntered,
    },
    {
      id: "inpIPSecondaryDNS",
      hint: aTexts.network.SecondaryDNSServer,
      title: aTexts.network.SecondaryDNSServer,
      error: aTexts.network.InvalidAddressEntered,
    },
  ],
  checkIPv4Address: function(address) {
    var m = address.match(/^(\d+)\.(\d+)\.(\d+)\.(\d+)$/);
    if(m)
      for(var i = 1; i <= 4; i++)
        if((m[i] < 0) || (m[i] > 255))
        {
          m = null;
          break;
        }
    return m;
  },
  checkIPv4Gateway: function(gateway, addrMatch, maskMatch) {
    var m = secNetwork.checkIPv4Address(gateway);
    if(!m)
      return null;

    var mask = (maskMatch[1] << 24) | (maskMatch[2] << 16) | (maskMatch[3] << 8) | maskMatch[4];
    var addr = (addrMatch[1] << 24) | (addrMatch[2] << 16) | (addrMatch[3] << 8) | addrMatch[4];
    var gate = (m[1] << 24) | (m[2] << 16) | (m[3] << 8) | m[4];

    addr &= mask;
    gate &= mask;

    return (addr == gate) ? m : null;
  },
  prefix2mask: function(prefix) {
    var i = 0xFFFFFFFF;
    i <<= 32 - prefix;
    var s = "";
    s += ((i & 0xFF000000) >>> 24) + ".";
    s += ((i & 0x00FF0000) >>> 16) + ".";
    s += ((i & 0x0000FF00) >>> 8) + ".";
    s += ((i & 0x000000FF) >>> 0);
    return s;
  },
  mask2prefix: function(mask) {
    var x = (mask[1] << 24) | (mask[2] << 16) | (mask[3] << 8) | mask[4];
    for(var p = 0; p < 32; p++)
    {
      if((x & 0x80000000) == 0)
        break;
      x <<= 1;
    }
    return x ? -1 : p;
  },
  hex2text: function(hex) {
    var text;
    var uri = hex.replace(/[0-9A-Fa-f]{2}/g, "%$&");

    /* if URI is invalid replace chars >0x7F by 0x20 (spaces) */
    try
    {
      text = decodeURIComponent(uri);
    }
    catch(e)
    {
      text = decodeURIComponent(uri.replace(/%[8-9A-Fa-f][0-9A-Fa-f]/g, "%20"));
    }
    return text;
  },
  char2hex: function(c) {
    return c.charCodeAt(0).toString(16);
  },
  text2hex: function(text) {
    return encodeURIComponent(text.replace(/[!-~]/g, secNetwork.char2hex)).replace(/%/g, "");
  },
  getIPElementByID: function(id) {
    for(var i = 0; i < secNetwork.aIPElements.length; i++)
      if(secNetwork.aIPElements[i].id == id)
        return secNetwork.aIPElements[i];
  },
  getSelectedNetwork: function() {
    var el = secNetwork.aElements;
    var net = secNetwork.oNetworks;
    if(net && net.available)
      for(var i = 0; i < net.available.length; i++)
        if(net.available[i]._index == el["selWiFiNetwork"].selectedIndex)
          return net.available[i];
    return null;
  },
  getEncryptionByType: function(type) {
    for(var i = secNetwork.aEncryptions.length; i--; )
    {
      var enc = secNetwork.aEncryptions[i];
      if(enc.type && (enc.type.indexOf(type) >= 0))
        return enc;
    }
    return null;
  },
  getEncryptionByIndex: function(idx) {
    for(var i = secNetwork.aEncryptions.length; i--; )
    {
      var enc = secNetwork.aEncryptions[i];
      if(enc._index == idx)
        return enc;
    }
    return null;
  },
  getSelectedEncryption: function() {
    var el = secNetwork.aElements;
    return secNetwork.getEncryptionByIndex(el["selWiFiEncryption"].selectedIndex);
  },
  updateIPInfo: function(obj) {
    var el = secNetwork.aElements;

    if(obj.ipv4)
    {
      if(obj.ipv4.address)
        el.setValue("inpIPAddress", obj.ipv4.address);
      if(obj.ipv4.prefix)
        el.setValue("inpIPSubnet", secNetwork.prefix2mask(obj.ipv4.prefix));
      if(obj.ipv4.gateway)
        el.setValue("inpIPGateway", obj.ipv4.gateway);
      if(obj.ipv4.dns)
      {
        if(obj.ipv4.dns.length > 0)
          el.setValue("inpIPPrimaryDNS", obj.ipv4.dns[0]);
        if(obj.ipv4.dns.length > 1)
          el.setValue("inpIPSecondaryDNS", obj.ipv4.dns[1]);
      }
    }

    if(obj.dhcp != null)
    {
      el.check("chbIPStatic", !obj.dhcp);
      secNetwork.chbStaticAddressConfigClick();
    }
  },
  updateConnection: function(conn) {
    secNetwork._connection = conn;
  },
  loadNetworks: function() {
    var el = secNetwork.aElements;
    if(!el["selWiFiNetwork"])
    {
      el.setTitle("selWiFiNetwork", aTexts.network.Network);
    }
    if(!el["selWiFiNetwork"].options.length)
    {
      var option = el.create("option");
      option.disabled = true;
      option.style.display = "none";
      el["selWiFiNetwork"].add(option);
      el["selWiFiNetwork"].selectedIndex = 0;
    }
    if(!el["inpWiFiManualName"])
    {
      el.setTitle("inpWiFiManualName", aTexts.network.NetworkName);
      el.setPlaceholder("inpWiFiManualName", aTexts.network.NetworkName);
    }
  },
  populateNetworks: function(sel, networks) {
    var offset = 1; // make sure every 'sel' object already has just one option
    for(var i = sel.options.length; --i >= offset; )
      sel.options[i] = null;

    if(networks && networks.available)
    {
      sel.options[0].text = aTexts.network.SelectNetwork;

      var current = networks.current && networks.current.ssid
                  ? networks.current.ssid
                  : null;
      for(var i = 0; i < networks.available.length; i++) {
        networks.available[i]._index = offset + i;
        var option = element.create("option");
        option.text = secNetwork.hex2text(networks.available[i].ssid);
        var title = aTexts.network.Signal + " " + networks.available[i].signal + "%";
        var enc = secNetwork.getEncryptionByType(networks.available[i].encryption);
        if(enc)
          title += "\n" + aTexts.network.Encryption + " " + enc.name;
        option.title = title;
        sel.add(option);
        if(networks.available[i].ssid == current)
          sel.selectedIndex = offset + i;
      }
      sel.disabled = false;
    }
    else
    {
      sel.disabled = true;
      sel.options[0].text = aTexts.network.NoNetworksAvailable;
    }
  },
  populateEncryptions: function(sel) {
    var enc = secNetwork.aEncryptions;
    var offset = 1;
    for(var i = 0; i < enc.length; i++)
    {
      enc[i]._index = offset + i;
      var option = element.create("option");
      option.text = enc[i].name;
      sel.add(option);
    }
  },
  updateNetworks: function(obj) {
    var el = secNetwork.aElements;

    el["selWiFiNetwork"].selectedIndex = 0;

    secNetwork.oNetworks = obj;
    secNetwork.populateNetworks(el["selWiFiNetwork"], obj);

    secNetwork.updateEncryptionElements();
  },
  chbWiFiManualClick: function() {
    var el = secNetwork.aElements;
    var checked = el.isChecked("chbWiFiManual");
    el.visible("contWiFiAuto", !checked);
    el.visible("contWiFiManual", checked);
    secNetwork.updateEncryptionElements();
  },
  btnWiFiRefreshClick: function() {
    var el = secNetwork.aElements;
    spin.invokeButtonAction({
      elements: el.add([
        "chbWiFiManual",   "btnWiFiRefresh",    "selWiFiNetwork",
        "inpWiFiKey",      "chbWiFiKeyShow",    "chbIPStatic",
        "inpIPAddress",    "inpIPSubnet",       "inpIPGateway",
        "inpIPPrimaryDNS", "inpIPSecondaryDNS", "btnNetworkSave",
      ]),
      container: el.add("contBtnWiFiRefresh"),
      action: smoip.refreshWireless,
    });
  },
  updateEncryptionElements: function() {
    log.fnEntry("secNetwork.updateEncryptionElements");
    var el = secNetwork.aElements;

    var enc = null;
    if(el.isChecked("chbWiFiManual"))
    {
      enc = secNetwork.getSelectedEncryption();
    }
    else
    {
      var net = secNetwork.getSelectedNetwork();
      if(net)
        enc = secNetwork.getEncryptionByType(net.encryption);
    }

    var hint = "";
    var title = "";
    var show = "";
    if(enc) {
      log.deb("Encryption: " + enc.name);
      hint = enc.hint;
      title = enc.title;
      show = enc.show;
    }

    el.setTitle("inpWiFiKey", title);
    el.setPlaceholder("inpWiFiKey", hint);
    el.setValue("chbValWiFiKeyShow", show);
    el.visible("contWiFiKey", hint);
    log.fnExit();
  },
  selWiFiEncryptionChange: function() {
    secNetwork.updateEncryptionElements();
  },
  selWiFiNetworkChange: function() {
    secNetwork.updateEncryptionElements();
  },
  chbShowWiFiKeyClick: function() {
    var el = secNetwork.aElements;
    el["inpWiFiKey"].type = el.isChecked("chbWiFiKeyShow") ? "text" : "password";
  },
  chbStaticAddressConfigClick: function() {
    var el = secNetwork.aElements;
    el.visible("contIPSettings", el.isChecked("chbIPStatic"));
  },
  loadEncryptions: function() {
    var el = secNetwork.aElements;
    if(!el.selWiFiEncryption)
      el.setTitle("selWiFiEncryption", aTexts.network.Encryption);
    if(!el.selWiFiEncryption.options.length)
    {
      var option = el.create("option");
      option.text = aTexts.network.SelectEncryption;
      option.disabled = true;
      option.style.display = "none";
      el.selWiFiEncryption.add(option);
      el.selWiFiEncryption.selectedIndex = 0;
    }
    secNetwork.populateEncryptions(el["selWiFiEncryption"]);
  },
  loadStaticIP: function() {
    var el = secNetwork.aElements;
    var iel = secNetwork.aIPElements;
    el.add("contIPSettings");
    for(var i = 0; i < iel.length; i++)
    {
      var input = el.create("input");
      el[iel[i].id] = input;
      input.id = iel[i].id;
      input.className = "form-control";
      input.type = "text";
      input.placeholder = iel[i].hint;
      input.title = iel[i].title;
      el["contIPSettings"].appendChild(el.create("br"));
      el["contIPSettings"].appendChild(input);
    }
  },
  updateDisconnectedMessage: function(ssid) {
    if(!ssid)
      return;

    secNetwork.disconnectedText = aTexts.wizard.ConnectToNetwork.replace(/NETWORK/g, "<b>" + secNetwork.hex2text(ssid) + "</b>");
    setTimeout(function() { secNetwork.disconnectedText = null; }, 5000);
  },
  connectTo: function(obj) {
    var el = secNetwork.aElements;

    if(secNetwork._connection === "ap")
      secNetwork.updateDisconnectedMessage(obj.wireless_ssid);

    spin.invokeButtonAction({
      elements: el.add([
        "chbWiFiManual",     "selWiFiNetwork",
        "btnWiFiRefresh",    "inpWiFiManualName",
        "selWiFiEncryption", "inpWiFiKey",
        "chbWiFiKeyShow",
        "chbIPStatic",       "inpIPAddress",
        "inpIPSubnet",       "inpIPGateway",
        "inpIPPrimaryDNS",   "inpIPSecondaryDNS",
        "btnNetworkSave",
      ]),
      container: el.add("contBtnNetworkSave"),
      action: smoip.setNetwork,
      params: [ obj ],
    });
  },
  checkStaticAddresses: function(elm, netData) {
    netData.dhcp = false;

    var address = elm.getValue("inpIPAddress");
    var addressMatch = secNetwork.checkIPv4Address(address);
    if(!addressMatch)
      return "inpIPAddress";
    netData.address = address;

    var mask = elm.getValue("inpIPSubnet");
    var maskMatch = secNetwork.checkIPv4Address(mask);
    var prefix = maskMatch ? secNetwork.mask2prefix(maskMatch) : -1;
    if(prefix == -1)
      return "inpIPSubnet";
    netData.prefix = prefix;

    var gateway = elm.getValue("inpIPGateway");
    var gatewayMatch = secNetwork.checkIPv4Gateway(gateway, addressMatch, maskMatch);
    if(!gatewayMatch)
      return "inpIPGateway";
    netData.gateway = gateway;

    var priDNS = elm.getValue("inpIPPrimaryDNS");
    var priDNSMatch = secNetwork.checkIPv4Address(priDNS);
    if(!priDNSMatch)
      return "inpIPPrimaryDNS";
    netData.dns = [ priDNS ];

    var secDNS = elm.getValue("inpIPSecondaryDNS");
    if(secDNS.length)
    {
      var secDNSMatch = secNetwork.checkIPv4Address(secDNS);
      if(!secDNSMatch)
        return "inpIPSecondaryDNS";
      netData.dns.push(secDNS);
    }

    return null;
  },
  btnSaveClick: function() {
    var el = secNetwork.aElements;
    var newNetworkData = { };
    var wifiKeyPopupData = null;
    if(el.isChecked("chbWiFiManual"))
    {
      var manualName = el.getValue("inpWiFiManualName");
      if(!manualName.length)
      {
        popup.showError({
          text: aTexts.network.NetworkNameNotEntered,
          callbackOK: function() {
            el.focus("inpWiFiManualName");
          },
        });
        return;
      }
      newNetworkData.wireless_ssid = secNetwork.text2hex(manualName);
      var encryption = secNetwork.getSelectedEncryption();
      if(!encryption)
      {
        popup.showError({
          text: aTexts.network.EncryptionNotSelected,
          callbackOK: function() {
            el.focus("selWiFiEncryption");
          },
        });
        return;
      }
      newNetworkData.wireless_encryption = encryption.type[0];
      var key = el.getValue("inpWiFiKey");
      if(!key.length && encryption.error)
      {
        popup.showError({
          text: encryption.error,
          callbackOK: function() {
            el.focus("inpWiFiKey");
          },
        });
        return;
      }
      newNetworkData.wireless_key = key;
    }
    else
    {
      var net = secNetwork.getSelectedNetwork();
      if(net)
      {
        var encryption = secNetwork.getEncryptionByType(net.encryption);
        if(!encryption)
        {
          popup.showError({
            text: "Unexpected error!",
          });
          return;
        }
        var key = el.getValue("inpWiFiKey");
        if(!key.length && encryption.q)
        {
          wifiKeyPopupData = {
            title: encryption.q.title,
            text: encryption.q.text,
            withContinue: true,
          };
        }
        newNetworkData.wireless_ssid = net.ssid;
        newNetworkData.wireless_encryption = net.encryption;
        if(key.length)
          newNetworkData.wireless_key = key;
      }
    }
    if(el.isChecked("chbIPStatic"))
    {
      var err = secNetwork.checkStaticAddresses(el, newNetworkData);
      if(err)
      {
        var iel = secNetwork.getIPElementByID(err);
        popup.showError({
          text: iel.error,
          callbackOK: function() {
            el.focus(err);
          },
        });
        return;
      }
    }
    else
    {
      newNetworkData.dhcp = true;
    }

    if(wifiKeyPopupData)
    {
      wifiKeyPopupData.callbackYes = function() {
        secNetwork.connectTo(newNetworkData);
      };
      popup.showYesNo(wifiKeyPopupData);
      return;
    }

    secNetwork.connectTo(newNetworkData);
  },
  init: function() {
    var el = secNetwork.aElements;
    var txt = aTexts.network;
    var obj = {
      "valNetworkHeader": txt.NetworkSettings,
      "chbValWiFiManual": txt.ConfigureManually,
      "chbValIPStatic":   txt.StaticIPConfig,
      "btnWiFiRefresh":   txt.Refresh,
      "btnNetworkSave":   aTexts.Save,
    };
    for(var key in obj)
      el.setInnerHTML(key, obj[key]);

    secNetwork.loadEncryptions();
    secNetwork.loadNetworks();
    secNetwork.updateNetworks(null);
    secNetwork.loadStaticIP();

    secProduct.connectModelCallback(function(model) {
      el.setValue("valNetworkDesc", aTexts.network.SetupYourProduct.replace(/PRODUCT/g, model.name));
    });
  },
};

var secPower = {
  aElements: Object.create(element),
  aStandbyModes: {
    "ECO_MODE": {
      name: aTexts.power.ECOMode,
    },
    "NETWORK": {
      name: aTexts.power.NetworkStandby,
    }
  },
  aAutoPowerDownItems: [ ],
  loadStandbyMode: function() {
    var el = secPower.aElements;
    el.setTitle("selStandbyMode", aTexts.power.StandbyMode);
    if(!el["selStandbyMode"].options.length)
    {
      var option = el.create("option");
      option.disabled = true;
      option.style.display = "none";
      option.text = aTexts.power.StandbyMode;
      el["selStandbyMode"].add(option);
      el["selStandbyMode"].selectedIndex = 0;
    }
  },
  updateStandbyModeItems: function(obj) {
    if(obj.readonly || !obj.enum)
      return;

    var el = secPower.aElements;
    var idx = el["selStandbyMode"].options.length;

    for(var i = 0; i < obj.enum.length; i++)
    {
      var key = obj.enum[i];
      if(secPower.aStandbyModes[key]) {
        secPower.aStandbyModes[key]._index = idx++;
        var option = el.create("option");
        option.text = secPower.aStandbyModes[obj.enum[i]].name;
        el["selStandbyMode"].add(option);
      }
    }

    el.show("contPowerSettings");
  },
  updateStandbyMode: function(mode) {
    var el = secPower.aElements;
    if(secPower.aStandbyModes[mode])
      el["selStandbyMode"].selectedIndex = secPower.aStandbyModes[mode]._index;
  },
  loadAutoPowerDown: function() {
    var el = secPower.aElements;
    el.setTitle("selAutoPowerDown", aTexts.power.AutoPowerDown);
    if(!el["selAutoPowerDown"].options.length)
    {
      var option = el.create("option");
      option.disabled = true;
      option.style.display = "none";
      option.text = aTexts.power.AutoPowerDown;
      el["selAutoPowerDown"].add(option);
      el["selAutoPowerDown"].selectedIndex = 0;
    }
  },
  updateAutoPowerDownItems: function(obj) {
    if(obj.readonly || !obj.maximum || (obj.maximum % 60))
      return;

    var el = secPower.aElements;
    var idx = el["selAutoPowerDown"].options.length;

    var max = obj.maximum / 60;
    for(var i = 0; i <= max; i += 5)
    {
      var txt;
      if(!i)
      {
        txt = aTexts.power.AutoPowerDownOff;
      }
      else
      {
        txt = "0" + ((i >= 60) ? Math.floor(i / 60) : 0) + ":";
        var tmp = i % 60;
        txt += (tmp < 10) ? ("0" + tmp) : tmp;
      }
      secPower.aAutoPowerDownItems.push({
        _index: idx++,
        name: txt,
        key: i * 60,
      });

      var option = el.create("option");
      option.text = txt;
      el["selAutoPowerDown"].add(option);
    }
    el.show("contPowerSettings");
  },
  updateAutoPowerDown: function(value) {
    if(value % 300)
      return;

    var el = secPower.aElements;

    for(var i = 0; i < secPower.aAutoPowerDownItems.length; i++)
      if(secPower.aAutoPowerDownItems[i].key == value)
      {
        el["selAutoPowerDown"].selectedIndex = secPower.aAutoPowerDownItems[i]._index;
        break;
      }
  },
  btnSaveClick: function() {
    var el = secPower.aElements;

    var mode = null;
    var modeIdx = el["selStandbyMode"].selectedIndex;
    for(var key in secPower.aStandbyModes)
      if(secPower.aStandbyModes[key]._index == modeIdx)
      {
        mode = key;
        break;
      }

    var apd = -1;
    var apdIdx = el["selAutoPowerDown"].selectedIndex;
    for(var i = 0; i < secPower.aAutoPowerDownItems.length; i++)
      if(secPower.aAutoPowerDownItems[i]._index == apdIdx)
      {
        apd = secPower.aAutoPowerDownItems[i].key;
        break;
      }

    spin.invokeButtonAction({
      elements: el.add([ "btnPowerSave", "selStandbyMode", "selAutoPowerDown" ]),
      container: el.add("contBtnPowerSave"),
      action: smoip.setStandbyModeAndAPD,
      params: [ mode, apd ],
    });
  },
  init: function() {
    var el = secPower.aElements;
    var txt = aTexts.power;
    var obj = {
      "valPowerHeader": txt.PowerSettings,
      "btnPowerSave":   aTexts.Save,
    };
    for(var key in obj)
      el.setInnerHTML(key, obj[key]);

    secPower.loadStandbyMode();
    secPower.loadAutoPowerDown();
  },
};

var secVolume = {
  aElements: Object.create(element),
  _availSources: { },
  _updateDescription: function() {
    var el = secVolume.aElements;
    var id = "DescriptionLimit";
    if(secVolume._model == "Edge NQ")
      id += "Edge";
    el.setValue("valVolumeLimit", aTexts.volume["VolumeLimit"]);
    el.setValue("valVolumeLimitDesc", aTexts.volume[id]);
  },
  updateVolumeLimitValues: function(obj) {
    if(obj.readonly || (obj.minimum === undefined) || (obj.maximum === undefined) || (obj.minimum >= obj.maximum))
      return;

    var el = secVolume.aElements;
    el.show("contVolumeSettings");
  },
  _updateLimitSlider: function(value) {
    var el = secVolume.aElements;
    var width = el.add("rngVolumeLimit").clientWidth - 20;
    var text = value + "%";
    var left = (width * value / 100) + "px";

    if(el.getValue("rngVolumeLimit") != value)
      el.setValue("rngVolumeLimit", value);

    if(!el["hiddenDiv"])
    {
      el["hiddenDiv"] = element.create("div");
      el.styles("hiddenDiv", {
        "display": "inline-block",
        "visibility": "hidden",
        "width": "auto",
      });
      el.add("body").appendChild(el["hiddenDiv"]);
    }
    el.setInnerHTML("hiddenDiv", text);
    width = el["hiddenDiv"].clientWidth;

    element.setPseudoStyles("contRngVolumeLimit", "before", {
      "content": "'" + text + "'",
      "left": left,
      "margin-left": (-width / 2 + 5) + "px",
    });
    element.setPseudoStyles("contRngVolumeLimit", "after", {
      "left": left,
    });
  },
  updateVolumeLimitChange: function(limit) {
    secVolume._updateLimitSlider(limit);
  },
  rngLimitChange: function() {
    var el = secVolume.aElements;
    var value = el.getValue("rngVolumeLimit");
    if(secVolume._currentLimitValue != value)
    {
      secVolume._currentLimitValue = value;
      secVolume._updateLimitSlider(value);
    }
  },
  btnSaveClick: function() {
    var el = secVolume.aElements;

    spin.invokeButtonAction({
      elements: el.add([ "rngVolumeLimit", "btnVolumeSave" ]),
      container: el.add("contBtnVolumeSave"),
      action: smoip.setVolumeLimit,
      params: [ parseInt(el.getValue("rngVolumeLimit")) ],
    });
  },
  init: function() {
    var el = secVolume.aElements;
    var txt = aTexts.volume;
    var obj = {
      "valVolumeHeader": txt.VolumeSettings,
      "btnVolumeSave":   aTexts.Save,
    };
    for(var key in obj)
      el.setInnerHTML(key, obj[key]);

    secVolume._updateLimitSlider(0);

    secProduct.connectModelCallback(function(model) {
      secVolume._model = model.name;
      secVolume._updateDescription();
    });
    secProduct.connectSourceAvailCallback(function(sources) {
      secVolume._availSources = sources;
      secVolume._updateDescription();
    });
  },
};

var secTimezone = {
  aElements: Object.create(element),
  updateTimezone: function(timezone) {
    if(!Timezones || !Timezones.length)
      return;

    var el = secTimezone.aElements;
    if(el["selTimezoneTimezone"].offset === undefined)
    {
      el["selTimezoneTimezone"].offset = el["selTimezoneTimezone"].options.length;
      for(var i = 0; i < Timezones.length; i++)
      {
        var tz = Timezones[i];
        var gmt = tz.offset;
        var txt = "(GMT";
        if(gmt < 0)
        {
          txt += "-";
          gmt = -gmt;
        }
        else
          txt += "+";
        var hrs = (gmt / 60) | 0;
        if(hrs < 10)
          txt += "0";
        txt += hrs + ":";
        var mins = gmt % 60;
        if(mins < 10)
          txt += "0";
        txt += mins + ") " + tz.zone.replace(/_/g, " ");

        var option = el.create("option");
        option.text = txt;
        el["selTimezoneTimezone"].add(option);

      }
    }
    for(var i = 0; i < Timezones.length; i++)
      if(timezone === Timezones[i].zone)
      {
        el["selTimezoneTimezone"].selectedIndex = el["selTimezoneTimezone"].offset + i;
        break;
      }

    el.show("contTimezone");
  },
  btnSaveClick: function() {
    var el = secTimezone.aElements;
    var idx = el["selTimezoneTimezone"].selectedIndex - el["selTimezoneTimezone"].offset;

    spin.invokeButtonAction({
      elements: el.add([ "selTimezoneTimezone", "btnTimezoneSave" ]),
      container: el.add("contBtnTimezoneSave"),
      action: smoip.setTimezone,
      params: [ Timezones[idx].zone ],
    });
  },
  init: function() {
    var el = secTimezone.aElements;
    var txt = aTexts.timezone;
    var obj = {
      "valTimezoneHeader": txt.Timezone,
      "btnTimezoneSave":   aTexts.Save,
    };
    for(var key in obj)
      el.setInnerHTML(key, obj[key]);

    el.setTitle("selTimezoneTimezone", txt.Timezone);
    var option = el.create("option");
    option.disabled = true;
    option.style.display = "none";
    option.text = txt.SelectTimezone;
    el["selTimezoneTimezone"].add(option);
    el["selTimezoneTimezone"].selectedIndex = 0;
  },
};

var secFirmware = {
  aElements: Object.create(element),
  isUpdating: false,
  wsOpen: false,
  _reloadPage: function() {
    newHTTPRequest().sendGet("", null).onReadyDone = function(status, response) {
      if(status == 200)
      {
        popup.updateMessage({ text: aTexts.Reloading, }, true);
        setTimeout(function() { window.location.reload(true); }, 3000);
      }
      else
      {
        setTimeout(function() { secFirmware._reloadPage(); }, 1000);
      }
    };
  },
  updateVersions: function(obj) {
    var el = secFirmware.aElements;
    for(var i = 0; i < obj.length; i++)
    {
      if(!obj[i].version)
        continue;

      if(obj[i].component == "service-pack")
      {
        el.setValue("valCurrentVersion", obj[i].version);
        continue;
      }
      if(obj[i].component == "MCU")
      {
        el.setValue("valMCUVersion", obj[i].version);
        continue;
      }
      if(obj[i].component == "cast")
      {
        el.visible("contFirmwareCast", true);
        el.setValue("valCastVersion", obj[i].version);
        continue;
      }
    }
  },
  updateUnitID: function(unitID) {
    var el = secFirmware.aElements;
    el.setValue("valUnitID", unitID);
  },
  updateEarlyUpdate: function(value) {
    var el = secFirmware.aElements;
    el.check("chbFirmwareEarlyUpdate", value);
  },
  updateAvailableUpdate: function(value) {
    var el = secFirmware.aElements;
    secFirmware._isNewAvailable = value;
    if(value)
    {
      el.setValue("valFirmwareAvailable", aTexts.firmware.NewFirmwareAvailable);
      el.setInnerHTML("btnFirmwareCheck", aTexts.firmware.Update);
    }
    else
    {
      el.setValue("valFirmwareAvailable", aTexts.firmware.NoFirmwareAvailable);
      el.setInnerHTML("btnFirmwareCheck", aTexts.firmware.Check);
    }
    el.show("contFirmwareCheck");
  },
  updateStart: function() {
    secFirmware.isUpdating = true;
    if(!uui)
    {
      popup.showMessage({
        title: aTexts.firmware.FirmwareUpdate,
        text: aTexts.firmware.Starting,
      });
      uui = new UUI();
      uui.connectCallbacks({
        "onConnectionOpen": function() {
          secFirmware.wsOpen = true;
          popup.updateMessage({ text: aTexts.PleaseWait, }, true);
        },
        "onConnectionClose": function(code, reason) {
          if(secFirmware.wsOpen)
            secFirmware._reloadPage();
          secFirmware.wsOpen = false;
          uui = null;
        },
        "onMessage": function(message) {
          popup.updateMessage({ text: message, }, true);
        },
      });
      uui.start();
    }
  },
  doUpdateIfAvail: function(ret) {
    if(ret)
      setTimeout(function() {
        if(secFirmware._isNewAvailable)
          secFirmware.btnCheckClick();
      });
  },
  btnCheckClick: function() {
    var el = secFirmware.aElements;
    spin.invokeButtonAction({
      elements: el.add([ "chbFirmwareEarlyUpdate", "btnFirmwareCheck" ]),
      container: el.add("contBtnFirmwareCheck"),
      action: secFirmware._isNewAvailable ? smoip.firmwareUpdate : smoip.firmwareCheck,
      params: [ null ],
      callback: !secFirmware._isNewAvailable ? secFirmware.doUpdateIfAvail : null,
    });
  },
  doCheck: function(param) {
    var el = secFirmware.aElements;
    secFirmware._startUpdate = true;
    spin.invokeButtonAction({
      elements: el.add([ "chbFirmwareEarlyUpdate", "btnFirmwareCheck" ]),
      container: el.add("contBtnFirmwareCheck"),
      action: smoip.firmwareCheck,
      params: [ param ],
      callback: secFirmware.doUpdateIfAvail,
    });
  },
  chbEarlyUpdateClick: function() {
    var el = secFirmware.aElements;
    if(el.isChecked("chbFirmwareEarlyUpdate"))
    {
      popup.showOK({
        title: aTexts.firmware.EarlyUpdate,
        text: aTexts.firmware.EarlyNotification,
        callbackOK: function() {
          secFirmware.doCheck(true);
        },
      });
    }
    else
    {
      secFirmware.doCheck(false);
    }
  },
  init: function() {
    var el = secFirmware.aElements;
    var txt = aTexts.firmware;
    var obj = {
      "valFirmwareHeader":            txt.Firmware,
      "valFirmwareHdrCurrentVersion": txt.CurrentVersion,
      "valFirmwareHdrMCUVersion":     txt.MCUVersion,
      "valFirmwareHdrUnitID":         txt.UnitID,
      "valFirmwareHdrCastVersion":    aTexts.cast.Version,
      "chbValFirmwareEarlyUpdate":    txt.EarlyUpdate,
      "valFirmwareEarlyDesc":         txt.EarlyDescription,
    };
    for(var key in obj)
      el.setInnerHTML(key, obj[key]);
  },
};

var secCast = {
  aElements: Object.create(element),
  updateCast: function(obj) {
    var el = secCast.aElements;
    switch(obj.cast_setup_state)
    {
      case "not-set-up":
        secCast.needSetup = true;
        el.hide("contCastContent");
        el.show("contCastSetup");
        break;
      case "disabled":
        el.hide("contCastContent");
        el.show("contCastSetup");
        break;
      case "enabled":
        if(secCast._setupShown)
        {
          secCast._setupShown = null;
          popup.hide();
        }
        secCast.needTutorials = !obj.tutorials_seen;
        el.hide("contCastSetup");
        el.show("contCastContent");
        break;
      default:
        el.hide("contCastSetup");
        el.hide("contCastContent");
        return;
    }
    el.check("chbCastShareData", obj.share_usage_data);
  },
  _tutorialsSeen: function(learnMore) {
    var el = secCast.aElements;

    if(learnMore)
      window.open("https://www.google.com/cast/learn/audio/", "_blank");

    spin.invokeButtonAction({
      elements: [ el.add("btnCastSetup"), popup.getYesButton(), popup.getNoButton() ],
      container: el.add("contBtnCastSetup"),
      action: smoip.setCast,
      params: [ { tutorials_seen: true } ],
      callback: popup.hide,
    });
  },
  tutorialText: "",
  updateName: function(name) {
    secCast.tutorialText = aTexts.cast.TutorialDescription.replace(/PRODUCT/g, name);
	},
  startTutorial: function(data) {
    var txt = aTexts.cast;
    var popupData = {
      title: txt.CastTutorial,
      text: secCast.tutorialText,
      buttonYes: txt.LearnMore,
      buttonNo: txt.NoThanks,
    };
    for(var key in data)
      popupData[key] = data[key];
    popup.showYesNo(popupData);
  },
  _acceptTerms: function(accept) {
    var el = secCast.aElements;

    if(secCast._setupShown)
      secCast._setupShown = null;

    var setupCallback = function(ret) {
      if(accept)
        secCast.startTutorial({
          callbackYesNo: secCast._tutorialsSeen,
          keep: true,
        });
      else
        popup.hide();
    };

    spin.invokeButtonAction({
      elements: [ el.add("btnCastSetup"), popup.getYesButton(), popup.getNoButton() ],
      container: el.add("contBtnCastSetup"),
      action: smoip.setCast,
      params: [ { accept_terms: accept } ],
      callback: setupCallback,
    });
  },
  startSetup: function(data) {
    var txt = aTexts.cast;
    var tc = txt.TermsAndConditions;
    tc = tc.replace(/<GOOGLE_TERMS>/g, createHref("https://www.google.com/policies/terms/"));
    tc = tc.replace(/<GOOGLE_PRIVACY>/g, createHref("https://www.google.com/policies/privacy/"));

    secCast._setupShown = true;
    var popupData = {
      title: txt.CastSetup,
      text: tc,
      buttonYes: txt.Accept,
      buttonNo: txt.Decline,
    };
    for(var key in data)
      popupData[key] = data[key];
    popup.showYesNo(popupData);
  },
  btnSetupClick: function() {
    secCast.startSetup({
      callbackYesNo: secCast._acceptTerms,
      keep: true,
    });
  },
  chbShareDataClick: function() {
    var el = secCast.aElements;
    spin.invokeButtonAction({
      elements: [ el.add("chbCastShareData") ],
      action: smoip.setCast,
      params: [ { share_usage_data: el.isChecked("chbCastShareData") } ],
    });
  },
  aHowToCastClick: function() {
    var el = secCast.aElements;
    spin.invokeButtonAction({
      elements: [ el.add("chbCastShareData") ],
      action: smoip.setCast,
      params: [ { tutorials_seen: true } ],
    });
    return true;
  },
  init: function() {
    var el = secCast.aElements;
    var txt = aTexts.cast;

    var obj = {
      "valCastHeader":       txt.Cast,
      "valCastNeedSetup":    txt.NeedSetup,
      "btnCastSetup":        txt.Setup,
      "chbValCastShareData": txt.ShareUsageData,
    };
    for(var key in obj)
      el.setInnerHTML(key, obj[key]);

    var links = [
      { txt: txt.LearnAboutCastPolicy, url: "https://support.google.com/googlecast/answer/6076570" },
      { txt: txt.HowToCast,            url: "https://www.google.com/cast/learn/audio/", onclick: "secCast.aHowToCastClick();" },
      { txt: txt.LearnAboutMultiroom,  url: "https://www.google.com/cast/learn/audio/#multiroom" },
      { txt: txt.EnabledApps,          url: "https://www.google.com/cast/apps?device=audio" },
      { },
      { txt: txt.TermsOfService,       url: "https://www.google.com/policies/terms/" },
      { txt: txt.PrivacyPolicy,        url: "https://www.google.com/policies/privacy/" },
      { txt: txt.OpenSourceLicenses,   url: "https://support.google.com/googlecast/answer/6121012" },
    ];
    var lnk = "";
    for(var i = 0; i < links.length; i++)
      lnk += (links[i].txt && links[i].url)
           ? createLink(links[i]) + "<br/>"
           : "<br/>";

    el.setValue("contCastLinks", lnk);

    secProduct.connectSourceAvailCallback(function(sources) {
      if(sources.cast)
        el.show("contCast");
    });
  },
};

var secServices = {
  aElements: Object.create(element),
  _linkService: function(obj) {
    var el = secServices.aElements;
    var srv = secServices.aServices[obj.idx];
    var title = aTexts.services.LinkService.replace(/SERVICE/g, srv.name);
    var item = el.add("contServicesLink").cloneNode(true);
    el.addChildren(item, [ "inpServicesLinkUsername", "inpServicesLinkPassword" ]);

    var link = function() {
      obj.username = el.getValue("inpServicesLinkUsername");
      obj.password = el.getValue("inpServicesLinkPassword");

      if(!obj.username || !obj.username.length)
      {
        obj.focus = "inpServicesLinkUsername";
        popup.showError({
          text: aTexts.services.UsernameNotEntered,
          keep: true,
          callbackOK: function() { secServices._linkService(obj); },
        });
        return;
      }
      if(!obj.password || !obj.password.length)
      {
        obj.focus = "inpServicesLinkPassword";
        popup.showError({
          text: aTexts.services.PasswordNotEntered,
          keep: true,
          callbackOK: function() { secServices._linkService(obj); },
        });
        return;
      }

      popup.showMessage({
        title: aTexts.PleaseWait,
        text: aTexts.services.Linking,
      });

      newHTTPRequest().sendGet("service-management", {
        action: "linkService",
        id: secServices.aServices[obj.idx].id,
        username: obj.username,
        password: obj.password,
      }).onReadyDone = function(status, response) {
        var err = aTexts.services.UnableToLink;
        var s = "services: ";
        if(status == 200)
        {
          try {
            var resp = JSON.parse(response);
            if(resp["action"] !== "linkService")
            {
              log.deb(s + "Invalid response: action: " + resp["action"]);
            }
            else if(resp["result"] === "ERROR")
            {
              log.deb(s + "Error: " + resp["message"]);
              if(resp["message"])
                err = resp["message"];
            }
            else if(resp["result"] !== "OK")
            {
              log.deb(s + "Invalid response: result: " + resp["result"]);
            }
            else
            {
              secServices._updateItem(obj.idx, true);
              err = null;
            }
          } catch(e) {
            log.deb(s + "Error: " + e.message);
          }
        }
        if(err)
          popup.showError({
            text: err,
          });
        else
          popup.hide();
      };
    };

    if(!obj.focus)
      obj.focus = "inpServicesLinkUsername";
    if(obj.username)
      el.setValue("inpServicesLinkUsername", obj.username);
    if(obj.password)
      el.setValue("inpServicesLinkPassword", obj.password);

    popup.showYesNo({
      title: title,
      content: item,
      buttonYes: aTexts.OK,
      buttonNo: aTexts.Cancel,
      focus: el[obj.focus],
      keep: true,
      callbackNo: popup.hide,
      callbackYes: link,
    });
  },
  _unlinkService: function(obj) {
    var srv = secServices.aServices[obj.idx];
    var title = aTexts.services.UnlinkService.replace(/SERVICE/g, srv.name);
    var unlink = function() {
      popup.showMessage({
        title: aTexts.PleaseWait,
        text: aTexts.services.Unlinking,
      });

      newHTTPRequest().sendGet("service-management", {
        action: "unlinkService",
        id: secServices.aServices[obj.idx].id,
      }).onReadyDone = function(status, response) {
        var err = aTexts.services.UnableToUnlink;
        var s = "services: ";
        if(status == 200)
        {
          try {
            var resp = JSON.parse(response);
            if(resp["action"] !== "unlinkService")
            {
              log.deb(s + "Invalid response: action: " + resp["action"]);
            }
            else if(resp["result"] === "ERROR")
            {
              log.deb(s + "Error: " + resp["message"]);
              if(resp["message"])
                err = resp["message"];
            }
            else if(resp["result"] !== "OK")
            {
              log.deb(s + "Invalid response: result: " + resp["result"]);
            }
            else
            {
              secServices._updateItem(obj.idx, false);
              err = null;
            }
          } catch(e) {
            log.deb(s + "Error: " + e.message);
          }
        }
        if(err)
          popup.showError({
            text: err,
          });
        else
          popup.hide();
      };
    };
    popup.showYesNo({
      title: title,
      text: aTexts.services.UnlinkInfo,
      focus: aTexts.No,
      withContinue: true,
      callbackYes: unlink,
    });
  },
  btnLinkClick: function(sender) {
    var idx = sender.id.replace(/^.*?(\d+)$/g, "$1");
    var srv = secServices.aServices[idx];
    if(!srv.linked)
      secServices._linkService({ idx: idx });
    else
      secServices._unlinkService({ idx: idx });
  },
  contServiceClick: function(sender) {
    var el = secServices.aElements;
    var id = sender.id.replace(/^.*?(\d+)$/g, "$1");
    var open = !secServices.aServices[id].open;
    for(var key in secServices.aServices)
      if(secServices.aServices[key].open)
      {
        el.styles("contBtnServicesEdit" + key, { "max-height": "0px", });
        secServices.aServices[key].open = false;
      }
    if(open)
    {
      var eID = "contBtnServicesEdit" + id;
      var height = el[eID].scrollHeight;
      el.styles(eID, { "max-height": height + "px", });
      secServices.aServices[id].open = true;
    }
  },
  _updateItem: function(idx, linked) {
    var el = secServices.aElements;
    var txt = aTexts.services;
    if(linked)
    {
      el.setInnerHTML("btnServiceLink" + idx, txt.Unlink);
      var e = el["contServicesItemIn" + idx];
      var c = e.className;
      c = c.replace(/ service-unlinked/g, "");
      c += " service-linked";
      e.className = c;
    }
    else
    {
      el.setInnerHTML("btnServiceLink" + idx, txt.Link);
      var e = el["contServicesItemIn" + idx];
      var c = e.className;
      c = c.replace(/ service-linked/g, "");
      c += " service-unlinked";
      e.className = c;
    }
  },
  load: function(cb) {
    newHTTPRequest().sendGet("service-management", {
      action: "listServices",
    }).onReadyDone = function(status, response) {
      var el = secServices.aElements;
      var ret = false;
      var s = "services: ";
      if(status == 200)
      {
        try {
          var resp = JSON.parse(response);
          if(resp["action"] !== "listServices")
          {
            log.deb(s + "Invalid response: action: " + resp["action"]);
          }
          else if(resp["result"] === "ERROR")
          {
            log.deb(s + "Error: " + resp["message"]);
          }
          else if(resp["result"] !== "OK")
          {
            log.deb(s + "Invalid response: result: " + resp["result"]);
          }
          else
          {
            secServices.aServices = resp["services"];
            var l = secServices.aServices.length;
            if(l)
              el.show("contServices");
            for(var i = 0; i < l; i++)
            {
              var srv = secServices.aServices[i];

              srv.open = false;

              var item = el.add("contServicesItem").cloneNode(true);
              el.addChildrenS(item, i, [
                "contServicesItemIn",
                "contServicesValues",
                "valServicesLogo",
                "contBtnServicesEdit",
                "btnServiceLink",
              ]);

              var id_logo = "valServicesLogo" + i;
              if(srv["logo"])
              {
                el.styles(id_logo, { backgroundImage: "url(\"" + srv["logo"] + "\")" });
                el.setValue(id_logo, "&nbsp;");
              }
              else
              {
                el.setValue(id_logo, srv["name"]);
              }
              el.setTitle(id_logo, srv["name"]);
              secServices._updateItem(i, srv["linked"]);

              item.id += i;
              item.style.display = "block";
              el.add("contServicesItems").appendChild(item);
            }
            ret = true;
          }
        } catch(e) {
        }
      }
      if(cb)
        cb(ret);
    };
  },
  init: function() {
    var el = secServices.aElements;
    var txt = aTexts.services;
    var obj = {
      "valServicesHeader": txt.Services,
    };
    for(var key in obj)
      el.setInnerHTML(key, obj[key]);
    var obj = {
      "inpServicesLinkUsername": txt.EnterUsername,
      "inpServicesLinkPassword": txt.EnterPassword,
    };
    for(var key in obj)
      el.setPlaceholder(key, obj[key]);
  },
};

var secPodcasts = {
  aElements: Object.create(element),
  aPodcasts: { },
  _podcastCount: 0,
  _removeItem: function(idx) {
    var el = secPodcasts.aElements;
    el.add("contPodcastsItems").removeChild(element.getByID("contPodcastsItem" + idx));
    delete secPodcasts.aPodcasts[idx];
  },
  _addItem: function(obj) {
    var el = secPodcasts.aElements;

    obj.open = false;
    var idx = ++secPodcasts._podcastCount;
    secPodcasts.aPodcasts[idx] = obj;

    var item = el.add("contPodcastsItem").cloneNode(true);
    el.addChildrenS(item, idx, [
      "contPodcastsValues",
      "valPodcastsID",
      "valPodcastsName",
      "contBtnPodcastsEdit",
      "valPodcastsURL",
      "btnPodcastsRemove",
    ]);

    el.setValue("valPodcastsID" + idx, idx + ".");
    el.setValue("valPodcastsName" + idx, obj.name);
    el.setValue("valPodcastsURL" + idx, obj.url);

    item.id += idx;
    item.style.display = "block";
    el.add("contPodcastsItems").appendChild(item);
  },
  _addPodcast: function(obj) {
    var el = secPodcasts.aElements;
    var item = el.add("contPodcastsNewPodcast").cloneNode(true);
    el.addChildren(item, [ "inpPodcastsNewName", "inpPodcastsNewURL" ]);

    if(!obj)
      obj = { };

    var add = function() {
      obj.name = el.getValue("inpPodcastsNewName");
      obj.url = el.getValue("inpPodcastsNewURL");

      if(!obj.name || !obj.name.length)
      {
        obj.focus = "inpPodcastsNewName";
        popup.showError({
          text: aTexts.podcasts.NameNotEntered,
          keep: true,
          callbackOK: function() { secPodcasts._addPodcast(obj); },
        });
        return;
      }
      if(!obj.url || !obj.url.length)
      {
        obj.focus = "inpPodcastsNewURL";
        popup.showError({
          text: aTexts.podcasts.AddressNotEntered,
          keep: true,
          callbackOK: function() { secPodcasts._addPodcast(obj); },
        });
        return;
      }

      popup.showMessage({
        title: aTexts.PleaseWait,
        text: aTexts.podcasts.Adding,
      });

      newHTTPRequest().sendGet("service-management", {
        action: "addPodcast",
        name: obj.name,
        url: obj.url,
      }).onReadyDone = function(status, response) {
        var err = aTexts.podcasts.UnableToAdd;
        var s = "podcasts: ";
        if(status == 200)
        {
          try {
            var resp = JSON.parse(response);
            if(resp["action"] !== "addPodcast")
            {
              log.deb(s + "Invalid response: action: " + resp["action"]);
            }
            else if(resp["result"] === "ERROR")
            {
              log.deb(s + "Error: " + resp["message"]);
              if(resp["message"])
                err = resp["message"];
            }
            else if(resp["result"] !== "OK")
            {
              log.deb(s + "Invalid response: result: " + resp["result"]);
            }
            else
            {
              obj.id = resp["id"];
              secPodcasts._addItem(obj);
              err = null;
            }
          } catch(e) {
            log.deb(s + "Error: " + e.message);
          }
        }
        if(err)
          popup.showError({
            text: err,
          });
        else
          popup.hide();
      };
    };

    if(!obj.focus)
      obj.focus = "inpPodcastsNewName";
    if(obj.name)
      el.setValue("inpPodcastsNewName", obj.name);
    if(obj.url)
      el.setValue("inpPodcastsNewURL", obj.url);

    popup.showYesNo({
      title: aTexts.podcasts.AddNewPodcast,
      content: item,
      buttonYes: aTexts.OK,
      buttonNo: aTexts.Cancel,
      focus: el[obj.focus],
      keep: true,
      callbackNo: popup.hide,
      callbackYes: add,
    });
  },
  btnRemoveClick: function(sender) {
    var id = sender.id.replace(/^.*?(\d+)$/g, "$1");

    var remove = function() {
      popup.showMessage({
        title: aTexts.PleaseWait,
        text: aTexts.podcasts.Removing,
      });

      newHTTPRequest().sendGet("service-management", {
        action: "deletePodcast",
        id: secPodcasts.aPodcasts[id].id,
      }).onReadyDone = function(status, response) {
        var err = aTexts.podcasts.UnableToRemove;
        var s = "podcasts: ";
        if(status == 200)
        {
          try {
            var resp = JSON.parse(response);
            if(resp["action"] !== "deletePodcast")
            {
              log.deb(s + "Invalid response action: " + resp["action"]);
            }
            else if(resp["result"] === "ERROR")
            {
              log.deb(s + "Error: " + resp["message"]);
              if(resp["message"])
                err = resp["message"];
            }
            else if(resp["result"] !== "OK")
            {
              log.deb(s + "Invalid response: result: " + resp["result"]);
            }
            else
            {
              secPodcasts._removeItem(id);
              err = null;
            }
          } catch(e) {
            log.deb(s + "Error: " + e.message);
          }
        }
        if(err)
          popup.showError({
            text: err,
          });
        else
          popup.hide();
      };
    };

    popup.showYesNo({
      title: aTexts.podcasts.RemovePodcast,
      text: aTexts.podcasts.RemoveInfo,
      focus: aTexts.No,
      withContinue: true,
      callbackYes: remove,
    });
  },
  contPodcastClick: function(sender) {
    var el = secPodcasts.aElements;
    var id = sender.id.replace(/^.*?(\d+)$/g, "$1");
    var open = !secPodcasts.aPodcasts[id].open;
    for(var key in secPodcasts.aPodcasts)
      if(secPodcasts.aPodcasts[key].open)
      {
        el.styles("contBtnPodcastsEdit" + key, { "max-height": "0px" });
        secPodcasts.aPodcasts[key].open = false;
      }
    if(open)
    {
      var eID = "contBtnPodcastsEdit" + id;
      var height = el.add(eID).scrollHeight;
      el.styles(eID, { "max-height": height + "px", });
      secPodcasts.aPodcasts[id].open = true;
    }
  },
  btnAddNewClick: function() {
    secPodcasts._addPodcast(null);
  },
  load: function(cb) {
    newHTTPRequest().sendGet("service-management", {
      action: "listPodcasts",
    }).onReadyDone = function(status, response) {
      var el = secPodcasts.aElements;
      var ret = false;
      var s = "podcasts: ";
      if(status == 200)
      {
        try {
          var resp = JSON.parse(response);
          if(resp["action"] !== "listPodcasts")
          {
            log.deb(s + "Invalid response: action: " + resp["action"]);
          }
          else if(resp["result"] === "ERROR")
          {
            log.deb(s + "Error: " + resp["message"]);
          }
          else if(resp["result"] !== "OK")
          {
            log.deb(s + "Invalid response: result: " + resp["result"]);
          }
          else
          {
            el.show("contPodcasts");
            var p = resp["podcasts"];
            for(var i = 0; i < p.length; i++)
            {
              secPodcasts._addItem(p[i]);
            }
            ret = true;
          }
        } catch(e) {
        }
      }
      if(cb)
        cb(ret);
    };
  },
  init: function() {
    var el = secPodcasts.aElements;
    var txt = aTexts.podcasts;
    var obj = {
      "valPodcastsHeader": txt.Podcasts,
      "btnPodcastsRemove": txt.Remove,
      "btnPodcastsAddNew": txt.AddNewPodcast,
    };
    for(var key in obj)
      el.setInnerHTML(key, obj[key]);
    var obj = {
      "inpPodcastsNewName": txt.EnterPodcastName,
      "inpPodcastsNewURL":  txt.EnterPodcastAddress,
    };
    for(var key in obj)
      el.setPlaceholder(key, obj[key]);
  },
};

var secPresets = {
  aElements: Object.create(element),
  aPresetList: { },
  aEditOpen: { },
  maxValue: 0,
  _updateElementsID: function(el, add) {
    if(el.id)
      el.id += add;
    for(var u = el.children.length; u--; )
      secPresets._updateElementsID(el.children[u], add);
  },
  _getControlButtons: function() {
    var el = secPresets.aElements;
    var toDisable = [ ];
    for(var i = 1; i <= secPresets.maxValue; i++)
    {
      toDisable.push(el.add("btnPresetsRename" + i));
      toDisable.push(el.add("btnPresetsRemove" + i));
      toDisable.push(el.add("btnPresetsPlay" + i));
    }
    toDisable.push(el.add("btnPresetsAddNew"));
    return toDisable;
  },
  updateMaxValue: function(max) {
    if(secPresets.maxValue != 0)
      return;

    secPresets.maxValue = max;
    var el = secPresets.aElements;
    el.add("contPresetsItems");
    el.add("selPresetsNewID");
    var template = element.getByID("contPresetsItem");
    for(var i = 1; i <= secPresets.maxValue; i++)
    {
      var item = template.cloneNode(true);
      secPresets._updateElementsID(item, i);
      el["contPresetsItems"].appendChild(item);

      var option = el.create("option");
      option.text = i;
      el["selPresetsNewID"].add(option);

      secPresets.aEditOpen[i] = false;
    }
    for(var i = 1; i <= secPresets.maxValue; i++)
      el.setValue("valPresetsID" + i, i + ".");
    el.show("contPresets");
  },
  updateList: function(list) {
    var el = secPresets.aElements;
    secPresets.aPresetList = { };
    if(list)
      for(var i = 0; i < list.length; i++)
      {
        var id = list[i].id;
        if(   (id == null) || !list[i].name
           || (id < 1) || (id > secPresets.maxValue))
        {
          continue;
        }
        el.setValue("valPresetsName" + id, list[i].name);
        secPresets.aPresetList[id] = { name: list[i].name };
        var playid = "btnPresetsPlay" + id;
        if(list[i].is_playing)
        {
          el.setInnerHTML(playid, aTexts.presets.Playing);
          el.enable(playid, false);
        }
        else
        {
          el.setInnerHTML(playid, aTexts.presets.Play);
          el.enable(playid, true);
        }
      }
    for(var i = 1; i <= secPresets.maxValue; i++)
      el.visible("contPresetsItem" + i, secPresets.aPresetList[i]);
  },
  _showNewPresetPopup: function(id, name, address) {
    var el = secPresets.aElements;

    var focus = "selPresetsNewID";
    if(id < 0)
      id = 0;
    else if(!name || !name.length)
      focus = "inpPresetsNewName";
    else if(!address || !address.length)
      focus = "inpPresetsNewAddress";

    var item = el.add("contPresetsNewPreset").cloneNode(true);
    el.addChildren(item, [ "selPresetsNewID", "inpPresetsNewName", "inpPresetsNewAddress" ]);
    el["selPresetsNewID"].selectedIndex = id;
    el.setValue("inpPresetsNewName", name);
    el.setValue("inpPresetsNewAddress", address);

    popup.showYesNo({
      title: aTexts.presets.NewPreset,
      content: item,
      buttonYes: aTexts.OK,
      buttonNo: aTexts.Cancel,
      focus: el[focus],
      keep: true,
      callbackNo: popup.hide,
      callbackYes: secPresets._addNewPreset,
    });
  },
  _addNewPreset: function() {
    var el = secPresets.aElements;
    var params = {
      preset: el["selPresetsNewID"].selectedIndex,
      name: el.getValue("inpPresetsNewName"),
      url: el.getValue("inpPresetsNewAddress"),
    };

    var err = null;
    if(params.preset < 1)
      err = aTexts.presets.InvalidPresetPositionSelected;
    else if(!params.name.length)
      err = aTexts.presets.InvalidPresetNameEntered;
    else if(!params.url.length)
      err = aTexts.presets.InvalidPresetAddressEntered;

    if(err)
    {
      popup.showError({
        text: err,
        callbackOK: function() {
          secPresets._showNewPresetPopup(params.preset, params.name, params.url);
        },
      });
      return;
    }
    popup.hide();
    spin.invokeButtonAction({
      elements: secPresets._getControlButtons(),
      container: el.add("contBtnPresetsAddNew"),
      action: smoip.addPreset,
      params: [ params ],
    });
  },
  btnAddNewClick: function() {
    secPresets._showNewPresetPopup(-1, "", "");
  },
  contPresetClick: function(sender) {
    var el = secPresets.aElements;
    var id = sender.id.replace(/^.*?(\d+)$/g, "$1");
    var open = !secPresets.aEditOpen[id];
    for(var i = 1; i <= secPresets.maxValue; i++)
      if(secPresets.aEditOpen[i])
      {
        el.styles("contBtnPresetsEdit" + i, { "max-height": "0px", });
        secPresets.aEditOpen[i] = false;
      }
    if(open)
    {
      var eID = "contBtnPresetsEdit" + id;
      var height = el.add(eID).scrollHeight;
      el.styles(eID, { "max-height": height + "px", });
      secPresets.aEditOpen[id] = true;
    }
  },
  _showRenamePresetPopup: function(id, name) {
    var el = secPresets.aElements;
    var item = el.add("contPresetsRenamePreset").cloneNode(true);
    el.addChildrenS(item, id, [ "valPresetsRenameID", "inpPresetsRenameName" ]);
    el.setValue("valPresetsRenameID" + id, id + ".");
    el.setValue("inpPresetsRenameName" + id, name);

    popup.showYesNo({
      title: aTexts.presets.RenamePreset,
      content: item,
      buttonYes: aTexts.OK,
      buttonNo: aTexts.Cancel,
      focus: "inpPresetsRenameName" + id,
      keep: true,
      callbackNo: popup.hide,
      callbackYes: function() {
        secPresets._renamePreset(id, el.getValue("inpPresetsRenameName" + id));
      },
    });
  },
  _renamePreset: function(id, name) {
    var el = secPresets.aElements;
    var params = {
      preset: id,
      name: name,
    };

    if(!params.name.length)
    {
      popup.showError({
        text: aTexts.presets.InvalidPresetNameEntered,
        callbackOK: function() {
           secPresets._showRenamePresetPopup(params.id, params.name);
        },
      });
      return;
    }
    popup.hide();
    spin.invokeButtonAction({
      elements: secPresets._getControlButtons(),
      container: el.add("contBtnPresetsAddNew"),
      action: smoip.renamePreset,
      params: [ params ],
    });
  },
  btnRenameClick: function(sender) {
    var id = sender.id.replace(/^.*?(\d+)$/g, "$1");
    secPresets._showRenamePresetPopup(parseInt(id), secPresets.aPresetList[id].name);
  },
  _removePreset: function(id) {
  },
  btnRemoveClick: function(sender) {
    var el = secPresets.aElements;
    var id = sender.id.replace(/^.*?(\d+)$/g, "$1");
    popup.showYesNo({
      title: aTexts.presets.RemovePreset,
      text: aTexts.presets.RemoveInfo.replace(/PRESET_ID/g, "#" + id),
      focus: aTexts.No,
      withContinue: true,
      callbackYes: function() {
        spin.invokeButtonAction({
          elements: secPresets._getControlButtons(),
          container: el.add("contBtnPresetsAddNew"),
          action: smoip.removePreset,
          params: [ parseInt(id) ],
        });
      },
    });
  },
  btnPlayClick: function(sender) {
    var el = secPresets.aElements;
    var id = sender.id.replace(/^.*?(\d+)$/g, "$1");
    spin.invokeButtonAction({
      elements: secPresets._getControlButtons(),
      container: el.add("contBtnPresetsAddNew"),
      action: smoip.playPreset,
      params: [ parseInt(id) ],
    });
  },
  init: function() {
    var el = secPresets.aElements;
    var txt = aTexts.presets;
    var obj = {
      "valPresetsHeader": txt.Presets,
      "btnPresetsRename": txt.Rename,
      "btnPresetsRemove": txt.Remove,
      "btnPresetsPlay": txt.Play,
      "btnPresetsAddNew": txt.AddNewPreset,
    };
    for(var key in obj)
      el.setInnerHTML(key, obj[key]);

    el.setTitle("selPresetsNewID", aTexts.presets.PresetPosition);
    var option = el.create("option");
    option.disabled = true;
    option.style.display = "none";
    option.text = aTexts.presets.SelectPresetPosition;
    el["selPresetsNewID"].add(option);
    el["selPresetsNewID"].selectedIndex = 0;

    el.setPlaceholder("inpPresetsRenameName", aTexts.presets.EnterPresetName);
    el.setTitle("inpPresetsRenameName", aTexts.presets.PresetName);
    el.setPlaceholder("inpPresetsNewName", aTexts.presets.EnterPresetName);
    el.setTitle("inpPresetsNewName", aTexts.presets.PresetName);
    el.setPlaceholder("inpPresetsNewAddress", aTexts.presets.EnterPresetAddress);
    el.setTitle("inpPresetsNewAddress", aTexts.presets.PresetAddress);
  },
};

var wizard = {
  aElements: Object.create(element),
  _getSetupDescription: function(state) {
    var txt = aTexts.wizard;
    var desc = txt.WelcomeDescription + "<br/><br/>";
    var al = "&gt; ";
    var ar = " &lt;";

    if(state == 0)
      desc += al + txt.SetupInternet + ar;
    else
      desc += txt.SetupInternet;
    desc += "<br/>";
    if(state == 1)
      desc += al + txt.FirmwareUpdate + ar;
    else
      desc += txt.FirmwareUpdate;
    desc += "<br/>";
    if(state == 2)
      desc += al + txt.SetupRest + ar;
    else
      desc += txt.SetupRest;

    return desc;
  },
  aTasks: {
    _data: [ ],
    add: function(prio, task) {
      var d = this._data;
      var i = 0;
      for(; i < d.length; i++)
        if(d[i].prio > prio)
          break;
      d.splice(i, 0, { prio: prio, task: task });
    },
    get: function(idx) {
      var d = this._data;
      return (idx < d.length) ? d[idx].task : null;
    },
  },
  aScreens: [
  [
    {
      id: "welcomeWiFi",
      func: function() {
        var txt = aTexts.wizard;
        popup.showYesNo({
          title: txt.Welcome,
          text: wizard._getSetupDescription(0),
          buttonYes: aTexts.Skip,
          buttonNo: aTexts.Continue,
          focus: aTexts.Continue,
          keep: true,
          callbackNo: wizard.next,
          callbackYes: popup.hide,
        });
      },
    },
    {
      id: "wifiNetwork",
      func: function() {
        var el = wizard.aElements;
        var item = el.add("contWizardWiFiNetwork").cloneNode(true);
        el.addChildren(item, [
          "valWizardWiFiNetworkDesc",
          "selWizardWiFiNetwork",
          "contBtnWizardWiFiRefresh",
          "btnWizardWiFiRefresh",
          "chbWizardIPStatic",
          "chbValWizardIPStatic",
        ]);

        var refreshCallback = function(obj) {
          wizard._networks = obj;
          secNetwork.populateNetworks(el["selWizardWiFiNetwork"], wizard._networks);
          var option = el.create("option");
          option.text = "<" + aTexts.network.AddNetwork + ">";
          el["selWizardWiFiNetwork"].add(option);
          el["selWizardWiFiNetwork"].selectedIndex = 0;
        };

        var option = el.create("option");
        option.disabled = true;
        option.style.display = "none";
        el["selWizardWiFiNetwork"].add(option);

        refreshCallback(wizard._networks);

        el.setInnerHTML("btnWizardWiFiRefresh", aTexts.network.Refresh);
        el["btnWizardWiFiRefresh"].onclick = function() {
          spin.invokeButtonAction({
            elements: [
              el["btnWizardWiFiRefresh"], popup.getOKButton()
            ],
            container: el["contBtnWizardWiFiRefresh"],
            action: smoip.refreshWireless,
          });
        };
        wizard._wifiRefreshCallback = refreshCallback;

        el.setValue("chbValWizardIPStatic", aTexts.network.StaticIPConfig);

        var submitTask = function() {
          wizard._wifiRefreshCallback = null;
          wizard._newNetworkData = { };

          var selIndex = el["selWizardWiFiNetwork"].selectedIndex;
          var maxIndex = el["selWizardWiFiNetwork"].options.length - 1;
          if(selIndex == 0)
          {
            popup.showError({
              text: aTexts.network.NetworkNotSelected,
              keep: true,
              callbackOK: wizard.same,
            });
          }
          else
          {
            wizard.aTasks.add(1, {
              info: aTexts.network.NetworkSettings,
              func: function() {
                secNetwork.updateDisconnectedMessage(wizard._newNetworkData.wireless_ssid);
                smoip.setNetwork(wizard._applySetupNext, wizard._newNetworkData);
              },
            });

            if(el.isChecked("chbWizardIPStatic"))
              wizard._unskipScreen("wifiAddresses");
            else
              wizard._newNetworkData.dhcp = true;

            if(selIndex == maxIndex)
            {
              wizard._unskipScreen("wifiEnterName");
            }
            else
            {
              for(var i = 0; i < wizard._networks.available.length; i++)
                if(wizard._networks.available[i]._index == selIndex)
                {
                  var net = wizard._networks.available[i];
                  var data = wizard._newNetworkData;
                  data.wireless_ssid = net.ssid;
                  data.wireless_encryption = net.encryption;
                  break;
                }
              var enc = wizard._newNetworkData ? secNetwork.getEncryptionByType(wizard._newNetworkData.wireless_encryption) : null;
              if(enc && enc.hint)
              {
                wizard._unskipScreen("wifiEnterKey");
              }
            }
            wizard.next();
          }
        };

        popup.showOK({
          title: aTexts.network.NetworkName,
          content: item,
          buttonOK: aTexts.Continue,
          focus: el["selWizardWiFiNetwork"],
          keep: true,
          callbackOK: submitTask,
        });
      },
    },
    {
      id: "wifiEnterName",
      skip: true,
      func: function() {
        var el = wizard.aElements;
        var item = el.add("contWizardWiFiEnterName").cloneNode(true);
        el.addChildren(item, [ "inpWizardWiFiEnterName" ]);

        el.setPlaceholder("inpWizardWiFiEnterName", aTexts.network.NetworkName);

        var submitTask = function() {
          var name = el.getValue("inpWizardWiFiEnterName");
          if(!name || !name.length)
          {
            popup.showError({
              text: aTexts.network.NetworkNameNotEntered,
              keep: true,
              callbackOK: wizard.same,
            });
          }
          else
          {
            wizard._newNetworkData.wireless_ssid = secNetwork.text2hex(name);
            wizard._unskipScreen("wifiEncryption");
            wizard.next();
          }
        };

        popup.showOK({
          title: aTexts.network.NetworkName,
          content: item,
          buttonOK: aTexts.Continue,
          focus: el["inpWizardWiFiEnterName"],
          keep: true,
          callbackOK: submitTask,
        });
      },
    },
    {
      id: "wifiEncryption",
      skip: true,
      func: function() {
        var el = wizard.aElements;
        var item = el.add("contWizardWiFiEncryption").cloneNode(true);
        el.addChildren(item, [ "selWizardWiFiEncryption" ]);

        var option = el.create("option");
        option.disabled = true;
        option.style.display = "none";
        option.text = aTexts.network.SelectEncryption;
        el["selWizardWiFiEncryption"].add(option);
        secNetwork.populateEncryptions(el["selWizardWiFiEncryption"]);
        el["selWizardWiFiEncryption"].selectedIndex = 0;

        var submitTask = function() {
          var idx = el["selWizardWiFiEncryption"].selectedIndex;
          if(idx == 0)
          {
            popup.showError({
              text: aTexts.network.EncryptionNotSelected,
              keep: true,
              callbackOK: wizard.same,
            });
          }
          else
          {
            var enc = secNetwork.getEncryptionByIndex(idx);
            wizard._newNetworkData.wireless_encryption = enc.type[0];
            if(enc.hint)
              wizard._unskipScreen("wifiEnterKey");
            wizard.next();
          }
        };

        popup.showOK({
          title: aTexts.network.Encryption,
          content: item,
          buttonOK: aTexts.Continue,
          focus: el["selWizardWiFiEncryption"],
          keep: true,
          callbackOK: submitTask,
        });
      },
    },
    {
      id: "wifiEnterKey",
      skip: true,
      func: function() {
        var el = wizard.aElements;
        var item = el.add("contWizardWiFiEnterKey").cloneNode(true);
        el.addChildren(item, [ "inpWizardWiFiEnterKey", "chbWizardWiFiShowKey", "chbValWizardWiFiShowKey" ]);

        var enc = secNetwork.getEncryptionByType(wizard._newNetworkData.wireless_encryption);

        el.setPlaceholder("inpWizardWiFiEnterKey", enc.hint);
        el.setValue("chbValWizardWiFiShowKey", enc.show);

        el["chbWizardWiFiShowKey"].onclick = function() {
          el["inpWizardWiFiEnterKey"].type = el.isChecked("chbWizardWiFiShowKey") ? "text" : "password";
        };

        var submitTask = function() {
          var key = el.getValue("inpWizardWiFiEnterKey");
          if(!key || !key.length)
          {
            popup.showError({
              text: enc.error,
              keep: true,
              callbackOK: wizard.same,
            });
          }
          else
          {
            wizard._newNetworkData.wireless_key = key;
            wizard.next();
          }
        };

        popup.showOK({
          title: aTexts.network.Encryption,
          content: item,
          buttonOK: aTexts.Continue,
          keep: true,
          callbackOK: submitTask,
        });
      },
    },
    {
      id: "wifiAddresses",
      skip: true,
      func: function() {
        var el = wizard.aElements;
        var item = el.add("contIPSettings").cloneNode(true);
        var children = [ "inpIPAddress", "inpIPSubnet", "inpIPGateway", "inpIPPrimaryDNS", "inpIPSecondaryDNS" ];
        el.addChildren(item, children);

        if(!wizard._inAddresses)
          wizard._inAddresses = { };

        for(var i = children.length; i--; )
        {
          var child = children[i];
          var value = wizard._inAddresses[child];
          if(!value)
            value = "";
          el.setValue(child, value);
        }

        item.style.display = "initial";

        var submitTask = function() {
          for(var i = children.length; i--; )
          {
            var child = children[i];
            wizard._inAddresses[child] = el.getValue(child);
          }
          var err = secNetwork.checkStaticAddresses(el, wizard._newNetworkData);
          if(err)
          {
            var iel = secNetwork.getIPElementByID(err);
            popup.showError({
              text: iel.error,
              keep: true,
              callbackOK: wizard.same,
            });
            wizard._inAddresses.focus = err;
          }
          else
          {
            wizard.next();
          }
        };

        if(!wizard._inAddresses.focus)
          wizard._inAddresses.focus = "inpIPAddress";

        popup.showOK({
          title: aTexts.wizard.IPAddresses,
          content: item,
          buttonOK: aTexts.Continue,
          focus: el[wizard._inAddresses.focus],
          keep: true,
          callbackOK: submitTask,
        });
      },
    },
  ],
  [
    {
      id: "welcomeFirmware",
      func: function() {
        var txt = aTexts.wizard;

        var task = function() {
          smoip.firmwareUpdate(wizard._applySetupNext);
        };

        popup.showYesNo({
          title: txt.Welcome,
          text: wizard._getSetupDescription(1),
          buttonYes: aTexts.Skip,
          buttonNo: aTexts.Continue,
          focus: aTexts.Continue,
          keep: true,
          callbackNo: function() {
            wizard.aTasks.add(1, {
              info: aTexts.firmware.FirmwareUpdate,
              func: task,
            });
            wizard.aTasks.add(10, {
              info: null,
              func: function() { },
            });
            wizard.next();
          },
          callbackYes: popup.hide,
        });
      },
    },
  ],
  [
    {
      id: "welcomeRest",
      func: function() {
        var txt = aTexts.wizard;
        popup.showYesNo({
          title: txt.Welcome,
          text: wizard._getSetupDescription(2),
          buttonYes: aTexts.Skip,
          buttonNo: aTexts.Continue,
          focus: aTexts.Continue,
          keep: true,
          callbackNo: wizard.next,
          callbackYes: popup.hide,
        });
      },
    },
    {
      id: "productName",
      func: function() {
        var el = wizard.aElements;
        var item = el.add("contWizardName").cloneNode(true);
        el.addChildren(item, [ "valWizardNameDesc", "inpWizardName" ]);
        el.setValue("valWizardNameDesc", aTexts.wizard.RenameDescription);
        el.setValue("inpWizardName", wizard._productName);

        var applyTask = function() {
          if(wizard._newProductName !== wizard._productName) {
            smoip.setProductName(wizard._applySetupNext, wizard._newProductName);
          } else
            wizard._applySetupNext(true);
        };
        var submitTask = function() {
          var value = el.getValue("inpWizardName");
          if(!value || !value.length)
          {
            popup.showError({
              text: aTexts.product.NameNotEntered,
              keep: true,
              callbackOK: wizard.same,
            });
          }
          else
          {
            wizard._newProductName = value;
            wizard.aTasks.add(1, {
              info: aTexts.product.ProductName,
              func: applyTask,
            });
			      secCast.updateName(value);
            wizard.next();
          }
        };

        var txt = aTexts.wizard;
        popup.showOK({
          title: txt.RenameYourUnit,
          content: item,
          buttonOK: aTexts.Continue,
          focus: el["inpWizardName"],
          keep: true,
          callbackOK: submitTask,
        });
      },
    },
    {
      id: "standbyMode",
      skip: true,
      func: function() {
        var el = wizard.aElements;
        var item = el.add("contWizardPower").cloneNode(true);
        el.addChildren(item, [ "chbWizardPowerNetwork" ]);

        var applyTask = function() {
          var newMode = wizard._networkStandby ? "NETWORK" : "ECO_MODE";
          if(wizard._standbyMode !== newMode)
            smoip.setStandbyModeAndAPD(wizard._applySetupNext, newMode, -1);
          else
            wizard._applySetupNext(true);
        };
        var submitTask = function() {
          wizard._networkStandby = el.isChecked("chbWizardPowerNetwork");
          wizard.aTasks.add(1, {
            info: aTexts.power.PowerSettings,
            func: applyTask,
          });
          wizard.next();
        };

        popup.showOK({
          title: aTexts.power.PowerSettings,
          content: item,
          buttonOK: aTexts.Continue,
          focus: el["chbWizardPowerNetwork"],
          keep: true,
          callbackOK: submitTask,
        });
      },
    },
    {
      id: "cast",
      func: function() {
        secCast.startSetup({
          keep: true,
          callbackYesNo: function(accept) {
            if(accept)
              wizard._unskipScreen("castTutorial");
            else
            {
              wizard.aTasks.add(1, {
                info: aTexts.cast.Cast,
                func: function() {
                  smoip.setCast(wizard._applySetupNext, { accept_terms: accept });
                },
              });
            }
            wizard.next();
          },
        });
      },
    },
    {
      id: "castTutorial",
      skip: true,
      func: function() {
        secCast.startTutorial({
          keep: true,
          callbackYesNo: function(learnMore) {
            if(learnMore)
              window.open("https://www.google.com/cast/learn/audio/", "_blank");
            wizard.aTasks.add(1, {
              info: aTexts.cast.Cast,
              func: function() {
                smoip.setCast(wizard._applySetupNext, {
                  accept_terms: true,
                  tutorials_seen: true,
                });
              },
            });
            wizard.next();
          },
        });
      },
    },
  ],
  ],
  _unskipScreen: function(name) {
    for(var i = wizard.aScreens.length; i--; )
      for(var u = wizard.aScreens[i].length; u--; )
        if(wizard.aScreens[i][u].id === name)
        {
          wizard.aScreens[i][u].skip = false;
          break;
        }
  },
  updateName: function(name) {
    wizard._productName = name;
  },
  _setScreens: function() {
    if(wizard._ap)
    {
      log.deb("wizard: Enable Wi-Fi screen");
      wizard._activeScreens = wizard.aScreens[0];
    }
    else if(wizard._fwUpdate)
    {
      log.deb("wizard: Enable Firmware screen");
      wizard._activeScreens = wizard.aScreens[1];
    }
    else
    {
      wizard._activeScreens = wizard.aScreens[2];
    }
  },
  updateConnection: function(conn) {
    if(conn === "ap")
      wizard._ap = true;
    wizard._setScreens();
  },
  updateNetworks: function(obj) {
    if(obj.available)
      wizard._networks = obj;
    if(wizard._wifiRefreshCallback)
      wizard._wifiRefreshCallback(obj);
  },
  updateStandbyModeValues: function(obj) {
    if(!obj.readonly && obj.enum
    && (obj.enum.indexOf("ECO_MODE") >= 0)
    && (obj.enum.indexOf("NETWORK") >= 0))
    {
      log.deb("wizard: Enable standby screen");
      wizard._unskipScreen("standbyMode");
    }
  },
  updateStandbyMode: function(mode) {
    wizard._standbyMode = mode;
  },
  updateAvailableUpdate: function(value) {
    wizard._fwUpdate = value;
    wizard._setScreens();
  },
  _applySetupNext: function(ret) {
    log.fnEntry("wizard._applySetupNext");
    if(!wizard._taskIdx)
    {
      wizard._taskIdx = 0;
      popup.showMessage({
        title: aTexts.wizard.ApplyingSettings,
        text: "",
      });
    }
    var task = wizard.aTasks.get(wizard._taskIdx++);
    if(task)
    {
      if(task.info)
      {
        popup.updateMessage({ text: task.info, }, true);
        log.deb("Setting up " + task.info);
      }
      task.func();
    }
    else
      popup.hide();
    log.fnExit();
  },
  _showContent: function(idx) {
    if(idx < wizard._activeScreens.length)
    {
      var obj = wizard._activeScreens[idx];
      log.deb("wizard: #" + idx + " " + obj.id + (obj.skip ? " (skipped)" : ""));
      if(obj.skip)
        wizard.next();
      else
        obj.func();
      return;
    }
    wizard._applySetupNext(true);
  },
  same: function() {
    wizard._showContent(wizard._index);
  },
  next: function() {
    wizard._showContent(++wizard._index);
  },
  start: function() {
    wizard._showContent(wizard._index = 0);
  },
  init: function() {
    var el = wizard.aElements;
    var txt = aTexts.wizard;
    el.setValue("chbValWizardPowerNetwork", txt.NetworkStandby);

    secProduct.connectModelCallback(function(model) {
      txt.WelcomeDescription = txt.WelcomeDescription.replace(/PRODUCT/g, model.name);
      txt.RenameYourUnit = txt.RenameYourUnit.replace(/PRODUCT/g, model.name);
      txt.RenameDescription = txt.RenameDescription.replace(/PRODUCT/g, model.name);
    });
  },
};

var spin = {
  opt_button: {
    lines: 13,            // The number of lines to draw
    length: 7,//28,           // The length of each line
    width: 2,//14,            // The line thickness
    radius: 2,//42,           // The radius of the inner circle
    scale: 1,             // Scales overall size of the spinner
    corners: 1,           // Corner roundness (0..1)
    color: '#555555',     // #rgb or #rrggbb or array of colors
    opacity: 0.05,        // Opacity of the lines
    rotate: 0,            // The rotation offset
    direction: 1,         // 1: clockwise, -1: counterclockwise
    speed: 0.6,           // Rounds per second
    trail: 50,            // Afterglow percentage
    fps: 20,              // Frames per second when using setTimeout() as a fallback for CSS
    zIndex: 0,//2e9,          // The z-index (defaults to 2000000000)
    className: 'spinner', // The CSS class to assign to the spinner
    top: '17px',          // Top position relative to parent
    left: '15px',         // Left position relative to parent
    shadow: false,        // Whether to render a shadow
    hwaccel: false,       // Whether to use hardware acceleration
    position: 'relative', // Element positioning
  },
  getByButton: function(container) {
    return new Spinner(spin.opt_button).spin(container);
  },
  remove: function(handle) {
    handle.stop();
  },
  invokeButtonAction: function(params) {
    var el = [ ];
    var elements = params.elements;
    if(elements)
      for(var i = 0; i < elements.length; i++)
        if(!elements[i].disabled)
          el.push(elements[i]);
    element.disableArray(el);
    var container = params.container;
    var s = container ? spin.getByButton(container) : null;
    var args = [
      function(ret) {
        if(s)
          spin.remove(s);
        element.enableArray(el);
        if(params.callback)
          params.callback(ret);
      },
    ];
    if(params.params)
      args = args.concat(params.params);
    params.action.apply(this, args);
  },
};

function smoipConnectionClose(code, reason) {
  if(secFirmware.isUpdating)
    return;

  if(reason === "System power down")
  {
    popup.showMessage({
      title: aTexts.Disconnected,
      text: aTexts.UnitTurnedOff,
    });
  }
  else if(secNetwork.disconnectedText)
  {
    popup.showMessage({
      title: aTexts.Disconnected,
      text: secNetwork.disconnectedText,
    });
  }
  else
  {
    popup.showOK({
      title: aTexts.Disconnected,
      text: aTexts.ConnectionLost + "<br/>" + aTexts.TryAndReloadPage,
      buttonOK: aTexts.Reload,
      keep: true,
      callbackSpinOK: function(callback) {
        newHTTPRequest().sendGet("", null).onReadyDone = function(status, response) {
          var ok = status == 200;
          callback(ok);
          if(ok)
          {
            popup.hide();
            popup.showMessage({
              title: aTexts.PleaseWait,
              text: aTexts.Reloading,
            });
            setTimeout(function() { window.location.reload(); }, 3000);
          }
        };
      },
    });
  }
}

function bodyOnLoad() {
  aTexts.init();

  popup.showMessage({
    title: aTexts.PleaseWait,
    text: aTexts.Loading + "...",
  });

  // secStatus.init();
  // secProduct.init();
  // secNetwork.init();
  // secPower.init();
  // secVolume.init();
  // secTimezone.init();
  // secCast.init();
  // secFirmware.init();
  // secServices.init();
  // secPodcasts.init();
  secPresets.init();
  // wizard.init();

  var init0 = function() {
    popup.updateMessage({
      text: aTexts.Done,
    }, true);

    var func;
    if(secCast.needSetup)
    {
      func = wizard.start;
    }
    else if(secCast.needTutorials)
    {
      func = function() {
        secCast.startTutorial({
          callbackYesNo: secCast._tutorialsSeen,
        });
      };
    }
    else
    {
      func = popup.hide;
      // Allow jumping to the CCBI section
      var link = window.location.href;
      if(link.match(/[\?\&]cast/))
        element.getByID("contCast").scrollIntoView();
    }
    setTimeout(func, 800);
  };
  var initDone = function() {
    setTimeout(init0, 200);
  };
  var initPodcasts = function() {
    secPodcasts.load(function(ret) {
      if(ret)
        log.deb("Poadcasts loaded");
      initDone();
    });
  };
  var initServices = function() {
    secServices.load(function(ret) {
      if(ret)
        log.deb("Services loaded");
      initPodcasts();
    });
  };
  var initProgress = function(p, message) {
    log.deb(message + " loaded");
    if(!p)
      initServices();
  };

  smoip = new SMoIP();
  smoip.connectCallbacks({
    "onConnectionClose":       smoipConnectionClose,
    "onInfoModel":             secProduct.updateModel,
    "onInfoName":              [ wizard.updateName, secProduct.updateName, secCast.updateName, ],
    "onInfoVersions":          secFirmware.updateVersions,
    "onInfoUnitID":            secFirmware.updateUnitID,
    "onInfoTimezone":          secTimezone.updateTimezone,
    "onNetworkConnection":     [
      wizard.updateConnection,
      secStatus.updateConnection,
      secNetwork.updateConnection,
    ],
    "onNetworkIPInfo":         [ secStatus.updateIPAddress, secNetwork.updateIPInfo, ],
    "onNetworkWireless":       [
      wizard.updateNetworks,
      secStatus.updateCurrentNetwork,
      secNetwork.updateNetworks,
    ],
    "onStandbyModeValues":     [ wizard.updateStandbyModeValues, secPower.updateStandbyModeItems, ],
    "onStandbyModeChange":     [ wizard.updateStandbyMode, secPower.updateStandbyMode, ],
    "onStandbyAPDValues":      secPower.updateAutoPowerDownItems,
    "onStandbyAPDChange":      secPower.updateAutoPowerDown,
    "onSourceValues":          [
      secProduct.updateSources,
      secSource.updateSourceItems,
    ],
    "onSourceCast":            secCast.updateCast,
    "onPSMetadataChange":      secSource.updatePSMetadata,
    "onSourceChange":          secSource.updateSource,
    "onVolumeLimitValues":     secVolume.updateVolumeLimitValues,
    "onVolumeLimitChange":     secVolume.updateVolumeLimitChange,
    "onUpdateEarlyChange":     secFirmware.updateEarlyUpdate,
    "onUpdateAvailableChange": [ wizard.updateAvailableUpdate, secFirmware.updateAvailableUpdate ],
    "onUpdateStart":           secFirmware.updateStart,
    "onPresetsMaxValue":       secPresets.updateMaxValue,
    "onPresetsList":           secPresets.updateList,
    "onStartProgress":         initProgress,
  });
  smoip.start();
}

