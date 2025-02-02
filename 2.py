from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

# Dictionary to map full language names to their language codes
language_mapping = {
    'afrikaans': 'af', 'arabic': 'ar', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg',
    'english': 'en', 'georgian': 'ka', 'german': 'de', 'gujarati': 'gu', 'hindi': 'hi', 
    'indonesian': 'id', 'italian': 'it', 'japanese': 'ja', 'korean': 'ko',
    'latin': 'la', 'malayalam': 'ml', 'marathi': 'mr', 'nepali': 'ne', 'persian': 'fa',
    'portuguese': 'pt', 'punjabi': 'pa', 'russian': 'ru', 'sindhi': 'sd', 'spanish': 'es',
    'tamil': 'ta', 'telugu': 'te', 'turkish': 'tr', 'urdu': 'ur',
}

# Capture Voice
# takes command through the microphone
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # Adjust pause_threshold and non_speaking_duration here
        r.pause_threshold = 0.1
        r.non_speaking_duration = 0.1

        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"The User said: {query}\n")

        # Save the user's speech to a text file
        with open("inputSpeech.txt", "a") as text_file:
            text_file.write(query + "\n")

        return query
    except Exception as e:
        print("Say that again, please...")
        return "None"

def translate_and_speak(text, to_lang):
    translator = Translator()

    text_to_translate = translator.translate(text, dest=to_lang)
    translated_text = text_to_translate.text

    speak = gTTS(text=translated_text, lang=to_lang, slow=False)
    speak.save("translated_voice.mp3")

    playsound("translated_voice.mp3")
    os.remove("translated_voice.mp3")

    print(translated_text)
    with open("outputSpeech.txt", "a", encoding="utf-8") as text_file:  
        text_file.write(translated_text + "\n")

i = 0
while i < 3:
    print("Select an option:")
    print("1. Speak a sentence to translate.")
    print("2. Input a sentence to translate.")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        query = takecommand()
        while query == "None":
            query = takecommand()
    elif choice == "2":
        query = input("Enter the text to translate: ")
    else:
        print("Invalid choice. Please select 1 or 2.")
        continue

    to_lang = input("Enter the target language: ").lower()

    # Correct full language names to language codes
    if to_lang in language_mapping:
        to_lang = language_mapping[to_lang]
    else:
        print("Language not found. Please enter a valid language name.")
        continue

    translate_and_speak(query, to_lang)
    i += 1
