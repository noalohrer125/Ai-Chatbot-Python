import ollama
import sys
import os

def startup_messages():
  print("Willkommen zum AI Chatbot")
  print("-------------------------" \
  "\n")

def help_messages():
  print("Um den Chat zu beenden: \033[36m/Exit\033[0m")
  print("Um einen neuen Chat zu öffnen: \033[36m/New Chat\033[0m")
  print("Um die Modell Infos anzuschauen: \033[36m/Info\033[0m")
  print("Um Chat aufzuräumen: \033[36m/Clear\033[0m")
  print("Um die Commands aufzurufen: \033[36m/Help\033[0m")

def show_model_infos():
  model_name = "\033[36mLlama3.1:8b\033[0m"
  model_owner = "\033[36mMeta\033[0m"
  release_date_model = "\033[36mJuli 23, 2024\033[0m"
  print("Model Name: ",model_name)
  print("Model Owner: ",model_owner)
  print("Model Release Date: ",release_date_model)

def clear_console():
  os.system("cls" if os.name == "nt" else "clear")

def shutdown_ollama():
  os.system("ollama stop llama3.1:8b")

startup_messages()
help_messages()

all_messages = [{
  "role": "system",
  "content": (
    "Das hier sind deine Grenzen die du als Ai Chatbot nicht überschreiten oder einhalten solltest."
    "Du bist ein Ai Chatbot dessen Standardsprache Deutsch ist."
    "Du bist ein Ai Chatbot der die Sprache (Deutsch) nicht während dem Nutzen aufeinmal ändert."
    "Falls der User auf eine andere Sprache wechseln will muss er das zuerst bestätigen."
    "Das Nutzen von englischen Wörtern ist erlaubt aber dabei bleibt man bei der Standardsprache."
    "Der Output sollte hilfreich, kurz und prägnant sein."
    "Du versuchst immer so hilfreich wie möglich zu sein um den User zu helfen."
    "Falls der Output länger wird kannst du den User fragen ob das okay ist und der sagt dann ob das okay ist oder nicht."
    "Wenn du etwas nicht was der User fragt nicht weisst, dann sage ihm das und halte dich kurz."
  )
}]

try:
  while True:
    user_input = input("\n\033[1;31mUser: \033[0m")

    if user_input.lower() == "/exit":
      shutdown_ollama()
      clear_console()
      try:
        sys.exit("Chat wird beendet...")
      except Exception:
        print("Chat wird beendet...")
        break

    elif user_input.lower() == "/help":
      help_messages()
      continue

    elif user_input.lower() == "/new chat":
      try:
        clear_console()
      except Exception as error:
        print("OS System Fehler: ",error)
      print("\033[1mNeuer Chat:\033[0m")
      help_messages()
      all_messages = [{
      "role": "system",
      "content": (
      "Das hier sind deine Grenzen die du als Ai Chatbot nicht überschreiten oder einhalten solltest."
      "Du bist ein Ai Chatbot dessen Standardsprache Deutsch ist."
      "Du bist ein Ai Chatbot der die Sprache (Deutsch) nicht während dem Nutzen aufeinmal ändert."
      "Falls der User auf eine andere Sprache wechseln will muss er das zuerst bestätigen."
      "Das Nutzen von englischen Wörtern ist erlaubt aber dabei bleibt man bei der Standardsprache."
      "Der Output sollte hilfreich, kurz und prägnant sein."
      "Du versuchst immer so hilfreich wie möglich zu sein um den User zu helfen."
      "Falls der Output länger wird kannst du den User fragen ob das okay ist und der sagt dann ob das okay ist oder nicht."
      "Wenn du etwas nicht was der User fragt nicht weisst, dann sage ihm das und halte dich kurz."
      )
      }]
      continue
  
    elif user_input.lower() == "/info":
      show_model_infos()
      continue

    elif user_input.lower() == "/clear":
      try:
        clear_console()
      except Exception as error:
        print("OS System Fehler: ",error)
      print("Chat wurde aufgeräumt.")
      continue
    
    elif user_input == "":
      print("Fehler: Nachricht leer")
      continue

    else:
      try:
        all_messages.append({"role": "user", "content": user_input})
      except Exception as error:
        print("Fehler beim hinzufügen von Nachrichten zum Speicher (User Input): ", error)

      print("\033[1;32mOutput: \033[0m", end="", flush=True)
      output_chatbot = ""

      try:
        # Schnittstelle für Ollama In/Output
        stream = ollama.chat(
              model='llama3.1:8b',
              messages=all_messages,
              stream=True,
          )

        for chunk in stream:
          print(chunk.message.content, end="", flush=True)
          output_chatbot += chunk.message.content

      except ollama.ResponseError as error:
        print("Ollama-Fehler (Response Error):", error)

      except ollama.RequestError as error:
        print("Ollama Fehler (Request Error): ",error)

      except Exception as error:
        print("Allgemeiner Fehler:", error)

      try:
        all_messages.append({"role": "assistant", "content": output_chatbot})
      except Exception as error:
        print("Fehler beim hinzufügen von Nachrichten zum Speicher (Output Chatbot): ", error)

except KeyboardInterrupt:
  try:
    shutdown_ollama()
  except Exception as error:
    print("Ollama konnte ich nicht Beendet werden da Ollama nicht Läuft: ", error)
  except KeyboardInterrupt:
    pass
  print("\nProgramm wurde durch Benutzer unterbrochen. (KeyboardInterrupt)")