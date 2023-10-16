from gtts import gTTS
import os

text = input()
tts = gTTS(text, lang='en')
tts.save("output.mp3")
os.system("vlc output.mp3")
