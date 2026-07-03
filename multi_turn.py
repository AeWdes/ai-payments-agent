import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

# La storia della conversazione — cresce ad ogni turno
conversation = []

print("Chatta con Claude! (scrivi 'esci' per terminare)\n")

while True:
    user_input = input("Tu: ")
    
    if user_input.lower() == "esci":
        break
    
    # Aggiungi il messaggio utente alla storia
    conversation.append({"role": "user", "content": user_input})
    
    # Manda tutta la storia ad ogni chiamata
    #response = client.messages.create(
    #    model="claude-sonnet-4-6",
    #    max_tokens=1024,
    #    messages=conversation
    #)
    # response come sopra, ma introduco system per dire a Claude chi è e come deve comportarsi
    response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system="Sei un assistente specializzato in pagamenti Bitcoin. \
            Rispondi sempre in italiano. \
            Sei preciso, conciso e attento alla sicurezza.",
    messages=conversation
)
    
    assistant_message = response.content[0].text
    
    # Aggiungi la risposta di Claude alla storia
    conversation.append({"role": "assistant", "content": assistant_message})
    
    print(f"Claude: {assistant_message}\n")