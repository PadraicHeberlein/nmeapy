import serial
import time
import gpgga, gpgll, gpgsa, gpgsv, gprmc

DEFAULT_PORT = '/dev/ttyUSB0'
DEFAULT_BAUDRATE = 9600
DEFAULT_BYTESIZE = serial.EIGHTBITS
DEFAULT_PARITY = serial.PARITY_NONE
DEFAULT_STOPBITS = serial.STOPBITS_ONE
DEFAULT_TIMEOUT = 1

ser = serial.Serial(
  port='/dev/ttyUSB0',
  baudrate=9600,
  bytesize=serial.EIGHTBITS,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  timeout=1
)

class NMEA:
  def __init__(self):
    self.gga = gpgga.GPGGA()
    self.gll = gpgll.GPGLL()
    self.gsa = gpgsa.GPGSA()
    self.gsv = gpgsv.GPGSV()
    self.rmc = gprmc.GPRMC()
    self.serial = serial.Serial(
      port=DEFAULT_PORT,
      baudrate=DEFAULT_BAUDRATE,
      bytesize=DEFAULT_BYTESIZE,
      parity=DEFAULT_PARITY,
      stopbits=DEFAULT_STOPBITS,
      timeout=DEFAULT_TIMEOUT
    )
