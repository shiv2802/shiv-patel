from gtts import gTTS
import os
speech = input("what do you want to convert:   ")

text = speech

language = "en"
output = gTTS(text=text, lang=language, slow=True )


output.save("myspeech.mp3")
os.system("myspeech.mp3")
