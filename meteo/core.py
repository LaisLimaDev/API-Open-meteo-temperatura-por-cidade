import requests

def get_lat_lon(city):
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": city, "format": "json", "limit": 1}
    headers = {"User-Agent": "open-meteo-app/1.0 (seu-email@exemplo.com)"}
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data:
            return float(data[0]["lat"]), float(data[0]["lon"])
    except Exception as e:
        print(f"Erro ao buscar coordenadas: {e}")
    return None, None

def get_temperature(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": "true"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("current_weather", {}).get("temperature")
    except Exception as e:
        print(f"Erro ao buscar temperatura: {e}")
    return None

def get_temperatures_for_cities(cities):
    results = []
    for city in cities:
        lat, lon = get_lat_lon(city)
        if lat is not None and lon is not None:
            temp = get_temperature(lat, lon)
            if temp is not None:
                results.append(f"{city}: {temp}°C")
            else:
                results.append(f"{city}: N/A")
        else:
            results.append(f"{city}: N/A")
    print("\t".join(results))