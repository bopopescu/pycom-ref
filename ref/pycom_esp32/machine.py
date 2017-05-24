# https://docs.pycom.io/pycom_esp32/library/machine.html
""" machine - functions related to the board

The machine module contains specific functions to the board."""

#
# Reset related functions -
# https://docs.pycom.io/pycom_esp32/library/machine.html#reset-related-functions
#
def reset():
    """Resets the device in a manner similar to pushing the external RESET button."""
    pass

def reset_cause():
    """Get the reset cause. See constants for the possible return values."""
    return int()

#
# Interrupt related functions -
# https://docs.pycom.io/pycom_esp32/library/machine.html#interrupt-related-functions
#
def disable_irq():
    """Disable interrupt requests. Returns and integer representing the previous IRQ state. This return value can be passed to enable_irq to restore the IRQ to its original state."""
    return int()

def enable_irq():
    """Enable interrupt requests. The most common use of this function is to pass the value returned by disable_irq to exit a critical section. Another options is to enable all interrupts which can be achieved by calling the function with no parameters."""
    pass
def enable_irq(state):
    """Enable interrupt requests. The most common use of this function is to pass the value returned by disable_irq to exit a critical section. Another options is to enable all interrupts which can be achieved by calling the function with no parameters."""
    pass

#
# Power related functions -
# https://docs.pycom.io/pycom_esp32/library/machine.html#power-related-functions
#
def freq():
    """Returns CPU frequency in hertz."""
    return int()

def idle():
    """Gates the clock to the CPU, useful to reduce power consumption at any time during short or long periods. Peripherals continue working and execution resumes as soon as any interrupt is triggered (on many ports this includes system timer interrupt occurring at regular intervals on the order of millisecond)."""
    pass

def deepsleep():
    """Stops the CPU and all peripherals (including networking interfaces, if any). Execution is resumed from the main script, just as with a reset. If a value in milliseconds is given then the device will wake up after that period of time, otherwise it will remain in deep sleep until the reset button is pressed."""
    pass
def deepsleep(time_ms):
    """Stops the CPU and all peripherals (including networking interfaces, if any). Execution is resumed from the main script, just as with a reset. If a value in milliseconds is given then the device will wake up after that period of time, otherwise it will remain in deep sleep until the reset button is pressed."""
    pass

#
# Miscellaneous functions -
# https://docs.pycom.io/pycom_esp32/library/machine.html#miscellaneous-functions
#
def main(filename):
    """Set the filename of the main script to run after boot.py is finished. If this function is not called then the default file main.py will be executed.

It only makes sense to call this function from within boot.py."""
    pass

def rng():
    """Return a 24-bit software generated random number."""
    return int()

def unique_id():
    """Returns a byte string with a unique identifier of a board/SoC. It will vary from a board/SoC instance to another, if underlying hardware allows. Length varies by hardware (so use substring of a full value if you expect a short ID). In some MicroPython ports, ID corresponds to the network MAC address.

Hint: use binascii.hexlify() to convert the byte string to the much used hexadecimal form."""
    return bytes()

#
# Constants - https://docs.pycom.io/pycom_esp32/library/machine.html#constants
#

# reset causes
PWRON_RESET=0
HARD_RESET=1
WDT_RESET=2
DEEPSLEEP_RESET=3
SOFT_RESET=4
BROWN_OUT_RESET=5

# https://docs.pycom.io/pycom_esp32/library/machine.ADC.html
class ADC(object):
    """class ADC – analog to digital conversion"""

    # Constructors -
    # https://docs.pycom.io/pycom_esp32/library/machine.ADC.html#constructors
    def __init__(self, id=0):
        """Create an ADC object, that will let you associate a channel with a pin. For more info check the hardware section."""
        super().__init__(id)
        self.init(id)

    # Methods -
    # https://docs.pycom.io/pycom_esp32/library/machine.ADC.html#methods
    def init(self, *, bits=12):
        """Enable the ADC block. This method is automatically called on object creation.
    - bits can take values between 9 and 12 and selects the number of bits of resolution of the ADC block."""
        pass

    def deinit(self):
        """Disable the ADC block."""
        pass

    def channel(self, *, pin, attn=ADC.ATTN_0DB):
        """Create an analog pin.
    - pin is a keyword-only string argument. Valid pins are ‘P13’ to ‘P20’.
    - attn is the attenuation level. The supported values are: ADC.ATTN_0DB, ADC.ATTN_2_5DB, ADC.ATTN_6DB, ADC.ATTN_11DB"""
        return ADCChannel()

    ATTN_0DB=0
    ATTN_2_5DB=1
    ATTN_6DB=2
    ATTN_11DB=3

class ADCChannel(object):
    """class ADCChannel — read analog values from internal or external sources
ADC channels can be connected to internal points of the MCU or to GPIO pins. ADC channels are created using the ADC.channel method.

Warning: ADC pin input range is 0-1.1V. This maximum value can be increased up to 3.3V using the highest attenuation of 11dB. DO NOT exceed the maximum of 3.3V in order to avoid damaging the device."""

    def __call__(self):
        """Fast method to read the channel value."""
        return self.value()

    def value(self):
        """Read the channel value."""
        return int()

    def init(self):
        """(Re)init and enable the ADC channel. This method is automatically called on object creation."""
        pass

    def deinit(self):
        """Disable the ADC channel."""
        pass

# https://docs.pycom.io/pycom_esp32/library/machine.DAC.html
class DAC(object):
    """class DAC – digital to analog conversion
The DAC is used to output analog values (a specific voltage) on pin P22 or pin P21. The voltage will be between 0 and 3.3V.

Usage:
    import machine

    dac = machine.DAC('P22')        # create a DAC object
    dac.write(0.5)                  # set output to 50%

    dac_tone = machine.DAC('P21')   # create a DAC object
    dac_tone.tone(1000, 0)          # set tone output to 1kHz
"""

    def __init__(self, pin):
        """Create a DAC object, that will let you associate a channel with a pin. pin can be a string argument."""
        super().__init__(pin=pin)
        self.init()

    def init(self):
        """Enable the DAC block. This method is automatically called on object creation."""
        pass

    def deinit(self):
        """Disable the DAC block."""
        pass

    def write(self, value):
        """Set the DC level for a DAC pin. value is a float argument, with values between 0 and 1."""
        pass

    def tone(self, frequency, amplitude):
        """Sets up tone signal to the specified frequency at amplitude scale. frequency can be from 125Hz to 20kHz. amplitude is an integer specifying the tone amplitude to write the DAC pin. Amplitude value represents: 0 is 0dB, 1 is 6dB, 2 is 12dB, 3 is 18dB."""
        pass

# https://docs.pycom.io/pycom_esp32/library/machine.I2C.html
class I2C(object):
    """class I2C – a two-wire serial protocol
I2C is a two-wire protocol for communicating between devices. At the physical level it consists of 2 wires: SCL and SDA, the clock and data lines respectively.

I2C objects are created attached to a specific bus. They can be initialized when created, or initialized later on.

Example:
    from machine import I2C

    i2c = I2C(0)                         # create on bus 0
    i2c = I2C(0, I2C.MASTER)             # create and init as a master
    i2c.init(I2C.MASTER, baudrate=20000) # init as a master
    i2c.deinit()                         # turn off the peripheral

Printing the i2c object gives you information about its configuration.

A master must specify the recipient’s address:
    i2c.init(I2C.MASTER)
    i2c.writeto(0x42, '123')        # send 3 bytes to slave with address 0x42
    i2c.writeto(addr=0x42, b'456')  # keyword for address

Master also has other methods:
    i2c.scan()                          # scan for slaves on the bus, returning
                                        #   a list of valid addresses
    i2c.readfrom_mem(0x42, 2, 3)        # read 3 bytes from memory of slave 0x42,
                                        #   starting at address 2 in the slave
    i2c.writeto_mem(0x42, 2, 'abc')     # write 'abc' (3 bytes) to memory of slave 0x42
                                        # starting at address 2 in the slave, timeout after 1 second"""

    def __init__(self, bus=0, **kwargs):
        """Construct an I2C object on the given bus. bus can only be 0. If the bus is not given, the default one will be selected (0)."""
        super().__init__(bus=bus, **kwargs)
        self.init(I2C.MASTER, **kwargs)

    def init(self, mode, *, baudrate=100000, pins=(Pin.module.P9, Pin.module.P10)):
        """Initialize the I2C bus with the given parameters:
    - mode must be I2C.MASTER
    - baudrate is the SCL clock rate
    - pins is an optional tuple with the pins to assign to the I2C bus. The default I2C pins are P9 (SDA) and P10 (SCL)"""
        pass

    def scan(self):
        """Scan all I2C addresses between 0x08 and 0x77 inclusive and return a list of those that respond. A device responds if it pulls the SDA line low after its address (including a read bit) is sent on the bus."""
        return [int(), int()]

    def readfrom(self, addr, nbytes):
        """Read nbytes from the slave specified by addr. Returns a bytes object with the data read."""
        return bytes()

    def readfrom_into(self, addr, buf):
        """Read into buf from the slave specified by addr. The number of bytes read will be the length of buf.
Return value is the number of bytes read."""
        return int(len(buf))

    def writeto(self, addr, buf):
        """Write the bytes from buf to the slave specified by addr.
Return value is the number of bytes written."""
        return int()

    def readfrom_mem(self, addr, memaddr, nbytes):
        """Read nbytes from the slave specified by addr starting from the memory address specified by memaddr."""
        return bytes()

    def readfrom_mem_into(self, addr, memaddr, buf):
        """Read into buf from the slave specified by addr starting from the memory address specified by memaddr. The number of bytes read is the length of buf.
The return value is the number of bytes read."""
        return int(len(buf))

    def writeto_mem(self, addr, memaddr, buf):
        """Write buf to the slave specified by addr starting from the memory address specified by memaddr.
The return value is the number of bytes written."""
        return int()

    MASTER=0 # for initialising the bus to master mode

# https://docs.pycom.io/pycom_esp32/library/machine.Pin.html
class Pin(object):
    """class Pin – control I/O pins
A pin is the basic object to control I/O pins (also known as GPIO - general-purpose input/output). It has methods to set the mode of the pin (input, output, etc) and methods to get and set the digital logic level. For analog control of a pin, see the ADC class."""

    def __init__(self, id, **kwargs):
        """Create a new Pin object associated with the string id. If additional arguments are given, they are used to initialize the pin. See Pin.init().

from machine import Pin
p = Pin('P10', mode=Pin.OUT, pull=None, alt=-1)"""
        super().__init__(id=id, **kwargs)
        self.init(**kwargs)

    def init(self, mode, pull, *, alt):
        """Initialize the pin:
    - mode can be one of:
        * Pin.IN - input pin.
        * Pin.OUT - output pin in push-pull mode.
        * Pin.OPEN_DRAIN - input or output pin in open-drain mode.
    - pull can be one of:
        * None - no pull up or down resistor.
        * Pin.PULL_UP - pull up resistor enabled.
        * Pin.PULL_DOWN - pull down resistor enabled.
    - alt is the id of the alternate function.
Returns: None"""
        return None

    def id(self):
        """Get the pin id."""
        return str()

    def value(self):
        """Get or set the digital logic level of the pin:
    - With no argument, return 0 or 1 depending on the logic level of the pin.
    - With value given, set the logic level of the pin. value can be anything that converts to a boolean. If it converts to True, the pin is set high, otherwise it is set low."""
        return bool()
    def value(self, value):
        """Get or set the digital logic level of the pin:
    - With no argument, return 0 or 1 depending on the logic level of the pin.
    - With value given, set the logic level of the pin. value can be anything that converts to a boolean. If it converts to True, the pin is set high, otherwise it is set low."""
        pass

    def __call__(self):
        """Pin objects are callable. The call method provides a (fast) shortcut to set and get the value of the pin.

Example:
    from machine import Pin
    pin = Pin('P12', mode=Pin.IN, pull=Pin.PULL_UP)
    pin()   # fast method to get the value"""
        return self.value()
    def __call__(self, value):
        """Pin objects are callable. The call method provides a (fast) shortcut to set and get the value of the pin.

Example:
    from machine import Pin
    pin = Pin('P12', mode=Pin.IN, pull=Pin.PULL_UP)
    pin()   # fast method to get the value"""
        self.value(value)

    def toggle(self):
        """Toggle the value of the pin."""
        pass

    def mode(self):
        """Get or set the pin mode."""
        return int()
    def mode(self, mode):
        """Get or set the pin mode."""
        pass

    def pull(self):
        """Get or set the pin pull."""
        return int()
    def pull(self, pull):
        """Get or set the pin pull."""
        pass


    def hold(self):
        """Get or set the pin hold. Can be used to retain the pin state through a core reset and system reset triggered by watchdog time-out or Deep-sleep events."""
        pass
    def hold(self, hold):
        """Get or set the pin hold. Can be used to retain the pin state through a core reset and system reset triggered by watchdog time-out or Deep-sleep events."""
        return int()

    def callback(self, trigger, handler=None, arg=None):
        """Set a callback to be triggered when the input level at the pin changes.
    - trigger is the type of event that triggers the callback. Possible values are:
        * Pin.IRQ_FALLING interrupt on falling edge.
        * Pin.IRQ_FALLING interrupt on rising edge.
        * Pin.IRQ_LOW_LEVEL interrupt on low level.
        * Pin.IRQ_HIGH_LEVEL interrupt on high level.
      The values can be ORed together, for instance trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING
    - handler is the function to be called when the event happens. This function will receive one argument. Set handler to None to disable it.
    - arg is an optional argument to pass to the callback. If left empty or set to None, the function will receive the Pin object that triggered it.

Example:
    from machine import Pin

    def pin_handler(arg):
        print("got an interrupt in pin %s" % (arg.id()))

    p_in = Pin('P10', mode=Pin.IN, pull=Pin.PULL_UP)
    p_in.callback(Pin.IRQ_FALLING | Pin.IRQ_RISING, pin_handler)

Note: For more information on how Pycom’s products handle interrupts, see https://docs.pycom.io/pycom_esp32/pycom_esp32/toolsandfeatures.html#pycom-interrupt-handling"""
        if handler is not None: handler(self if arg is None else arg)

    class exp_board(object):
        G2=Pin('P0', mode=Pin.IN, pull=Pin.PULL_UP, alt=14)
        G1=Pin('P1', mode=Pin.OUT, pull=None, alt=14)
        G23=Pin('P2', mode=Pin.OUT, pull=None, alt=-1)
        G24=Pin('P3', mode=Pin.OUT, pull=None, alt=17)
        G11=Pin('P4', mode=Pin.IN, pull=Pin.PULL_UP, alt=17)
        G12=Pin('P5', mode=Pin.OUT, pull=None, alt=63)
        G13=Pin('P6', mode=Pin.OUT, pull=None, alt=65)
        G14=Pin('P7', mode=Pin.IN, pull=None, alt=64)
        G15=Pin('P8', mode=Pin.OUT, pull=None, alt=198)
        G16=Pin('P9', mode=Pin.OPEN_DRAIN, pull=Pin.PULL_UP, alt=-1)
        G17=Pin('P10', mode=Pin.OPEN_DRAIN, pull=Pin.PULL_UP, alt=-1)
        G22=Pin('P11', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
        G28=Pin('P12', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
        G5=Pin('P13', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
        G4=Pin('P14', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
        G0=Pin('P15', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
        G3=Pin('P16', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
        G31=Pin('P17', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
        G30=Pin('P18', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
        G6=Pin('P19', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
        G7=Pin('P20', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
        G8=Pin('P21', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
        G9=Pin('P22', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
        G10=Pin('P23', mode=Pin.IN, pull=None, alt=-1)
    class module(object):
        P0=Pin('P0', mode=Pin.IN, pull=Pin.PULL_UP, alt=14)
        P1=Pin('P1', mode=Pin.OUT, pull=None, alt=14)
        P2=Pin('P2', mode=Pin.OUT, pull=None, alt=-1)
        P3=Pin('P3', mode=Pin.OUT, pull=None, alt=17)
        P4=Pin('P4', mode=Pin.IN, pull=Pin.PULL_UP, alt=17)
        P5=Pin('P5', mode=Pin.OUT, pull=None, alt=63)
        P6=Pin('P6', mode=Pin.OUT, pull=None, alt=65)
        P7=Pin('P7', mode=Pin.IN, pull=None, alt=64)
        P8=Pin('P8', mode=Pin.OUT, pull=None, alt=198)
        P9=Pin('P9', mode=Pin.OPEN_DRAIN, pull=Pin.PULL_UP, alt=-1)
        P10=Pin('P10', mode=Pin.OPEN_DRAIN, pull=Pin.PULL_UP, alt=-1)
        P11=Pin('P11', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
        P12=Pin('P12', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
        P13=Pin('P13', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
        P14=Pin('P14', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
        P15=Pin('P15', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
        P16=Pin('P16', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
        P17=Pin('P17', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
        P18=Pin('P18', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
        P19=Pin('P19', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
        P20=Pin('P20', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
        P21=Pin('P21', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
        P22=Pin('P22', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
        P23=Pin('P23', mode=Pin.IN, pull=None, alt=-1)

    IN=1
    OUT=2
    OPEN_DRAIN=7

    PULL_UP=1
    PULL_DOWN=2

    IRQ_RISING=1
    IRQ_FALLING=2
    IRQ_LOW_LEVEL=4
    IRQ_HIGH_LEVEL=5

# https://docs.pycom.io/pycom_esp32/library/machine.PWM.html
class PWM(object):
    """class PWM – Pulse width modulation"""

    def __init__(self, timer, frequency):
        """Create a PWM object. This sets up the timer to oscillate at the specified frequency. timer is an integer from 0 to 3. frequency is an integer from 1 to 19455 Hz (this values can change in future upgrades)."""
        super().__init__(timer=timer, frequency=frequency)

    def channel(self, id, pin, *, duty_cycle=0.5):
        """Connect a PWM channel to a pin, setting the intial duty cycle. id is an integer from 0 to 7. pin is a string argument. duty_cycle is a keyword-only float argument, with values between 0 and 1. Returns an instance of PWMChannel."""
        return PWMChannel(id, pin, duty_cycle=duty_cycle)

# https://docs.pycom.io/pycom_esp32/library/machine.PWM.html#class-pwmchannel-control-a-pwm-channel
class PWMChannel(object):
    def duty_cycle(self, value):
        """Set the duty cycle for a PWM channel. value is a float argument, with values between 0 and 1."""
        pass

# https://docs.pycom.io/pycom_esp32/library/machine.RTC.html
class RTC(object):
    """class RTC – real time clock
The RTC is used to keep track of the date and time.

Example usage:
    from machine import RTC

    rtc = RTC()
    rtc.init((2014, 5, 1, 4, 13, 0, 0, 0))
    print(rtc.now())
    """
    def __init__(self, id, **kwargs):
        """Create an RTC object. See init for parameters of initialization.:
    # id of the RTC may be set if multiple are connected. Defaults to id = 0.
    rtc = RTC(id=0)
        """
        super().__init__(id=id, **kwargs)
        self.init(**kwargs)
    def init(self, datetime):
        """Initialize the RTC. Datetime is a tuple of the form:
    (year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])

For example:
    # for 2nd of February 2017 at 10:30am (TZ 0)
    rtc.init((2017, 2, 28, 10, 30, 0, 0, 0))

Note: tzinfo is ignored by this method. Use time.timezone to achieve similar results.
        """
        pass
    def now(self):
        """Get get the current datetime tuple.:
    # returns datetime tuple
    rtc.now()
        """
        return (2017, 2, 28, 10, 30, 0, 0, None)
    def ntp_sync(self, server, *, update_period=3600):
        """Set up automatic fetch and update the time using NTP (SNTP).
    - server is the URL of the NTP server. Can be set to None to disable the periodic updates.
    - update_period is the number of seconds between updates. Shortest period is 15 seconds.

Can be used like:
    rtc.ntp_sync("pool.ntp.org") # this is an example. You can select a more specific server according to your geographical
        """
        pass
    def calibration(self):
        """Get RTC calibration.
With no arguments, calibration() returns the current calibration value, which is an integer in the range [-(2^27 - 1) : 2^27 -1].:
    # returns current calibration
    rtc.calibration()
        """
        return int()
    def calibration(self, cal):
        """Set RTC calibration.
With one argument, calibration() sets the RTC calibration for long term counting.:
    # adjusts calibration to +1/128 of the counter tick.
    rtc.calibration(1)

The RTC counter ticks at 5 MHz. Current crystal has an error of less than 10 ppm (5 minutes a year), which is more than acceptable for most applications. Calibration is only needed if you want to achieve errors lower than that.

The units of cal are in 1/128 of RTC tick.

Units added will slow down the clock. Conversely, negative values will speed it up.

Experienced users can see the note below on how the RTC keeps the count of time for more information on how calibration works.

Note: Pycom’s port of MicroPython for the ESP32 uses the UNIX epoch (1970-01-01).

Note: Internally, a 64 bit counter is used to keep microseconds, so the time will overflow around year 586512 CE.

Note: The pseudocode for the RTC ISR is something like:
    # the 5 in the comments come from 5 ticks per us (@ 5 MHz)

    bres_counter = 0

    def rtc_isr():
        global bres_counter
        bres_limit = 128 * 8388605 + cal # 8388605 = 5 * ((2^23 - 1) // 5)
        bres_counter += 128 * 8388607 # 128 * (2^23 - 1)
        while bres_counter >= bres_limit:
            bres_counter -= bres_limit
            uptime_microseconds += 1677721 # 8388605 / 5
cal is the calibration parameter that can be set using the calibration method.
The idea was extracted from http://www.romanblack.com/one_sec.htm , which in turn is inspired on the Bresenham’s line algorithm .
        """
        return int()

# https://docs.pycom.io/pycom_esp32/library/machine.SD.html
class SD(object):
    """class SD – Secure digital memory card
The SD card class allows to configure and enable the memory card module of your Pycom module and automatically mount it as /sd as part of the file system. There is a single pin combination that can be used for the SD card, and the current implementation only works in 1-bit mode. The pin connections are as follows:

P8: DAT0, P23: SCLK and P4: CMD no external pull-up resistors are needed.

If you have one of the Pycom expansion boards, then simply insert the card into the micro SD socket and run your script.

Note: Make sure your SD card is formatted either as FAT16 or FAT32.

Example usage:
    from machine import SD
    import os

    sd = SD()
    os.mount(sd, '/sd')

    # check the content
    os.listdir('/sd')

    # try some standard file operations
    f = open('/sd/test.txt', 'w')
    f.write('Testing SD card write operations')
    f.close()
    f = open('/sd/test.txt', 'r')
    f.readall()
    f.close()

Note: Please note that the SD card library currently supports FAT16/32 formatted SD cards up to 32 GB. Future firmware updates will increase compatibility with additional formats and sizes.
    """
    def __init__(self, id, **kwargs):
        """Create a SD card object. See init() for parameters if initialization."""
        super().__init__(id=id, **kwargs)
        self.init(id)
    def init(self, id=0):
        """Enable the SD card."""
        pass
    def deinit(self):
        """Disable the SD card."""
        pass

# https://docs.pycom.io/pycom_esp32/library/machine.SPI.html
class SPI(object):
    """class SPI – a master-driven serial protocol
SPI is a serial protocol that is driven by a master. At the physical level there are 3 lines: SCK, MOSI, MISO.

See usage model of I2C; SPI is very similar. Main difference is parameters to init the SPI bus:
    from machine import SPI
    spi = SPI(0, mode=SPI.MASTER, baudrate=1000000, polarity=0, phase=0, firstbit=SPI.MSB)

Only required parameter is mode, must be SPI.MASTER. Polarity can be 0 or 1, and is the level the idle clock line sits at. Phase can be 0 or 1 to sample data on the first or second clock edge respectively."""
    def __init__(self, id, **kwargs):
        """Construct an SPI object on the given bus. id can be only 0. With no additional parameters, the SPI object is created but not initialized (it has the settings from the last initialisation of the bus, if any). If extra arguments are given, the bus is initialized. See init for parameters of initialisation."""
        super().__init__(id=id, **kwargs)
        self.init(**kwargs)
    def init(self, mode, baudrate=1000000, *, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, pins=(Pin.module.P10, Pin.module.P11, Pin.module.P12)):
        """Initialize the SPI bus with the given parameters:
    - mode must be SPI.MASTER.
    - baudrate is the SCK clock rate.
    - polarity can be 0 or 1, and is the level the idle clock line sits at.
    - phase can be 0 or 1 to sample data on the first or second clock edge respectively.
    - bits is the width of each transfer, accepted values are 8, 16 and 32.
    - firstbit can be SPI.MSB only.
    - pins is an optional tuple with the pins to assign to the SPI bus. If the pins argument is not given the default pins will be selected (P10 as CLK, P11 as MOSI and P12 as MISO). If pins is passed as None then no pin assigment will be made."""
        pass

    def deinit(self):
        """Turn off the SPI bus."""

    def write(self, buf):
        """Write the data contained in buf. Returns the number of bytes written."""
        return int()

    def read(self, nbytes, *, write=0x00):
        """Read the nbytes while writing the data specified by write. Return the number of bytes read."""
        return bytes()

    def readinto(self, buf, *, write=0x00):
        """Read into the buffer specified by buf while writing the data specified by write. Return the number of bytes read."""
        return int()

    def write_readinto(self, write_buf, read_buf):
        """Write from write_buf and read into read_buf. Both buffers must have the same length. Returns the number of bytes written"""
        return int()

    MASTER=0
    MSB=0

# https://docs.pycom.io/pycom_esp32/library/machine.Timer.html
class Timer(object):
    """class Timer – measure time spans and set alarms
Timers can be used for a great variety of tasks, like measuring time spans or being notified that a specific interval has elapsed.

These two concepts are grouped into two different subclasses:
    Chrono: used to measure time spans.
    Alarm: to get interrupted after a specific interval.

Hint: You can create as many of these objects as needed.
    """
    @staticmethod
    def sleep_us(time_us):
        """Delay for a given number of microseconds, should be positive or 0 (for speed, the condition is not enforced). Internally it uses the same timer as the other elements of the Timer class. It compensates for the calling overhead, so for example, 100 us should be really close to 100us. For times bigger than 10,000 us it releases the GIL to let other threads run, so exactitude is not guaranteed for delays longer than that."""
        pass

    class Chrono(object):
        """class Chrono – measure time spans

Usage example:
    from machine import Timer
    import time

    chrono = Timer.Chrono()

    chrono.start()
    time.sleep(1.25) # simulate the first lap took 1.25 seconds
    lap = chrono.read() # read elapsed time without stopping
    time.sleep(1.5)
    chrono.stop()
    total = chrono.read()

    print()
    print("\\nthe racer took %f seconds to finish the race" % total)
    print("  %f seconds in the first lap" % lap)
    print("  %f seconds in the last lap" % (total - lap))"""
        def __init__(self):
            """Create a chronometer object."""
            super().__init__()
        def start(self):
            """Start the chronometer."""
            pass
        def stop(self):
            """Stop the chronometer."""
            pass
        def reset(self):
            """Reset the time count to 0."""
            pass
        def read(self):
            """Get the elapsed time in seconds."""
            return int()
        def read_ms(self):
            """Get the elapsed time in miliseconds."""
            return int()
        def read_us(self):
            """Get the elapsed time in microseconds."""
            return int()
    class Alarm(object):
        """class Alarm – get interrupted after a specific interval

Usage example:
    from machine import Timer

    class Clock:

        def __init__(self):
            self.seconds = 0
            self.__alarm = Timer.Alarm(self._seconds_handler, 1, periodic=True)

        def _seconds_handler(self, alarm):
            self.seconds += 1
            print("%02d seconds have passed" % self.seconds)
            if self.seconds == 10:
                alarm.cancel() # stop counting after 10 seconds

    clock = Clock()

Note: For more information on how Pycom’s products handle interrupts, see https://docs.pycom.io/pycom_esp32/pycom_esp32/toolsandfeatures.html#pycom-interrupt-handling.
        """
        def __init__(self, handler, s, *, ms=int(), us=int(), arg=None, periodic=False):
            """Create an Alarm object.
    - handler: will be called after the interval has elapsed. If set to None, the alarm will be disabled after creation.
    - arg: an optional argument can be passed to the callback handler function. If None is specified, the function will receive the object that triggered the alarm.
    - s, ms, us: the interval can be specified in seconds (float), miliseconds (integer) or microseconds (integer). Only one at a time can be specified.
    - periodic: an alarm can be set to trigger repeatedly by setting this parameter to True.
            """
            super().__init__(handler=handler, s=s, ms=ms, us=us, arg=arg, periodic=periodic)
            if handler is not None: handler(self if arg is None else arg)
        def callback(self, handler, *, arg=None):
            """Specify a callback handler for the alarm. If set to None, the alarm will be disabled.

An optional argument arg can be passed to the callback handler function. If None is specified, the function will receive the object that triggered the alarm.
            """
            if handler is not None: handler(self if arg is None else arg)
        def cancel(self):
            """Diables the alarm"""
            pass

# https://docs.pycom.io/pycom_esp32/library/machine.UART.html
class UART(object):
    """class UART – duplex serial communication bus
UART implements the standard UART/USART duplex serial communications protocol. At the physical level it consists of 2 lines: RXD and TXD. The unit of communication is a character (not to be confused with a string character) which can be 5, 6, 7 or 8 bits wide.

UART objects can be created and initialized using:
    from machine import UART

    uart = UART(1, 9600)                         # init with given baudrate
    uart.init(9600, bits=8, parity=None, stop=1) # init with given parameters

Bits can be 5, 6, 7, 8. Parity can be None, UART.EVEN or UART.ODD. Stop can be 1, 1.5 or 2.

A UART object acts like a stream object therefore reading and writing is done using the standard stream methods:
    uart.read(10)       # read 10 characters, returns a bytes object
    uart.readall()      # read all available characters
    uart.readline()     # read a line
    uart.readinto(buf)  # read and store into the given buffer
    uart.write('abc')   # write the 3 characters

To check if there is anything to be read, use:
    uart.any()               # returns the number of characters available for reading"""
    def __init__(self, bus, **kwargs):
        """Construct a UART object on the given bus. bus can be 0 or 1. If the bus is not given, the default one will be selected (0) or the selection will be made based on the given pins."""
        super().__init__(bus=bus, **kwargs)
        self.init(**kwargs)
    def init(self, baudrate=9600, bits=8, parity=None, stop=1, *, timeout_chars=2, pins=(Pin.module.P1, Pin.module.P0)):
        """Initialize the UART bus with the given parameters:
    - baudrate is the clock rate.
    - bits is the number of bits per character. Can be 5, 6, 7 or 8.
    - parity is the parity, None, UART.EVEN or UART.ODD.
    - stop is the number of stop bits, 1 or 2.
    - timeout_chars Rx timeout defined in number of characters. The value given here will be multiplied by the time a characters takes to be transmitted at the configured baudrate.
    - pins is a 4 or 2 item list indicating the TXD, RXD, RTS and CTS pins (in that order). Any of the pins can be None if one wants the UART to operate with limited functionality. If the RTS pin is given the the RX pin must be given as well. The same applies to CTS. When no pins are given, then the default set of TXD (P1) and RXD (P0) pins is taken, and hardware flow control will be disabled. If pins=None, no pin assignment will be made.
        """
        pass
    def deinit(self):
        """Turn off the UART bus."""
        pass
    def any(self):
        """Return the number of characters available for reading."""
        return int()
    def read(self):
        """Read characters.
Return value: a bytes object containing the bytes read in. Returns None on timeout."""
        return bytes()
        return None
    def read(self, nbytes):
        """Read characters. If nbytes is specified then read at most that many bytes.
Return value: a bytes object containing the bytes read in. Returns None on timeout."""
        return bytes()
        return None
    def readall(self):
        """Read as much data as possible.
Return value: a bytes object or None on timeout."""
        return bytes()
        return None

    def readinto(self, buf):
        """Read at most len(buf) bytes into the buf.
Return value: number of bytes read and stored into buf or None on timeout."""
        return int()
        return None
    def readinto(self, buf, nbytes):
        """Read at most nbytes bytes into the buf.
Return value: number of bytes read and stored into buf or None on timeout."""
        return int()
        return None
    def readline(self):
        """Read a line, ending in a newline character. If such a line exists, return is immediate. If the timeout elapses, all available data is returned regardless of whether a newline exists.
Return value: the line read or None on timeout if no data is available."""
        return str()
        return None
    def write(self, buf):
        """Write the buffer of bytes to the bus.
Return value: number of bytes written or None on timeout."""
        return int()
        return None
    def sendbreak(self):
        """Send a break condition on the bus. This drives the bus low for a duration of 13 bits. Return value: None."""
        return None

    EVEN=2
    ODD=3

    RX_ANY=int()

# https://docs.pycom.io/pycom_esp32/library/machine.WDT.html
class WDT(object):
    """class WDT – watchdog timer
The WDT is used to restart the system when the application crashes and ends up into a non recoverable state. Once started it cannot be stopped or reconfigured in any way. After enabling, the application must “feed” the watchdog periodically to prevent it from expiring and resetting the system.

Example usage:
    from machine import WDT
    wdt = WDT(timeout=2000)  # enable it with a timeout of 2s
    wdt.feed()

Availability of this class: pyboard, WiPy.
    """
    def __init__(self, id=0, timeout=5000):
        """Create a WDT object and start it. The timeout must be given in seconds and the minimum value that is accepted is 1 second. Once it is running the timeout cannot be changed and the WDT cannot be stopped either."""
        super().__init__(id=id, timeout=timeout)
    def feed(self):
        """Feed the WDT to prevent it from resetting the system. The application should place this call in a sensible place ensuring that the WDT is only fed after verifying that everything is functioning correctly."""
        pass
