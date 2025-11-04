import pyttsx3
import speech_recognition as sr
import datetime


# Taking voice from my system
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)


# speak function
def speak(text):
    """
    
    Args:
        text (_type_): string
    """
    engine.say(text)
    engine.runAndWait()





    # speech recognition function
def takeCommand():
    """This function will recognize voice & return text
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query




# The function for wish me by using time
def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir. How are you doing")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir. How are you doing")

    else:
        speak("Good Evening Sir. How are you doing")

    speak("I am shalini . Tell me sir how can i help you")

