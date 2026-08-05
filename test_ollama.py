from ollama import Client

client = Client(host="http://127.0.0.1:11434")

response = client.chat(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "user",
            "content": "Say hello"
        }
    ]
)

print(response)