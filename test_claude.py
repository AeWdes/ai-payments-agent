import anthropic
from dotenv import load_dotenv

load_dotenv()  # carica la API key dal file .env in modo sicuro

client = anthropic.Anthropic()

message = client.messages.create( # manda il messaggio con parametri a Claude
    model="claude-sonnet-4-6",    # model specifica quale modello usare
    max_tokens=1024,
    messages=[                    # messages è la conversazione — stesso formato da usare gli agenti
        {"role": "user", "content": "Ciao! Dimmi in una frase cosa sei."}
    ]
)

print(message.content[0].text)    # estrae il testo dalla risposta