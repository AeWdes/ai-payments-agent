import requests

response = requests.get("https://api.github.com")
#requests.get() ha mandato una richiesta al server di GitHub

print(response.status_code)
#200 è lo status code che significa "successo" (404 = non trovato, 500 = errore server, ecc.)

print(response.json())
#.json() ha trasformato la risposta in un dizionario Python che puoi usare nel codice
# in questo caso la mappa completa di tutti gli endpoint dell'API GitHub 