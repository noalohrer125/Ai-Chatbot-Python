import ollama
import sys

print("Willkommen zum AI Chatbot")
print("-------------------------")
print()
print("Um denn Chat zu beenden: \033[36m/Exit\033[0m")
print("Um einen Neuen Chat zu öffnen: \033[36m/New Chat\033[0")

all_messages = []

while True:
  user_input = input("\n\033[1;31mUser: \033[0m")
  all_messages.append({"role": "user", "content": user_input})
  print("\033[1;32mOutput: \033[0m", end="", flush=True)
  output_chatbot = ""
  stream = ollama.chat(
    model='llama3.1:8b',
    messages=all_messages,
      stream=True,
      )
  for chunk in stream:
      print(chunk.message.content, end="", flush=True)
      output_chatbot += chunk.message.content
  all_messages.append({"role": "assistant", "content": output_chatbot})