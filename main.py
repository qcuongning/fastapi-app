from fastapi import FastAPI
from fastapi import FastAPI, Header, Request, Response

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/phuong')
async def phuongEvent(request: Request):
    body = await request.body()
    print(body)
    return "ok" 