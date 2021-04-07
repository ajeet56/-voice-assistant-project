#Building an application of Desktop Voice Assistant

import pyttsx3 #It is used for conversion of text to speech which is written by programmer in program
import datetime#Built-in module
import speech_recognition as sr #This module is used to recognize user voice (mean what they want to say/ask)
import wikipedia #Module for searching on wikipedia
import webbrowser #Built-in module to open youtube,google,stackoverflow and more...
import os #Built-in module to deal with all directory present in the system
import smtplib #Buit-in module to sent email from gmail
from playsound import playsound


engine=pyttsx3.init("sapi5")#It is used to take voice from users
voices=engine.getProperty("voices")#An built-in API provides by window to get voices
#print(voices[1].id) #It only acknowledge that what type of voices programmer want
engine.setProperty("voice",voices[1].id)#Set the voices type for male if we want to change for male then we write [0].id IN print()



def speak(audio): #This is the first declarative function that helps to speak jarvis
    engine.say(audio)
    engine.runAndWait()


def wishMe():#It is used to wish in specific way by using time therefore we have to import datetime module
    hour=int(datetime.datetime.now().hour)#typecasted in int
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<15 :
        speak("Good Afternoon!")

    elif hour>=15 and hour<18 :
        speak("Good Evening!")

    else:
        speak("Good Night!")
    
    speak("I am Jarvis Sir,please tell me how I may help you")

def takeCommand():
    #It takes (Audio) microphone input from the user, convert it to the string and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        #r.energy_threshold = 300  # minimum audio energy to consider for recording
        r.pause_threshold = 0.6 #Wait for seconds of non-speaking audio before a phrace is considered complete(means it deals with recognition time speed)
        audio=r.listen(source)

    try: #If error occur in recognizing
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)#It will give the error to recognize the audio of user 

        print("Say that again please....")
        return "None"#Return NONE as a string only if any problem occur
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("ajeetkumarabcd10@gmail.com","maa12345")
    server.sendmail('ajeetkumarabcd10@gmai.com',to,content)
    server.close()


if __name__ == "__main__": # main fn()
    speak("Hello Sir")#fn() calling
    wishMe()
    while True:
        query=takeCommand().lower()

        #Logic forexecuting tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")

        elif 'open code' in query:
            codePath="C:\\Users\\AJEET KUMAR\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to ajit' in query:
            try:
                speak("what should I say?")
                content=takeCommand()
                to="ajeetkumarabcd10@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print (e)
                speak("Sorry sir ,I am not able to send this email")

        
        '''elif 'play music' in query:
            music_dir='C:\\Users\\AJEET KUMAR\\Downloads\\file_example_MP3_700KB.mp3'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))'''

        '''elif 'play sound' in query:
            playsound('C:\\Users\\AJEET KUMAR\\Downloads\\file_example_MP3_700KB.mp3')'''

        
      

        
        


        