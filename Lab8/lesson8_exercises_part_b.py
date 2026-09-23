# Part B, Dictionary or class?

# 1. Represent a movie using a dictionary with title, director, and rating
movie_1 = {"title": "Stalker", "director": "Andrei Tarkovsky", "rating": 8.0}
print(f"Title: {movie_1['title']}, Director: {movie_1['director']}, Rating: {movie_1['rating']}")


# 2. Represent the same information using a Movie clas
class Movie:
    def __init__(self, title, director, rating: float):
        self.title = title
        self.director = director
        self.rating = rating

    def is_highly_rated(self):
        if self.rating >= 8.0:
            return True
        return False

movie_2 = Movie("John Carter", "Andrew Stanton", 6.6)
print(f"Title: {movie_2.title}, Director: {movie_2.director}, Rating: {movie_2.rating}")


# 3. Add a method to Movie that reutnrs whether the movie is highly rated
# See Movie class above, is_highly_rated() method returns either True or False based on movie rating
print(movie_2.is_highly_rated()) # :(


# 4. Explain one situation where you would choose a dictionary and one where you would choose a class
# I would create a dictionary if im only creating one movie,
# and create a class for when i need many movies.
# If using a class, every Movie object will have the same attribute (title, director, rating),
# and i call reusable code instead of duplicating code