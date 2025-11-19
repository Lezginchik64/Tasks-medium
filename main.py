from gtts import gTTS
from playsound import playsound

text = "Привет пока"
tts = gTTS(text=text, lang='ru', slow=False)
tts.save("test.mp3")
playsound("test.mp3")