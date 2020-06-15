import sounddevice as sd
from scipy.io.wavfile import write
import os




fs = 44100
seconds = 20

print("started")

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()
write('output2.wav',  fs, myrecording)
os.startfile("output2.wav")