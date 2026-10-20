from api_client import get_json

# 1.
data = get_json("https://geocoding-api.open-meteo.com/v1/search",
                  params={"name": "Stockholm", "count": 1})
print(data)

longitude = data["results"][0]["longitude"]
latitude = data["results"][0]["latitude"]

print(f"Longitude: {longitude}\nLatitude: {latitude}")


# 2. Get the weather for those coordinates^
data = get_json("https://api.open-meteo.com/v1/forecast",
                params={"longitude": longitude,
                        "latitude": latitude,
                        "current": "temperature_2m,wind_speed_10m"})
print(data)