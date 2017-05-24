# ref.: https://docs.pycom.io/pycom_esp32/library/micropython.html
"""micropython – access and control MicroPython internals"""

# Functions - https://docs.pycom.io/pycom_esp32/library/micropython.html#functions
def alloc_emergency_exception_buf(size):
    """Allocate size bytes of RAM for the emergency exception buffer (a good size is around 100 bytes). The buffer is used to create exceptions in cases when normal RAM allocation would fail (eg within an interrupt handler) and therefore give useful traceback information in these situations.
A good way to use this function is to put it at the start of your main script (eg boot.py or main.py) and then the emergency exception buffer will be active for all the code following it.
    """
    pass
