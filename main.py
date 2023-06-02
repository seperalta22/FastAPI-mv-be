from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app= FastAPI()
app.title = "My First API with FastAPI"
app.version = "0.0.1"
app.description = "This is my first API with FastAPI"

movies = [
    {
        "id": 1,
        "name": "The Shawshank Redemption",
        "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
        "genres": ["Drama"]
    },
    {
        "id": 2,
        "name": "The Godfather ",
        "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
        "genres": ["Crime", "Drama"]
    },
    {
        "id": 3,
        "name": "The Dark Knight",
        "casts": ["Christian Bale", "Heath Ledger", "Aaron Eckhart", "Michael Caine"],
        "genres": ["Action", "Crime", "Drama"]
    },
]

@app.get("/" ,tags=["Root"])
def message():
    return HTMLResponse(content="<h1>Welcome to my API</h1>", status_code=200)

@app.get("/api/movies", tags=["Movies"])
def get_movies():
    return movies

@app.get("/api/movies/{id}", tags=["Movies"])
def get_movie_by_id(id: int):
    for movie in movies:
        if(movie["id"] == id):
            return movie
    return {"Error": "Movie not found"}

#query parameter

@app.get("/api/movies/", tags=["Movies"])
def get_movies_by_genre(genre: str):
    genre = genre.capitalize()
    results = []
    for movie in movies:
        if(movie["genres"].count(genre) > 0):
            results.append(movie)

    if len(results) == 0:
        return {"Error": "Genre not found"}
    return results
    