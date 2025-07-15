import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import pygame
import time
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning coder")
    elif 12 <= hour < 18:
        speak("Good Afternoon coder")
    else:
        speak("Good evening coder")
    
    
    pygame.mixer.init()
    pygame.mixer.music.load("endgame.mp3.mp3")  # Use full path if needed
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)  # Wait until music finishes

    time.sleep(1)
    speak("Hey, I am Jarvis here! How may I help you, my dear")   
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening!...")        
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again, please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com") 
        elif 'search' in query:
            speak("What should I search on Google?")
            search_query = takeCommand()
            if search_query != "None":
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
                speak(f"Here are the search results for {search_query}")

        elif 'play' in query:
            song = query.replace("play", "")
            speak(f"Playing {song} on YouTube...")
            pywhatkit.playonyt(song)
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'bye' in query or 'exit' in query or 'stop' in query:
            speak("Goodbye baby! Have a great day.")
            
       
