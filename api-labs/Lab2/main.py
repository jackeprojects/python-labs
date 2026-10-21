from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# 1. Start the server
app = FastAPI()

movies = [
    {"id": 1, "title": "Stalker", "director": "Andrei Tarkovsky", "year": 1979},
    {"id": 2, "title": "Come and See", "director": "Elem Klimov", "year": 1985},
    {"id": 3, "title": "John Carter", "director": "Andrew Stanton", "year": 2012},
    {"id": 4, "title": "Van Helsing", "director": "Stephen Sommers", "year": 2004}
]

@app.get("/movies")
def get_movies(director: str | None = None, year: int | None = None):  # Step 3: Filter with optional params
    result = movies
    if director is not None:
        result = [movie for movie in result if director.lower() in movie["director"].lower()]
    if year is not None:
        result = [movie for movie in result if movie["year"] == year]
    return result


# 2. Get one movie
@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    return find_movie(movie_id)

# Testing ID used by a movie returns 200
# Testing ID that isn't used by a movie returns 404
# Testing ID with invalid chars returns 422


# 3. Filter with a query parameter
# See get_movies function ^


# 4. Add a movie
class Movie(BaseModel):
    title: str
    director: str
    year: int

@app.post("/movies", status_code=201)
def create_movie(movie: Movie):
    new_id = max((m["id"] for m in movies), default=0) + 1
    new_movie = {"id": new_id, "title": movie.title, "director": movie.director, "year": movie.year}
    movies.append(new_movie)
    return new_movie

# Creating a movie without a director returns 422
# Creating a movie with year written as text returns 201, successfully converting text to int
# Inside the "detail"-field of the error message


# 5. Replace and remove
def find_movie(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="No movie with that ID")

@app.put("/movies/{movie_id}")
def replace_movie(movie_id: int, movie: Movie):
    found_movie = find_movie(movie_id)
    found_movie["title"] = movie.title
    found_movie["director"] = movie.director
    found_movie["year"] = movie.year
    return found_movie

@app.delete("/movies/{movie_id}", status_code=204)
def delete_movie(movie_id: int):
    found_movie = find_movie(movie_id)
    movies.remove(found_movie)

# Deleting the same movie twice returns 404,
# since the movie isn't in the list anymore and ID doesnt rearrange

# Restarting the server reverts changes since it doesnt get saved


# 6. Call your own API from Python
# See api_client.py and client.py


# EXERCISE 2

# 1. Write the model and the route
class MovieUpdate(BaseModel):
    title: str | None = None
    director: str | None = None
    year: int | None = None

@app.patch("/movies/{movie_id}")
def update_movie(movie_id: int, movie_update: MovieUpdate):
    found_movie = find_movie(movie_id)
    found_movie.update(movie_update.model_dump(exclude_unset=True))

    return found_movie


# 2.
# Using .patch to update a movie and only sending year
# returns 200 - confirming it works.
# Checking same movie with .get shows that year has been updated