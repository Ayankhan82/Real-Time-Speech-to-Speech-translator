# Real-Time Speech-to-Speech Translator

This project is a real-time speech-to-speech translation tool that captures spoken input, translates it into a target language, and plays the translated speech.

## Features
- Captures voice input via a microphone
- Supports multiple languages for translation
- Converts translated text into speech
- Saves both input and translated text to files

## Installation

### Prerequisites
- Python 3.7 or later
- A working microphone

### Install Dependencies
Run the following command to install the required packages:
```sh
pip install -r requirements.txt
```

Alternatively, install each package individually:
```sh
pip install SpeechRecognition googletrans==4.0.0-rc1 gtts playsound pyaudio
```

## Usage
Run the Python script:
```sh
python ProposedModel.py
```

### Steps:
1. Select an option:
   - `1`: Speak a sentence to translate.
   - `2`: Input a sentence manually.
2. Enter the target language code (e.g., `hi` for Hindi, `es` for Spanish).
3. The program will translate and play the translated speech.

## Supported Languages
This program supports multiple languages. Some common language codes:
- English (`en`)
- Hindi (`hi`)
- Spanish (`es`)
- German (`de`)
- French (`fr`)
- Russian (`ru`)
- Chinese (`zh-cn`)

For a full list of supported languages, refer to [Google Translate language codes](https://cloud.google.com/translate/docs/languages).

## Troubleshooting
### Common Issues & Fixes
1. **Microphone Not Working?**
   - Ensure your microphone is enabled and working.
   - Run the following to check available microphones:
     ```python
     import speech_recognition as sr
     print(sr.Microphone.list_microphone_names())
     ```
2. **Translation Not Working?**
   - Ensure you have installed `googletrans==4.0.0-rc1`.
   - Run:
     ```sh
     pip uninstall googletrans
     pip install googletrans==4.0.0-rc1
     ```
3. **Error: 'No module named pyaudio'**
   - If `pyaudio` fails to install, try:
     ```sh
     pip install pipwin
     pipwin install pyaudio
     ```

## Contributing
Feel free to submit pull requests or report issues to improve this project!

## License
This project is licensed under the MIT License.

