from meteo.core import get_lat_lon, get_temperature

def test_get_lat_lon():
    lat, lon = get_lat_lon("Campinas")
    assert lat is not None and lon is not None

def test_get_temperature():
    lat, lon = get_lat_lon("Campinas")
    temp = get_temperature(lat, lon)
    assert temp is not None