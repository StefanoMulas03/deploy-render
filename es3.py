from textblob import TextBlob

frase = "I'm happy!"
blob = TextBlob(frase)

# Se sentiment > 0 allora -> positivo
# Se sentiment < 0 allora -> negativo
# Se sentiment = 0 allora -> neutro
sentiment = blob.sentiment.polarity
print(sentiment)


