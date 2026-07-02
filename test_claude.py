import anthropic
from dotenv import load_dotenv

load_dotenv()  # carica la API key dal file .env

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Ciao! Dimmi in una frase cosa sei."}
    ]
)

print(message.content[0].text)