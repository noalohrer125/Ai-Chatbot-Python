import ollama
import sys
import os

def startupmessage():
  print("Willkommen zum AI Chatbot")
  print("-------------------------")
  print()
  print("Um denn Chat zu beenden: \033[36m/Exit\033[0m")
  print("Um einen Neuen Chat zu öffnen: \033[36m/New Chat\033[0m")
  print("Um die Commands aufzurufen: \033[36m/Help\033[0m")

def helpmessage():
  print("Um denn Chat zu beenden: \033[36m /Exit\033[0m")
  print("Um einen Neuen Chat zu öffnen: \033[36m/New Chat\033[0m")

startupmessage()

all_messages = [{
  "role": "system",
  "content": (
    "Das hier sind deine Grenzen die du als Ai Chatbot nicht überschreiten oder einhalten solltest."
    "Du bist ein Ai Chatbot dessen Standardsprache deutsch ist."
    "Du bist ein Ai Chatbot der die Sprache (Deustch) nicht während dem Nutzen aufeinmal ändert."
    "Falls der User auf eine andere Spache wechseln will muss er das zuerst bestätigen."
    "Das Nutzen von Englischen Wörtern ist erlaubt aber dabei bleibt man bei der Standardsprache."
    "Der Output sollte Hilfreich, Kurz und Prägnant sein."
    "Du versuchst immer so hilfreich wie möglich zu sein um den User zu helfen."
    "Falls der Output länger wird kannst du den User fragen ob das okay ist und der sagt dann ob das okay ist oder nicht."
    "Wenn du etwas nicht was der User fragt nicht weisst, dann sage ihm das und halte dich Kurz."
  )
}]


  


try:
  while True:
    user_input = input("\n\033[1;31mUser: \033[0m")
    # User Commands
    if user_input.lower() == "/exit":
      os.system("ollama stop llama3.1:8b") # Stoppt Ollama (gegen RAM Probleme)
      sys.exit("Chat wird beendet...")
    elif user_input.lower() == "/help":
      helpmessage()
      continue
    elif user_input.lower() == "/new chat":
      try:
        os.system("cls") # Wird genutzt um vorherige nachrichten zu löschen
      except Exception as error:
        print("OS System Fehler: ",error)
      print("\033[1mNeuer Chat:\033[0m")
      helpmessage()

      all_messages = [{
      "role": "system",
      "content": (
      "Das hier sind deine Grenzen die du als Ai Chatbot nicht überschreiten oder einhalten solltest."
      "Du bist ein Ai Chatbot dessen Standardsprache deutsch ist."
      "Du bist ein Ai Chatbot der die Sprache (Deustch) nicht während dem Nutzen aufeinmal ändert."
      "Falls der User auf eine andere Spache wechseln will muss er das zuerst bestätigen."
      "Das Nutzen von Englischen Wörtern ist erlaubt aber dabei bleibt man bei der Standardsprache."
      "Der Output sollte Hilfreich, Kurz und Prägnant sein."
      "Du versuchst immer so hilfreich wie möglich zu sein um den User zu helfen."
      "Falls der Output länger wird kannst du den User fragen ob das okay ist und der sagt dann ob das okay ist oder nicht."
      "Wenn du etwas nicht was der User fragt nicht weisst, dann sage ihm das und halte dich Kurz."
      )
    }]
      continue
    else:
      try:
        all_messages.append({"role": "user", "content": user_input})
      except Exception as error:
        print("Fehler beim hinzufügen von Nachrichten zum Speicher (User Input): ", error)

      print("\033[1;32mOutput: \033[0m", end="", flush=True)
      output_chatbot = ""

      try:
        stream = ollama.chat(
              model='llama3.1:8b',
              messages=all_messages,
              stream=True,
          )

        for chunk in stream:
          print(chunk.message.content, end="", flush=True)
          output_chatbot += chunk.message.content

      except ollama.ResponseError or ollama.RequestError as error:
        print("Ollama-Fehler:", error)

      except Exception as error:
        print("Allgemeiner Fehler:", error)

      try:
        all_messages.append({"role": "assistant", "content": output_chatbot})
      except Exception as error:
        print("Fehler beim hinzufügen von Nachrichten zum Speicher (Output Chatbot): ", error)
except KeyboardInterrupt:
  os.system("ollama stop llama3.1:8b")
  print("\nProgramm wurde durch Benutzer unterbrochen. (KeyboardInterrupt)")