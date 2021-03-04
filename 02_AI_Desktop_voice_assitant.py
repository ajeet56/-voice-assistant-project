import pyttsx3 #It is used for conversion of text to speech 
import datetime#Built-in module

engine=pyttsx3.init("sapi5")#It is used to take voice from users
voices=engine.getProperty("voices")#An built-in API provides by window to get voices
print(voices[1].id)
engine.setProperty("voice",voices[0].id)#Set the voices type for male if we want to change for female then we write [1].id IN print()



def speak(audio): #This is the first declarative function that helps to speak jarvis
    engine.say(audio)
    engine.runAndWait()


def wishMe():#It is used to wish in specific way by using time therefore we have to import datetime module
    hour=int(datetime.datetime.now().hour)#typecasted in int
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16 :
        speak("Good Afternoon!")

    else:
        speak("Good Night!")
    #speak()

if __name__ == "__main__": # main fn()
    speak("Ajeet is a good boy")#fn() calling
    wishMe()