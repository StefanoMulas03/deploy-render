from fastapi import FastAPI
from textblob import TextBlob

app = FastAPI()

@app.get("/")
def homepage(frase: str):
    blob = TextBlob(frase)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        sentiment = "positivo"
    elif sentiment < 0:
        sentiment = "negativo"
    else:
        sentiment = "neutro"
    return "Il sentiment della frase è: " + str(sentiment)


