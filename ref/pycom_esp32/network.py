# https://docs.pycom.io/pycom_esp32/library/network.html
"""network — network configuration
This module provides network drivers and routing configuration. Network drivers for specific hardware are available within this module and are used to configure a hardware network interface.
"""

# https://docs.pycom.io/pycom_esp32/library/network.WLAN.html
class WLAN(object):
    """class WLAN
This class provides a driver for the WiFi network processor in the module. Example usage:
    import network
    import time
    # setup as a station
    wlan = network.WLAN(mode=network.WLAN.STA)
    wlan.connect('your-ssid', auth=(network.WLAN.WPA2, 'your-key'))
    while not wlan.isconnected():
        time.sleep_ms(50)
    print(wlan.ifconfig())

    # now use socket as usual
    ...
    """
    def __init__(self, id=0, **kwargs):
        """Create a WLAN object, and optionally configure it. See init for params of configuration.
Note: The WLAN constructor is special in the sense that if no arguments besides the id are given, it will return the already existing WLAN instance without re-configuring it. This is because WLAN is a system feature of the WiPy. If the already existing instance is not initialized it will do the same as the other constructors an will initialize it with default values.
        """
        super().__init__(id=id, **kwargs)
        self.init(**kwargs)
    def init(self, mode, *, ssid=None, auth=None, channel=1, antenna=WLAN.INT_ANT, power_save=False):
        """Set or get the WiFi network processor configuration.
Arguments are:
    - mode can be either WLAN.STA, WLAN.AP or WLAN.STA_AP.
    - ssid is a string with the ssid name. Only needed when mode is WLAN.AP.
    - auth is a tuple with (sec, key). Security can be None, WLAN.WEP, WLAN.WPA or WLAN.WPA2. The key is a string with the network password. If sec is WLAN.WEP the key must be a string representing hexadecimal values (e.g. ‘ABC1DE45BF’). Only needed when mode is WLAN.AP.
    - channel a number in the range 1-11. Only needed when mode is WLAN.AP.
    - antenna selects between the internal and the external antenna. Can be either WLAN.INT_ANT or WLAN.EXT_ANT.
    - power_save enables or disables power save functions in STA mode.

For example, you can do:
    # create and configure as an access point
    wlan.init(mode=WLAN.AP, ssid='wipy-wlan', auth=(WLAN.WPA2,'www.wipy.io'), channel=7, antenna=WLAN.INT_ANT)
or:
    # configure as an station
    wlan.init(mode=WLAN.STA)
        """
        pass
    def deinit(self):
        """Disables the WiFi radio."""
        pass
    def connect(self, ssid, *, auth=None, bssid=None, timeout=None):
        """Connect to a wifi access point using the given SSID, and other security parameters.
    - auth is a tuple with (sec, key). Security can be None, WLAN.WEP, WLAN.WPA or WLAN.WPA2. The key is a string with the network password. If sec is WLAN.WEP the key must be a string representing hexadecimal values (e.g. ‘ABC1DE45BF’).
    - bssid is the MAC address of the AP to connect to. Useful when there are several APs with the same ssid.
    - timeout is the maximum time in milliseconds to wait for the connection to succeed.
        """
        pass
    def scan(self):
        """Performs a network scan and returns a list of named tuples with (ssid, bssid, sec, channel, rssi). Note that channel is always None since this info is not provided by the WiPy."""
        return [(str(), bytes(), int(), int(), int())]
    def disconnect(self):
        """Disconnect from the wifi access point."""
        pass
    def isconnected(self):
        """In case of STA mode, returns True if connected to a wifi access point and has a valid IP address. In AP mode returns True when a station is connected, False otherwise."""
        return bool()
    def ifconfig(self, id=0):
        """When id is 0, the configuration will be get/set on the Station interface. When id is 1 the configuration will be done for the AP interface.
With no parameters given returns a 4-tuple of (ip, subnet_mask, gateway, DNS_server).
        """
        return (str(), str(), str(), str())
    def ifconfig(self, id=0, config="dhcp"):
        """When id is 0, the configuration will be get/set on the Station interface. When id is 1 the configuration will be done for the AP interface.

if 'dhcp' is passed as a parameter then the DHCP client is enabled and the IP params are negotiated with the AP.

If the 4-tuple config is given then a static IP is configured. For instance:
    wlan.ifconfig(config=('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
        """
        pass
    def mode(self):
        """Get the WLAN mode."""
        return int()
    def mode(self, mode):
        """Set the WLAN mode."""
        pass
    def ssid(self):
        """Get the SSID when in AP mode."""
        return str()
    def ssid(self, ssid):
        """Set the SSID when in AP mode."""
        pass
    def auth(self):
        """Get the authentication type when in AP mode."""
        return int()
    def auth(self, auth):
        """Set the authentication type when in AP mode."""
        pass
    def channel(self):
        """Get the channel (only applicanle in AP mode)."""
        return int()
    def channel(self, channel):
        """Set the channel (only applicanle in AP mode)."""
        pass
    def antenna(self):
        """Get the antenna type (external or internal)."""
        return int()
    def antenna(self):
        """Set the antenna type (external or internal)."""
        pass
    def mac(self):
        """Get a 6-byte long bytes object with the WiFi MAC address."""
        return b"\0\0\0\0\0\0"

    STA=1
    AP=2
    STA_AP=3

    WEP=1
    WPA=2
    WPA2=3

    INT_ANT=0
    INT_ANT=1

# https://docs.pycom.io/pycom_esp32/library/network.Server.html
class Server(object):
    """class Server
The Server class controls the behaviour and the configuration of the FTP and telnet services running on the WiPy. Any changes performed using this class’ methods will affect both.

Example:
    import network
    server = network.Server()
    server.deinit() # disable the server
    # enable the server again with new settings
    server.init(login=('user', 'password'), timeout=600)
    """
    def __init__(self, id, **kwargs):
        """Create a server instance, see init for parameters of initialization."""
        super().__init__(id=id, **kwargs)
        self.init(**kwargs)
    def init(self, *, login=('micro', 'python'), timeout=300):
        """Init (and effectively start the server). Optionally a new user, password and timeout (in seconds) can be passed."""
        pass
    def deinit(self):
        """Stop the server"""
        pass
    def timeout(self):
        """Get the server timeout."""
        return int()
    def timeout(self, timeout_in_seconds):
        """Set the server timeout."""
        pass
    def isrunning(self):
        """Returns True if the server is running (connected or accepting connections), False otherwise."""
        return bool()

# https://docs.pycom.io/pycom_esp32/library/network.LoRa.html
class LoRa(object):
    """class LoRa
This class provides a driver for the LoRa network processor in the LoPy. Below is an example demonstrating LoRaWAN Activation by Personalisation usage:
    from network import LoRa
    import socket
    import binascii
    import struct

    # Initialize LoRa in LORAWAN mode.
    lora = LoRa(mode=LoRa.LORAWAN)

    # create an ABP authentication params
    dev_addr = struct.unpack(">l", binascii.unhexlify('00 00 00 05'.replace(' ','')))[0]
    nwk_swkey = binascii.unhexlify('2B 7E 15 16 28 AE D2 A6 AB F7 15 88 09 CF 4F 3C'.replace(' ',''))
    app_swkey = binascii.unhexlify('2B 7E 15 16 28 AE D2 A6 AB F7 15 88 09 CF 4F 3C'.replace(' ',''))

    # join a network using ABP (Activation By Personalization)
    lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))

    # create a LoRa socket
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

    # set the LoRaWAN data rate
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

    # make the socket non-blocking
    s.setblocking(False)

    # send some data
    s.send(bytes([0x01, 0x02, 0x03]))

    # get any data received...
    data = s.recv(64)
    print(data)

Warning: Please ensure that there is an antenna connected to your device before sending/receiving LoRa messages as inproper use (e.g. without an antenna), may damage the device.
    """
    def __init__(self, id=0, **kwargs):
        """Create and configure a LoRa object. See init for params of configuration.
    lora = LoRa(mode=LoRa.LORAWAN)
        """
        super().__init__(id=id, **kwargs)
        self.init(**kwargs)
    def init(self, mode, *, frequency=868000000, tx_power=14, bandwidth=LoRa.BW_125KHZ, sf=7, preamble=8, coding_rate=LoRa.CODING_4_5, power_mode=LoRa.ALWAYS_ON, tx_iq=false, rx_iq=false, adr=false, public=true, tx_retries=1):
        """This method is used to set the LoRa subsystem configuration and to specific raw LoRa or LoRaWAN.
The arguments are:
    - mode can be either LoRa.LORA or LoRa.LORAWAN.
    - frequency accepts values between 863000000 and 870000000 in the 868 band, or between 902000000 and 928000000 in the 915 band.
    - tx_power is the transmit power in dBm. It accepts between 2 and 14 for the 868 band, and between 5 and 20 in the 915 band.
    - bandwidth is the channel bandwidth in KHz. In the 868 band the accepted values are LoRa.BW_125KHZ and LoRa.BW_250KHZ. In the 915 band the accepted values are LoRa.BW_125KHZ and LoRa.BW_500KHZ.
    - sf sets the desired spreading factor. Accepts values between 7 and 12.
    - preamble configures the number of pre-amble symbols. The default value is 8.
    - coding_rate can take the following values: LoRa.CODING_4_5, LoRa.CODING_4_6, LoRa.CODING_4_7 or LoRa.CODING_4_8.
    - power_mode can be either LoRa.ALWAYS_ON, LoRa.TX_ONLY or LoRa.SLEEP. In ALWAYS_ON mode, the radio is always listening for incoming packets whenever a transmission is not taking place. In TX_ONLY the radio goes to sleep as soon as the transmission completes. In SLEEP mode the radio is sent to sleep permanently and won’t accept any commands until the power mode is changed.
    - tx_iq enables TX IQ inversion.
    - rx_iq enables RX IQ inversion.
    - adr enables Adaptive Data Rate.
    - public selects between the public and private sync word.
    - tx_retries sets the number of TX retries in LoRa.LORAWAN mode.

Note: In LoRa.LORAWAN mode, only adr, public and tx_retries are used. All the other params will be ignored as they are handled by the LoRaWAN stack directly. On the other hand, in LoRa.LORA mode from those 3 arguments, only the public one is important in order to program the sync word. In LoRa.LORA mode adr and tx_retries are ignored since they are only relevant to the LoRaWAN stack.

For example, you can do:
    # initialize in raw LoRa mode
    lora.init(mode=LoRa.LORA, tx_power=14, sf=12)
or:
    # initialize in LoRaWAN mode
    lora.init(mode=LoRa.LORAWAN)
        """
        pass
    def join(self, activation, auth, *, timeout=None):
        """Join a LoRaWAN network. The parameters are:
    - activation: can be either LoRa.OTAA or LoRa.ABP.
    - auth: is a tuple with the authentication data.

In the case of LoRa.OTAA the authentication tuple is: (app_eui, app_key). Example:
    from network import LoRa
    import socket
    import time
    import binascii

    # Initialize LoRa in LORAWAN mode.
    lora = LoRa(mode=LoRa.LORAWAN)

    # create an OTAA authentication parameters
    app_eui = binascii.unhexlify('AD A4 DA E3 AC 12 67 6B'.replace(' ',''))
    app_key = binascii.unhexlify('11 B0 28 2A 18 9B 75 B0 B4 D2 D8 C7 FA 38 54 8B'.replace(' ',''))

    # join a network using OTAA (Over the Air Activation)
    lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

    # wait until the module has joined the network
    while not lora.has_joined():
        time.sleep(2.5)
        print('Not yet joined...')

In the case of LoRa.ABP the authentication tuple is: (dev_addr, nwk_swkey, app_swkey). Example:
    from network import LoRa
    import socket
    import binascii
    import struct

    # Initialize LoRa in LORAWAN mode.
    lora = LoRa(mode=LoRa.LORAWAN)

    # create an ABP authentication params
    dev_addr = struct.unpack(">l", binascii.unhexlify('00 00 00 05'.replace(' ','')))[0]
    nwk_swkey = binascii.unhexlify('2B 7E 15 16 28 AE D2 A6 AB F7 15 88 09 CF 4F 3C'.replace(' ',''))
    app_swkey = binascii.unhexlify('2B 7E 15 16 28 AE D2 A6 AB F7 15 88 09 CF 4F 3C'.replace(' ',''))

    # join a network using ABP (Activation By Personalization)
    lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))
        """
        pass
    def bandwidth(self):
        """Gets the bandwidth in raw LoRa mode (LoRa.LORA). Can be either LoRa.BW_125KHZ (0), LoRa.BW_250KHZ (1) or LoRa.BW_500KHZ (2).:
    # get raw LoRa Bandwidth
    lora.bandwidth()
        """
        return int()
    def bandwidth(self, bandwidth):
        """Sets the bandwidth in raw LoRa mode (LoRa.LORA). Can be either LoRa.BW_125KHZ (0), LoRa.BW_250KHZ (1) or LoRa.BW_500KHZ (2).:
    # set raw LoRa Bandwidth
    lora.bandwidth(LoRa.BW_125KHZ)
        """
        pass
    def frequency(self):
        """Get the frequency in raw LoRa mode (LoRa.LORA). The allowed range is between 863000000 and 870000000 Hz for the 868 MHz band version or between 902000000 and 928000000 Hz for the 915 MHz band version.:
    # get raw LoRa Frequency
    lora.frequency()
        """
        return int()
    def frequency(self, frequency):
        """Set the frequency in raw LoRa mode (LoRa.LORA). The allowed range is between 863000000 and 870000000 Hz for the 868 MHz band version or between 902000000 and 928000000 Hz for the 915 MHz band version.:
    # set raw LoRa Frequency
    lora.frequency(868000000)
        """
        pass
    def coding_rate(self):
        """Get the coding rate in raw LoRa mode (LoRa.LORA). The allowed values are: LoRa.CODING_4_5 (0), LoRa.CODING_4_6 (1), LoRa.CODING_4_7 (2) and LoRa.CODING_4_8 (3).
    # get raw LoRa Coding Rate
    lora.coding_rate()
        """
        return int()
    def coding_rate(self, coding_rate):
        """Set the coding rate in raw LoRa mode (LoRa.LORA). The allowed values are: LoRa.CODING_4_5 (0), LoRa.CODING_4_6 (1), LoRa.CODING_4_7 (2) and LoRa.CODING_4_8 (3).
    # set raw LoRa Coding Rate
    lora.coding_rate(LoRa.CODING_4_5)
        """
        pass
    def preamble(self):
        """Get the number of preamble symbols in raw LoRa mode (LoRa.LORA).:
    # get raw LoRa preamble symbols
    lora.preamble()
        """
        return int()
    def preamble(self, preamble):
        """Set the number of preamble symbols in raw LoRa mode (LoRa.LORA).:
    # set raw LoRa preamble symbols
    lora.preamble(LoRa.CODING_4_5)
        """
        pass
    def sf(self):
        """Get the spreading factor value in raw LoRa mode (LoRa.LORA). The minimmum value is 7 and the maximum is 12.:
    # get raw LoRa spread factor value
    lora.sf()
        """
        return int()
    def sf(self, sf):
        """Set the spreading factor value in raw LoRa mode (LoRa.LORA). The minimmum value is 7 and the maximum is 12.:
    # set raw LoRa spread factor value
    lora.sf(7)
        """
        pass
    def power_mode(self):
        """Get the power mode in raw LoRa mode (LoRa.LORA). The accepted values are: LoRa.ALWAYS_ON, LoRa.TX_ONLY and LoRa.SLEEP.:"""
        return int()
    def power_mode(self, power_mode):
        """Set the power mode in raw LoRa mode (LoRa.LORA). The accepted values are: LoRa.ALWAYS_ON, LoRa.TX_ONLY and LoRa.SLEEP.:"""
        pass
    def stats(self):
        """Return a named tuple with usefel information from the last received LoRa or LoRaWAN packet. The named tuple has the following form:
    (timestamp, rssi, snr, sf)

    Example:
        lora.stats()

Where: 
    - timestamp is an internat timestamp with microseconds presicion.
    - rssi hold the received signal strength in dBm.
    - snr contains the signal to noise ratio id dB.
    - sf tells the spreading factor of the packet received.
        """
        return (int(), int(), int(), int())
    def has_joined(self):
        """Returns True if a LoRaWAN network has been joined. False otherwise.:
    lora.has_joined()
        """
        return bool()
    def add_channel(self, index, *, frequency, dr_min, dr_max):
        """Add a LoRaWAN channel on the specified index. If there’s already a channel with that index it will be replaced with the new one.
The arguments are:
    - index: Index of the channel to add. Accepts values between 0 and 15 for EU and between 0 and 71 for US.
    - frequency: Center frequency in Hz of the channel.
    - dr_min: Minimum data rate of the channel (0-7).
    - dr_max: Maximum data rate of the channel (0-7).

Examples:
    lora.add_channel(index=0, frequency=868000000, dr_min=5, dr_max=6)
        """
        pass
    def remove_channel(self, index):
        """Removes the channel from the specified index. On the 868MHz band the channels 0 to 2 cannot be removed, they can only be replaced by other channels using the lora.add_channel method. A way to remove all channels except for one is to add the same channel, 3 times on indexes 0, 1 and 2. An example can be seen below:
    lora.remove_channel()
On the 915MHz band there are no restrictions around this.
        """
        pass
    def mac(self):
        """Returns a byte object with the 8-Byte MAC address of the LoRa radio.:
    lora.mac()
        """
        return b"\0\0\0\0\0\0\0\0"
    def callback(self, trigger, handler=None, arg=None):
        """Specify a callback handler for the LoRa radio. The trigger types are LoRa.RX_PACKET_EVENT and LoRa.TX_PACKET_EVENT
An example of how this callback functions can be seen the in method lora.events().
        """
        if handler is not None: handler(self if arg is None else arg)
        pass
    def events(self):
        """This method returns a value with bits sets (if any) indicating the events that have triggered the callback. Please note that by calling this function the internal events registry is cleared automatically, therefore calling it immediately for a second time will most likely return a value of 0.
Example:
    def lora_cb(lora):
        events = lora.events()
        if events & LoRa.RX_PACKET_EVENT:
            print('Lora packet received')
        if events & LoRa.TX_PACKET_EVENT:
            print('Lora packet sent')

    lora.callback(trigger=(LoRa.RX_PACKET_EVENT | LoRa.TX_PACKET_EVENT), handler=lora_cb)
        """
        pass
    
    # LoRa mode
    LORA=int()
    LORAWAN=int()

    # LoRaWAN join procedure
    OTAA=int()
    ABP=int()

    # Raw LoRa power mode
    ALWAYS_ON=int()
    TX_ONLY=int()
    SLEEP=int()

    # Raw LoRa bandwidth
    BW_125KHZ=int()
    BW_250KHZ=int()
    BW_500KHZ=int()

    # Raw LoRa coding rate
    CODING_4_5=int()
    CODING_4_6=int()
    CODING_4_7=int()
    CODING_4_8=int()

    # Callback trigger types (may be ORed)
    RX_PACKET_EVENT=int()
    TX_PACKET_EVENT=int()
