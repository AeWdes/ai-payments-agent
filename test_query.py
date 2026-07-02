import requests

#cerchiamo repository GitHub che parlano di "bitcoin"
response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "bitcoin", "sort": "stars", "per_page": 5, "page": 2}
)
#params viene automaticamente trasformato in ?q=bitcoin&sort=stars&per_page=5 nell'URL.
#stampa i primi 5 repository che contengono "bitcoin" con più stelle
#per avere i repository dal 6 al 10 aggiungo il parametro "page": 2



data = response.json()
for repo in data["items"]:
    print(repo["full_name"], "-", repo["stargazers_count"], "stars")