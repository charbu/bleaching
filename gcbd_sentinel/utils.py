from datetime import datetime
import sentinelhub as hub
import utm  # type: ignore


def lat_lon_to_pixel(lat, lon, transform):
    UTMx, UTMy, zone, band = utm.from_latlon(lat, lon)
    return hub.geo_utils.utm_to_pixel(UTMx, UTMy, transform)
