from api_client import get_json

# 1.
data = get_json("https://geocoding-api.open-meteo.com/v1/search",
                  params={"name": "Stockholm", "count": 1})
print(data)

print(f"""
Longitude: {data["results"][0]["longitude"]}
Latitude: {data["results"][0]["latitude"]}
""")