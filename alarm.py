import _datetime
import os

from gtts import gTTS



alarm_hor = int(input("what hour:   "))
alarm_min = int(input("what min:   "))
alarm_sec = int(input("what sec:   "))

am_pm = str(input("am or pm:  "))
what = input("what alarm do you want to save:   ")

if (am_pm == "pm"):
    alarm_hor = alarm_hor + 12

myText = "you saved the alarm named" + what
language = 'en'

output = gTTS(text=myText, lang=language, slow=False)


while (1 == 1) :
    if (alarm_hor == _datetime.datetime.now().hour and alarm_min == _datetime.datetime.now().minute and alarm_sec == _datetime.datetime.now().second):
        output.save("speech.mp3")

        os.system("start speech.mp3")

        print("Time to do " + what)
        break

print("closed")