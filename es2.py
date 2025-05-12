from langdetect import detect

testo = "Ciao, sto parlando in italiano"
lingua = detect(testo)

print(f"La lingua rilevata è: {lingua}")