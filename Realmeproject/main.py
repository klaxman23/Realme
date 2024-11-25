from fastapi import FastAPI
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel

app = FastAPI()

@app .get("/")

def my_fun():
    return {"message": "Please learn the data science and python fastapi"}
