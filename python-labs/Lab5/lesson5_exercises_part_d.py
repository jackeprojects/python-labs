# Part D, **kwargs

# 1. Write show_profile(**info), and iterate over all key/value pairs
def show_profile(**info):
    for keys, value in info.items():
        print(keys, value)

show_profile(name="Adam", age=26, city="Stockholm")


# 2. Write create_user(username, **details), return one dictionary containing username and all supplied details
user_details = {"first_name": "Adam", "last_name": "Smith", "city": "Stockholm"}
def create_user(username, **details):
    return {"username": username, **details}


print(create_user("Mada00", **user_details))


# 3. Write build_product(name, price, **metadata), and return a dictionary
gpu_data = {"memory_size": "16GB", "memory_type": "GDDR6","compute_units": 64, "ray_accelerators": 64, "ROPs": 128}
def build_product(name, price, **metadata):
    return {"name": name, "price": price, **metadata}

print(build_product("AMD Radeon RX 9070 XT", 900, **gpu_data))


# 4. Write function that accepts **settings, and return settings that aren't None
app_settings = {"theme": "dark", "volume": None, "font_size": 14}

def check_available_settings(**settings):
    available_settings = {}
    for key, value in settings.items():
        if value is not None:
            available_settings.update({key: value})

    return available_settings

print(check_available_settings(**app_settings))


# 5. Call normal named-parameter function using **dictionary unpacking
adam_info = {"name": "Adam", "age": 26, "city": "Stockholm"}

def introduce(name, age, city):
    return f"{name}, is {age} years old and lives in {city}"

print(introduce(**adam_info))