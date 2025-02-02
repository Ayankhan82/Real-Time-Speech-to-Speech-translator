from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
flag = 0

dic = ('english','en','hindi','hi')

def takecommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("listening.....")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing.....")
		query = r.recognize_google(audio, language='en-in')
		print(f"The User said {query}\n")
	except Exception as e:
		print("say that again please.....")
		return "None"
	return query

query = takecommand()
while (query == "None"):
	query = takecommand()
def destination_language():
	print("Enter the language in which you\
	want to convert : Ex. Hindi , English , etc.")
	print()
	to_lang = takecommand()
	while (to_lang == "None"):
		to_lang = takecommand()
	to_lang = to_lang.lower()
	return to_lang

to_lang = destination_language()

while (to_lang not in dic):
	print("Language in which you are trying\
	to convert is currently not available ,\
	please input some other language")
	print()
	to_lang = destination_language()

to_lang = dic[dic.index(to_lang)+1]

translator = Translator()

text_to_translate = translator.translate(query, to_lang)

text = text_to_translate.text

speak = gTTS(text=text, lang=to_lang, slow=False)#gtts

# Using save() method to save the translated
# speech in capture_voice.mp3
speak.save("captured_voice.mp3")

# Using OS module to run the translated voice.
playsound('captured_voice.mp3')
os.remove('captured_voice.mp3')

print(text)
