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

if __name__ == "__main__":
    def ref_network_WLAN():
        wlan = WLAN()
        wlan.init(WLAN.AP, ssid=str())
        wlan.init(auth=(None, str()))
        wlan.init(auth=(WLAN.WEP, str()))
        
        wlan.deinit()

        wlan.connect(str(), auth=(None, str()), bssid=b"\0\0\0\0\0\0", timeout=int())
        wlan.connect(str(), auth=(WLAN.WEP, str()), bssid=b"\0\0\0\0\0\0", timeout=int())

        wifis = wlan.scan()
        for wifi in wifis:
            (ssid, bssid, sec, channel, rssi) = wifi

        wlan.disconnect()
        b = wlan.isconnected()

        (ip, subnet_mask, gateway, dns_server) = wlan.ifconfig()
        wlan.ifconfig(config=(str(), str(), str(), str()))

        m = wlan.mode()
        wlan.mode(int())

        ssid = wlan.ssid()
        wlan.ssid(str())

        auth = wlan.auth()
        wlan.auth(int())

        ch = wlan.channel()
        wlan.channel(int())

        ant = wlan.antenna()
        wlan.antenna(int())

        mac = wlan.mac()

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

if __name__ == "__main__":
    def ref_network_Server():
        svr = Server(int())
        svr.init()
        svr.deinit()
        t = svr.timeout()
        svr.timeout(int())
        b = svr.isrunning()