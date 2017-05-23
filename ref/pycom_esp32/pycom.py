# https://docs.pycom.io/pycom_esp32/library/pycom.html
"""pycom – Pycom boards specific features
The pycom module contains functions to control specific features of the pycom boards, such as the heartbeat RGB LED.
"""

def heartbeat():
    """Get the state (enabled or disabled) of the heartbeat LED. Returns boolean values (True or False)."""
    return bool()
def heartbeat(enable):
    """Set the state (enabled or disabled) of the heartbeat LED. Returns boolean values (True or False)."""
    pass

def rgbled(color):
    """Set the color of the RGB LED. The color is specified as 24 bit value represeting red, green and blue, where the red color is represented by the 8 most significant bits. For instance, passign the value 0x00FF00 will light up the LED in a very bright green."""
    pass

if __name__ == "__main__":
    def ref_pycom():
        hb = heartbeat()
        heartbeat(bool())
        rgbled(int())