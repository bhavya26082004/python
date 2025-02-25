#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install gTTS')


# In[30]:


from gtts import gTTS


# In[31]:


convert = gTTS(text='I like this NLP. How about dude!', lang='en', slow=False)
convert.save('audio.mp3')


# In[32]:


get_ipython().system('pip install pyttsx3')


# In[7]:


import pyttsx3, time 
engine = pyttsx3.init()
engine.say('Hi, I am text to speach')
engine.runAndWait()


# In[8]:


text=['This is introduction to NLP','It is likely to be useful, to people ',\
      'Machine learning is the new electricity','There would be less hype around AI and more action going forward',\
      'python is the best tool!','R is good langauage','I like this book',\
      'I want more books like this']


# In[9]:


engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()


# In[10]:


import pyttsx3
engine = pyttsx3.init()

rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 180)

volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.say('My current speaking volume is ' + str(volume))
engine.runAndWait()
engine.stop()


# In[15]:


get_ipython().system('pip install translate')


# In[16]:


from translate import Translator
translator = Translator(to_lang="kn")  
translation = translator.translate("how are u the")
translation


# In[17]:


from translate import Translator
translator = Translator(to_lang="te")
translation = translator.translate("How are you?")
translation


# In[8]:


get_ipython().system('pip install python-vlc')


# In[10]:


import vlc
p = vlc.MediaPlayer("audio.mp3")
p.play()


# In[2]:


get_ipython().system('pip install playsound')


# In[4]:


import playsound as pl 
pl.playsound('audio.mp3')
print('playing sound using playsound')


# In[11]:


get_ipython().system('pip install SpeechRecognition')


# In[12]:


get_ipython().system('pip install PyAudio')


# In[15]:


import speech_recognition as sr


# In[17]:


import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Please say something")
    audio = r.listen(source)
try:
    print("I think you said: " + r.recognize_google(audio))
except:
    pass


# In[ ]:




