from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app= FastAPI()
app.title = "My First API with FastAPI"
app.version = "0.0.1"
app.description = "This is my first API with FastAPI"

movies = [
    {
        "name": "The Shawshank Redemption",
        "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
        "genres": ["Drama"]
    },
    {
        "name": "The Godfather ",
        "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
        "genres": ["Crime", "Drama"]
    },
    {
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
    