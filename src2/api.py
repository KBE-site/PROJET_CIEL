from datetime import datetime
from astropy.coordinates import get_body, EarthLocation
from astropy.time import Time
from astropy.coordinates import AltAz

def get_all_solar_pattern_objects(solar_obj: str, lat: float=48.87668, lon: float=2.35904, height=53):
    date = Time (datetime.now())
    loc = EarthLocation(lat=lat, lon=lon, height=height)
    obj = get_body(solar_obj, date, loc)

    altaz_frame = AltAz(obstime=date, location=loc)
    obj_altaz = obj.transform_to(altaz_frame)

    return obj_altaz

# obj = "moon"

# print(f"{obj} altitude : {get_all_solar_pattern_objects(obj).alt}")
# print(f"{obj} azimuth : {get_all_solar_pattern_objects(obj).az}")