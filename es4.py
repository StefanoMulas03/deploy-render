from fastapi import FastAPI
from langdetect import detect

app = FastAPI()

@app.get("/")
def homepage(frase: str):
    lingua = detect(frase)
    return "La lingua rilevata è: " + lingua


