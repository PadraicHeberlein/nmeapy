from math import sqrt, sin, cos, asin

class GPSPoint:
  def __init__(self, lat, lon):
    self.lat = str(lat)
    self.lon = str(lon)
  
  def dist(self, other): 
    return triangulate(self, other)

  def to_dd(self):
    return GPSPoint(to_decdeg(self.lat), to_decdeg(self.lon))
  
  def __str__(self): 
    decimal_gps = self.to_dd()
    return f'{decimal_gps.lat},{decimal_gps.lon}'
    
def triangulate(gps1, gps2):
  lat1, lat2 = float(gps1.lat), float(gps2.lat)
  lon1, lon2 = float(gps1.lon), float(gps2.lon)
  p = 0.017453292519943295        # = pi / 180
  a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
  return 12742 * asin(sqrt(a))    # 12742 = 2 * radius of earth in meters

def to_decdeg(dms):
  negative = False
  if dms[0] == '-': 
    dms = dms[1:len(dms)]
    negative = True
  d = float(dms) // 100
  m = (float(dms) % 100) 
  sign = -1 if negative else 1 
  return sign * dm_to_dd(d, m)

def dm_to_dd(degrees, minutes): return degrees + (minutes / 60)