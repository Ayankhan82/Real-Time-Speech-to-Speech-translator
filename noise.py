from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
import noisereduce as nr
import numpy as np

# A tuple containing all the language and
# codes of the language will be detected
dic = ('afrikaans', 'af', 'albanian', 'sq',
       'amharic', 'am', 'arabic', 'ar',
       'armenian', 'hy', 'azerbaijani', 'az',
       'basque', 'eu', 'belarusian', 'be',
       'bengali', 'bn', 'bosnian', 'bs', 'bulgarian',
       'bg', 'catalan', 'ca', 'cebuano',
       'ceb', 'chichewa', 'ny', 'chinese (simplified)',
       'zh-cn', 'chinese (traditional)',
       'zh-tw', 'corsican', 'co', 'croatian', 'hr',
       'czech', 'cs', 'danish', 'da', 'dutch',
       'nl', 'english', 'en', 'esperanto', 'eo',
       'estonian', 'et', 'filipino', 'tl', 'finnish',
       'fi', 'frisian', 'fy', 'galician',
       'gl', 'georgian', 'ka', 'german',
       'de', 'greek', 'el', 'gujarati', 'gu',
       'haitian creole', 'ht', 'hausa', 'ha',
       'hawaiian', 'haw', 'hebrew', 'he', 'hindi',
       'hi', 'hmong', 'hmn', 'hungarian',
       'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian',
       'id', 'irish', 'ga', 'italian',
       'it', 'japanese', 'ja', 'javanese', 'jw',
       'kannada', 'kn', 'kazakh', 'kk', 'khmer',
       'km', 'korean', 'ko', 'kurdish (kurmanji)',
       'ku', 'kyrgyz', 'ky', 'lao', 'lo',
       'latin', 'la', 'latvian', 'lv', 'lithuanian',
       'lt', 'luxembourgish', 'lb',
       'macedonian', 'mk', 'malagasy', 'mg', 'malay',
       'ms', 'malayalam', 'ml', 'maltese',
       'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian',
       'mn', 'myanmar (burmese)', 'my',
       'nepali', 'ne', 'norwegian', 'no', 'odia', 'or',
       'pashto', 'ps', 'persian', 'fa',
       'polish', 'pl', 'portuguese', 'pt', 'punjabi',
       'pa', 'romanian', 'ro', 'russian',
       'ru', 'samoan', 'sm', 'scots gaelic', 'gd',
       'serbian', 'sr', 'sesotho', 'st',
       'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si',
       'slovak', 'sk', 'slovenian', 'sl',
       'somali', 'so', 'spanish', 'es', 'sundanese',
       'su', 'swahili', 'sw', 'swedish',
       'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu',
       'te', 'thai', 'th', 'turkish',
       'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur', 'ug',
       'uzbek', 'uz',
       'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
       'yiddish', 'yi', 'yoruba',
       'yo', 'zulu', 'zu')

# Capture Voice
# takes command through microphone
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        # Perform noise reduction
        audio_data = np.frombuffer(audio.frame_data, dtype=np.int16)
        audio_data = nr.reduce_noise(y=audio_data, sr=audio.sample_rate)
        audio = sr.AudioData(audio_data.tobytes(), audio.sample_rate, audio.sample_width)

        query = r.recognize_google(audio, language='en-in')
        print(f"The User said: {query}\n")

        # Save the user's speech to a text file
        with open("user_speech.txt", "a") as text_file:
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
    with open("user_recog.txt", "a", encoding="utf-8") as text_file:  # Specify encoding as utf-8
        text_file.write(translated_text + "\n")

# Input from user
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

    to_lang = input("Enter the target language code: ").lower()  # Convert to lowercase

    while to_lang not in dic:
        print("Language code not found, please enter a valid language code.")
        to_lang = input("Enter the target language code: ").lower()

    if to_lang == 'urdu':
        to_lang = 'ur'  # Change 'urdu' to 'ur' for Urdu

    translate_and_speak(query, to_lang)
    i += 1
