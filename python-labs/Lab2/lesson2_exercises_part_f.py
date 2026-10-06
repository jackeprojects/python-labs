# Part F, Applied challenge: Personal media catalogue

# 1. & 2. Create catalogue of at least 8 items, each a dictionary with at least 4 fields, and store in a list
media1 = {"title": "The Legend of Zelda: Breath of the Wild", "category": "Game", "release_year": 2017, "genre": "Adventure"}
media2 = {"title": "Inception", "category": "Movie", "release_year": 2010, "genre": "Sci-Fi"}
media3 = {"title": "Dune", "category": "Book", "release_year": 1965, "genre": "Sci-Fi"}
media4 = {"title": "The Witcher 3: Wild Hunt", "category": "Game", "release_year": 2015, "genre": "RPG"}
media5 = {"title": "The Dark Knight", "category": "Movie", "release_year": 2008, "genre": "Action"}
media6 = {"title": "1984", "category": "Book", "release_year": 1949, "genre": "Dystopian"}
media7 = {"title": "Hades", "category": "Game", "release_year": 2020, "genre": "Roguelike"}
media8 = {"title": "Parasite", "category": "Movie", "release_year": 2019, "genre": "Thriller"}

media_catalogue = [media1, media2, media3, media4, media5, media6, media7, media8]


# 3. Create a set containing all unique genres represented in the catalogue
genres = {media1["genre"], media2["genre"], media3["genre"], media4["genre"], media5["genre"], media6["genre"], media7["genre"], media8["genre"]}
print(genres)


# 4. Create a tuple for each item's immutable identifier plus release year
media1["id"] = (media1["title"], media1["release_year"])
media2["id"] = (media2["title"], media2["release_year"])
media3["id"] = (media3["title"], media3["release_year"])
media4["id"] = (media4["title"], media4["release_year"])
media5["id"] = (media5["title"], media5["release_year"])
media6["id"] = (media6["title"], media6["release_year"])
media7["id"] = (media7["title"], media7["release_year"])
media8["id"] = (media8["title"], media8["release_year"])
print(media1["id"])


# 5. Perform at least 10 manual operations that demonstrate nested indexing, membership, and collection methods
print(media_catalogue[3]["title"])
print(media_catalogue[6]["genre"])
print("Sci-Fi" in genres)
print("Dune" == media_catalogue[2]["title"])

media_catalogue[0]["genre"] = "Open-World"
print(media_catalogue[0]["genre"])

media_catalogue[2].update({"re-released": True})
print(media_catalogue[2])

genres.add("Puzzle")
print(genres)

genres.discard("Puzzle")
print(genres)

print(media_catalogue[5]["id"][1])
print(len(media_catalogue))


# 6. Print a clean summary of the catalogue, without loops
print(f"{media1['title']} ({media1['release_year']}) - {media1['category']}, {media1['genre']}")
print(f"{media2['title']} ({media2['release_year']}) - {media2['category']}, {media2['genre']}")
print(f"{media3['title']} ({media3['release_year']}) - {media3['category']}, {media3['genre']}")
print(f"{media4['title']} ({media4['release_year']}) - {media4['category']}, {media4['genre']}")
print(f"{media5['title']} ({media5['release_year']}) - {media5['category']}, {media5['genre']}")
print(f"{media6['title']} ({media6['release_year']}) - {media6['category']}, {media6['genre']}")
print(f"{media7['title']} ({media7['release_year']}) - {media7['category']}, {media7['genre']}")
print(f"{media8['title']} ({media8['release_year']}) - {media8['category']}, {media8['genre']}")