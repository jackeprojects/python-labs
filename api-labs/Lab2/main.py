from fastapi import FastAPI

# 1. Start the server
app = FastAPI()

movies = [
    {"id": 1, "title": "Stalker", "director": "Andrei Tarkovsky", "year": 1979},
    {"id": 2, "title": "Come and See", "director": "Elem Klimov", "year": 1985},
    {"id": 3, "title": "John Carter", "director": "Andrew Stanton", "year": 2012},
    {"id": 4, "title": "Van Helsing", "director": "Stephen Sommers", "year": 2004}
]

@app.get("/movies")
def get_movies():
    return movies