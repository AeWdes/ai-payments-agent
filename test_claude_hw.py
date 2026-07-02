import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()  # legge automaticamente la key dal .env

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, world"}],
)

# print(message.content) così stampa anche i metadati del content
print(message.content[0].text)