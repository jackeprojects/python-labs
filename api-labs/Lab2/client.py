from api_client import get_json
import requests

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

response = requests.post("http://localhost:8000/movies", json=new_movie, timeout=5)
print(response.status_code)