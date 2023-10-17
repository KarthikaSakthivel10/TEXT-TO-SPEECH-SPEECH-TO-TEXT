
import speech_recognition as sr
recognizer = sr.Recognizer()
audio_file = "PATH OF AUDIO FILE IN WAV FORMAT"  #TO  CONVERT MP3 FILE INTO WAV FORMATE, IMPORT FFMPEG
with sr.AudioFile(audio_file) as source:
    audio = recognizer.record(source)
try:
    text = recognizer.recognize_google(audio)
    print("Transcribed text: " + text)
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError as e:
    print("Sorry, there was an error with the speech recognition service: {0}".format(e))
