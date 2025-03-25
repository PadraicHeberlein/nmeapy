class GPGGA:
    def __init__(self):
        self.msg = "$GPGGA"
        self.time = ""
        self.lat = ""
        self.lat_dir = ""
        self.lon = ""
        self.lon_dir = ""
        self.fix = 0
        self.satellites = 0
        self.altitude = 0.0
        self.altitude_units = ""
        self.geoid_height = 0.0
        self.geoid_height_units = ""
        self.differential_age = ""
        self.differential_ref_station = ""

    def parse(self, data):
        try:
            parts = data.split(",")
            self.time = parts[1]
            self.lat = parts[2]
            self.lat_dir = parts[3]
            self.lon = parts[4]
            self.lon_dir = parts[5]
            self.fix = int(parts[6])
            self.satellites = int(parts[7])
            self.altitude = float(parts[9])
            self.altitude_units = parts[10]
            self.geoid_height = float(parts[11])
            self.geoid_height_units = parts[12]
            if len(parts) > 13:
                self.differential_age = parts[13]
                self.differential_ref_station = parts[14]
        except Exception:
            print(f'unable to parse...{Exception}')

    def json(self):
        return {
            'msg': self.msg,
            'time': self.time,
            'latitude': self.lat,
            'latitude_dir': self.lat_dir,
            'longitude': self.lon,
            'longitude_dir': self.lon_dir,
            'fix': self.fix,
            'satellites': self.satellites,
            'altitude': self.altitude,
            'altitude_units': self.altitude_units,
            'geoid_height': self.geoid_height,
            'geoid_height_units': self.geoid_height_units,
            'differential_age': self.differential_age,
            'differential_ref_station': self.differential_ref_station
        }

    def __str__(self):
        return "%s,%s,%s %s,%s %s,%d,%d,%f %s,%f %s" % (
            self.msg, 
            self.time, 
            self.lat, 
            self.lat_dir, 
            self.lon,
            self.lon_dir, 
            self.fix, 
            self.satellites, 
            self.altitude, 
            self.altitude_units, 
            self.geoid_height, 
            self.geoid_height_units
        )