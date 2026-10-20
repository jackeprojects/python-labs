from api_client import get_json

# 1.
data = get_json("https://geocoding-api.open-meteo.com/v1/search",
                  params={"name": "Stockholm", "count": 1})
print(data)

lat = data["results"][0]["latitude"]
lon = data["results"][0]["longitude"]

print(f"Latitude: {lat}\nLongitude: {lon}")


# 2. Get the weather for those coordinates^
data = get_json("https://api.open-meteo.com/v1/forecast",
                params={"latitude": lat,
                        "longitude": lon,
                        "current": "temperature_2m,wind_speed_10m"})
print(data)


# 3. Put it together
def find_city(city):
    data = get_json("https://geocoding-api.open-meteo.com/v1/search",
                    params={"name": city, "count": 1})
    if data:
        if "results" in data:  # Step 4: Handle non-existant cities
                return data["results"][0]
    print("Could not find city")

def get_weather(lat, lon):
    data = get_json("https://api.open-meteo.com/v1/forecast",
                    params={"latitude": lat,
                            "longitude": lon,
                            "current": "temperature_2m,wind_speed_10m"})
    if data:
        return data
    print("Could not get weather")

user_input = input("Name a city: ")

city = find_city(user_input)
if city != None:
        lat = city["latitude"]
        lon = city["longitude"]

        weather = get_weather(lat, lon)
        if weather != None:
                city_name = city["name"]
                city_country = city["country"]

                temp = weather["current"]["temperature_2m"]
                temp_unit = weather["current_units"]["temperature_2m"]

                wind = weather["current"]["wind_speed_10m"]
                wind_unit = weather["current_units"]["wind_speed_10m"]

                print(f"{city_name}, {city_country}: {temp}{temp_unit}, wind {wind} {wind_unit}")


# 4. Handle a city that does not exist
print(find_city("asdfk"))
# Check side-comment in find_city() func