"""uos – basic “operating system” services
The uos module contains functions for filesystem access and urandom function.

Port specifics
    The filesystem has / as the root directory and the available physical drives are accessible
    from here. They are currently:
        /flash – the internal flash filesystem
        /sd – the SD card (if it exists)
"""
from os import *

def dupterm(stream_object):
    """Duplicate the terminal (the REPL) on the passed stream-like object.
The given object must at least implement the .read() and .write() methods.
    """
    return stream_object
