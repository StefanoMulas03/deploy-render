from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def homepage():
    return "Ciao, questa è l'homepage"



@app.get("/es1")
def homepage():
    return "hello world"

@app.get("/es2")
def homepage(nome, cognome):
    return "ciao" + nome + cognome



listName = []

@app.post("/aggiungi-utente")
def aggiungi_utente(username: str):
    listName.append(username)
    return "Utente " + username + " aggiunto con successo alla lista"




@app.get("/cerca-utente")
def cerca_utente(cercaNome: str):
    if cercaNome in listName:
        return "Il nome è presente nella lista"
    else:
        return "Il nome non è presente nella lista"



@app.get("/totale-utenti")
def totale_utenti():
    return "Il totale degli utenti è: " + str(len(listName))



@app.delete("/elimina-utente")
def elimina_utente(nameDelete):
    if nameDelete in listName:
        listName.remove(nameDelete)
        return "Il nome è stato eliminato dalla lista"
    else:
        return "Errore, il nome non è presente nella lista"