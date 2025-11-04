from src.helper import speak, takeCommand, wish_me
import datetime
import wikipedia
import webbrowser
import os




if __name__ == "__main__":

    wish_me()

    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif "youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("youtube.com")


        elif "google" in query:
             speak("Opening google")
             webbrowser.open("google.com")


        elif "github" in query:
             speak("Opening github")
             webbrowser.open("github.com")


        # This query for say the times
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            

        elif 'goodbye' in query:
            speak("ok sir. I am always here for you . bye bye")
            exit()




