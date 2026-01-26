from ollama import chat
from ollama import ChatResponse
import ollama

print("Willkommen zum AI Chatbot")

while True:
  user_input = input("\n\033[31mUser: \033[0m")
  response: ChatResponse = chat(model='llama3.1:8b', messages=[
    {
      'role': 'user',
      'content': user_input,
      "max_tokens": 200
    },
  ])
  print("\033[32mOutput: \033[0m", end="", flush=True)

  stream = ollama.chat(
        model='llama3.1:8b',
        messages=[{'role': 'user', 'content': user_input}],
        stream=True
    )
  for chunk in stream:
    print(chunk.message.content, end="", flush=True)
