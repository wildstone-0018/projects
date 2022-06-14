#Google Text to Speech
'''from gtts import gTTS
speech = gTTS("Hello good evening hope you are following")
#print(speech)
a = speech.save("audio.mp3")'''

from gtts import gTTS
import speech_recognition as sr
import time
from time import ctime
import re
import playsound
import uuid
import os
import webbrowser
import smtplib

#to make sure it listens
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening")
        audio = r.listen(source,phrase_time_limit=5)
    data = ""
    #Exception Handling
    try:
        data = r.recognize_google(audio,language='en-US')
        print("You said:"+data)
    except sr.UnknownValueError:
        print("I cannot hear you")
    except sr.RequestError as e:
        print("Request Failed")
    return data
#listen()

#Responding where we will make our virtual assistant to speak

def respond(String):
    print(String)
    tts = gTTS(text = String,lang = 'en-US')
    tts.save("speech.mp3")
    filename = "Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

#Virtual Assistant actions
def olivia(data):
    """give your actions"""
    if "how are you" in data:
        listening = True
        respond("Good and doing well")
    if "time" in data:
        listening = True
        respond(ctime())

    if "open google" in data.casefold():
        listening = True
        reg_ex = re.search('open google(.*)',data)
        url = "https://www.google.com/"
        if reg_ex:
            sub = reg_ex.group(1)
            url = url + 'r/'
        webbrowser.open(url)
        respond("Success")

    if "send mail" in data:
        listening = True
        respond("Whom should i send email to?")
        to = listen()
        edict = {'hello':'sowmyasribonagiri03@gmail.com','new':' '} #give mail ids
        toaddr = edict[to]
        respond("What is the Subject?")
        subject = listen()
        respond("What should i tell that person?")
        message = listen()
        content = 'Subject :{}\n\n{}'.format(subject,message)

        #init gmail SMTP
        mail = smtplib.SMTP('smtp.gmail.com',587)
        #identify the server
        mail.ehlo()
        mail.starttls()
        #login
        mail.login('','') #enter mailid and password make sure you enable less secure app access
        mail.sendmail('',toaddr,content) #enter your gmail username
        mail.close()
        respond('Email Sent')

    if "locate" in data:
        webbrowser.open('https://www.google.com/maps/search/'+data.replace("locate",""))
        result = "Located"
        respond("Located {}".format(data.replace("locate","")))
     
    if "stop" in data:
        listening =False
        print("Listening Stopped")
        respond("Okay get lost...")

    if "play" in data.casefold():
        webbrowser.open('https://www.youtube.com/results?search_query='+data.replace("play",""))
        result = "play"
        respond("play {}".format(data.replace("paly","")))
        
    if "open whatsapp" in data.casefold():
        listening = True
        reg_ex = re.search('open WhatsApp(.*)',data)
        url = "https://web.whatsapp.com/"
        if reg_ex:
            sub = reg_ex.group(1)
            url = url + 'r/'
        webbrowser.open(url)
        respond("Success")
        
    if "open gmail" in data.casefold():
        listening=True
        reg_ex=re.search('open Gmail(.*)',data)
        url="https://accounts.google.com/AccountChooser/signinchooser?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=AccountChooser"
        if reg_ex:
            sub=reg_ex.group(1)
            url=url+'r/'
            webbrowser.open(url)
            respond('success')
    if "open Instagram " in data.casefold():
        listening = True
        reg_ex = re.search('open Instagram(.*)',data)
        url ="https://www.instagram.com/"
        #"https://www.instagram.com/accounts/login/"
        if reg_ex:
            sub = reg_ex.group(1)
            url = url + 'r/'
        webbrowser.open(url)
        respond("Success")
    try:
        return listening
    except UnboundLocalError:
        print("call me if you need anything")

time.sleep(10)
respond("Hey sowmya how are you")
listening = True
while listening ==True:
    data = listen()
    listening = olivia(data)














    
    
        
    






