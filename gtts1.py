from gtts import gTTS
import os
from playsound import playsound
myt='Hello, Mr. Chirag Garg, You are a good boy, Thank You all for your Precious Time' 
myo=gTTS(text=myt, lang='en', slow=False)
myo.save("1.mp3")
os.system('start 1.mp3')
#playsound('D:\computer programs\python\1.mp3', True)
