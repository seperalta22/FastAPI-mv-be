from fastapi import Body, FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app= FastAPI()
app.title = "My First API with FastAPI"
app.version = "0.0.1"
app.description = "This is my first API with FastAPI"

class Movie(BaseModel):
    id: int | None
    name: str
    casts: list
    genres: list

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
    
@app.post("/api/movies", tags=["Movies"])
def create_movie(movie: Movie):
    movies.append(movie)
    return {"Success": "Movie created successfully"}

@app.put("/api/movies/{id}", tags=["Movies"])
def update_movie(id: int, movie: Movie):
    for i in range(len(movies)):
        if(movies[i]["id"] == id):
            movies[i] = movie
            return {"Message": "Movie updated successfully"}
    return {"Error": "Movie not found"}


@app.delete("/api/movies/{id}", tags=["Movies"])
def delete_movie(id: int):
    for movie in movies:
        if(movie["id"] == id):
            movies.remove(movie)
            return {"Message": "Movie deleted successfully"}
    return {"Error": "Movie not found"}