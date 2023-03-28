from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/post")
async def get():
    return {"data": "This is coming from this post"}

@app.get("/post")
async def get():
    return {"data": "This is coming new post"}