"""utime – time related functions
The utime module provides functions for getting the current time and date, measuring time intervals, and for delays.

Time Epoch: Pycom’s ESP32 port uses standard for POSIX systems epoch of 1970-01-01 00:00:00 UTC.

Maintaining actual calendar date/time: This requires a Real Time Clock (RTC). On systems with underlying OS (including some RTOS), an RTC may be implicit. Setting and maintaining actual calendar time is responsibility of OS/RTOS and is done outside of MicroPython, it just uses OS API to query date/time. On baremetal ports however system time depends on machine.RTC() object. The current calendar time may be set using machine.RTC().datetime(tuple) function, and maintained by following means:
    - By a backup battery (which may be an additional, optional component for a particular board).
    - Using networked time protocol (requires setup by a port/user).
    - Set manually by a user on each power-up (many boards then maintain RTC time across hard resets, though some may require setting it again in such case).

If actual calendar time is not maintained with a system/MicroPython RTC, functions below which require reference to current absolute time may behave not as expected.
"""

from time import gmtime, localtime, mktime, sleep, time, timezone

def sleep_ms(ms):
    """Delay for given number of milliseconds, should be positive or 0."""
    pass
def sleep_us(us):
    """Delay for given number of microseconds, should be positive or 0"""
    pass
def ticks_ms():
    """Returns uptime, in milliseconds."""
    return int()
def ticks_us():
    """Just like ticks_ms above, but in microseconds."""
    return int()
def ticks_cpu():
    """Similar to ticks_ms and ticks_us, but with higher resolution (25 ns)."""
    return int()
def ticks_diff(old, new):
    """Measure period between consecutive calls to ticks_ms(), ticks_us(), or ticks_cpu(). The value returned by these functions may wrap around at any time, so directly subtracting them is not supported. ticks_diff() should be used instead. “old” value should actually precede “new” value in time, or result is undefined. This function should not be used to measure arbitrarily long periods of time (because ticks_*() functions wrap around and usually would have short period). The expected usage pattern is implementing event polling with timeout:
    # Wait for GPIO pin to be asserted, but at most 500us
    start = time.ticks_us()
    while pin.value() == 0:
        if time.ticks_diff(start, time.ticks_us()) > 500:
            raise TimeoutError
    """
    return int()