from fastapi import FastAPI
from fastapi import FastAPI, Header, Request, Response

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
