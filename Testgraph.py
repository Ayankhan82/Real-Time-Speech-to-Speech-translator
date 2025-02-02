from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
import time
import matplotlib.pyplot as plt

# Languages
dic = ('afrikaans','af', 'arabic','ar',
       'bengali','bn','english', 'en','german','de',
        'gujarati','gu','hindi','hi', 'indonesian','id',
        'italian','it','japanese','ja', 'korean','ko',
       'latin','la', 'malayalam','ml' ,'marathi','mr',
       'nepali','ne', 'portuguese','pt',
        'russian','ru', 'spanish', 'es','french','fr',
        'tamil','ta', 'telugu','te' ,'turkish','tr','urdu', 'ur', 
       )

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.non_speaking_duration = 0.1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"The User said: {query}\n")

        with open("inputSpeech.txt", "a") as text_file:
            text_file.write(query + "\n")

        return query
    except Exception as e:
        print("Say that again, please...")
        return "None"

def count_words(text):
    # Counting the number of words in the input text
    words = text.split()
    return len(words)

def translate_and_speak(text, to_lang):
    start_time = time.time()
    translator = Translator()

    text_to_translate = translator.translate(text, dest=to_lang)
    translated_text = text_to_translate.text

    speak = gTTS(text=translated_text, lang=to_lang, slow=False)
    speak.save("translated_voice.mp3")

    playsound("translated_voice.mp3")
    os.remove("translated_voice.mp3")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Execution Time Elapsed: {elapsed_time:.2f} Seconds")
    print(translated_text)

    with open("outputSpeech.txt", "a", encoding="utf-8") as text_file:
        text_file.write(translated_text + "\n")

    return elapsed_time

execution_times = []
word_counts = []  # To store the number of words for labeling on the X-axis

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
        with open("inputSpeech.txt", "a") as text_file:
            text_file.write(query + "\n")
    else:
        print("Invalid choice. Please select 1 or 2.")
        continue

    to_lang = input("Enter the target language code: ").lower()

    while to_lang not in dic:
        print("Language code not found, please enter a valid language code.")
        to_lang = input("Enter the target language code: ").lower()

    if to_lang == 'urdu':
        to_lang = 'ur'

    elapsed_time = translate_and_speak(query, to_lang)
    execution_times.append(elapsed_time)
    
    # Counting words in the input text
    word_count = count_words(query)
    word_counts.append(word_count)

    i += 1

# Plotting the execution times in scatter format with word count on X-axis
plt.scatter(word_counts, execution_times, color='blue', marker='o')
plt.plot(word_counts, execution_times, linestyle='-', color='orange', marker='o')
plt.xlabel('Number of Words in Input')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs Number of Words in Input')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.tight_layout()  # Adjust layout for better appearance
plt.show()
