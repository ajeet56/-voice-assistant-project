#Building an application of Desktop Voice Assistant

import pyttsx3 #It is used for conversion of text to speech which is written by programmer in program
import datetime#Built-in module
import speech_recognition as sr #This module is used to recognize user voice (mean what they want to say/ask)

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
    with sr.Microphone as source:
        print("Listening.......")
        r.pause_threshold = 1 #Wait for seconds of non-speaking audio before a phrace is considered complete(means it deals with recognition time speed)
        audio=r.listen(source)

    try: #If error occur in recognizing
        print("Recognizing....")
        query=r.recognize_google(audio,Language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)#It will give the error to recognize the audio of user 

        print("Say that again please....")
        return "None"#Return NONE as a string only if any problem occur
    return query

if __name__ == "__main__": # main fn()
    speak("Hello Sir")#fn() calling
    wishMe()
    takeCommand()