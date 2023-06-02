from fastapi import FastAPI

app= FastAPI()
app.title = "My First API with FastAPI"
app.version = "0.0.1"
app.description = "This is my first API with FastAPI"

@app.get("/" ,tags=["Root"])
def message():
    return {"message": "Hello World"}