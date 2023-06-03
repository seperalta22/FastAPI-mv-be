from typing import Optional
from fastapi import Depends, FastAPI, HTTPException, Query, Path, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from fastapi.security import HTTPBearer
from jwt_manager import create_token, validate_token
import jwt

app = FastAPI()
app.title = "My First API with FastAPI"
app.version = "0.0.1"
app.description = "This is my first API with FastAPI"


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data["username"] != "admin":
            raise HTTPException(status_code=401, detail="Invalid username or password")
        return data


class User(BaseModel):
    username: str
    password: str


class Movie(BaseModel):
    id: Optional[int] = Field(None, title="ID of the movie", gt=0)
    name: str = Field(..., title="Name of the movie", min_length=2, max_length=50)
    casts: list = Field(..., title="Casts of the movie")
    genres: list = Field(..., title="Genres of the movie")


movies = [
    {
        "id": 1,
        "name": "The Shawshank Redemption",
        "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
        "genres": ["Drama"],
    },
    {
        "id": 2,
        "name": "The Godfather ",
        "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
        "genres": ["Crime", "Drama"],
    },
    {
        "id": 3,
        "name": "The Dark Knight",
        "casts": ["Christian Bale", "Heath Ledger", "Aaron Eckhart", "Michael Caine"],
        "genres": ["Action", "Crime", "Drama"],
    },
]


@app.get("/", tags=["Root"])
def message():
    return HTMLResponse(content="<h1>Welcome to my API</h1>", status_code=200)


@app.get("/api/movies", tags=["Movies"])
def get_movies(depends: dict = Depends(JWTBearer())):
    return movies


@app.get("/api/movies/{id}", tags=["Movies"])
def get_movie_by_id(id: int):
    for movie in movies:
        if movie["id"] == id:
            return movie
    return {"Error": "Movie not found"}


# query parameter


@app.get("/api/movies/", tags=["Movies"])
def get_movies_by_genre(genre: str):
    genre = genre.capitalize()
    results = []
    for movie in movies:
        if movie["genres"].count(genre) > 0:
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
        if movies[i]["id"] == id:
            movies[i] = movie
            return {"Message": "Movie updated successfully"}
    return {"Error": "Movie not found"}


@app.delete("/api/movies/{id}", tags=["Movies"])
def delete_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
            return {"Message": "Movie deleted successfully"}
    return {"Error": "Movie not found"}


# Login


@app.post("/api/login", tags=["Login"])
def login(user: User):
    if user.username == "admin" and user.password == "admin":
        token: str = create_token(user.dict())
    return {"token": token}
