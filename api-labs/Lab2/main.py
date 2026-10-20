from fastapi import FastAPI, HTTPException

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


# 2. Get one movie
@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="No movie with that ID")

# Testing ID used by a movie returns 200
# Testing ID that isn't used by a movie returns 404
# Testing ID with invalid chars returns 422