from api_client import get_json
import requests
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("API_KEY")

# 6. Call you own API from Python
movies = get_json("http://localhost:8000/movies", timeout=5)
print(movies)

fake_movie = get_json("http://localhost:8000/movies/30", timeout=5)
print(fake_movie)

new_movie ={
    "title": "Dune",
    "director": "David Lynch",
    "year": 1984
}


# Exersice 3; step 6 - See status_code of post with and without header
response = requests.post("http://localhost:8000/movies", json=new_movie, timeout=5)
print(response.status_code)

response = requests.post("http://localhost:8000/movies", json=new_movie, timeout=5, headers={"X-API-Key": key})
print(response.status_code)