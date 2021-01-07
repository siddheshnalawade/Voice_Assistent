import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import re
import subprocess
import pyjokes

MASTER='Siddhesh'

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
speak("Hii "+MASTER)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning"+MASTER)
    elif hour>=12 and hour<18:
        speak("Good Afternoon"+MASTER)
    else:
        speak('Good Evening')


with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            recognized_audio = r.recognize_google(audio)
            print(recognized_audio)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print("")
def takeCommand():
    with sr.Microphone() as source:
        
        
        print("Listening...")
        audio1 = r.listen(source)

        try:
            query = r.recognize_google(audio1,language='en-in')
            print(query)
        except Exception as e:
            speak("Say that again please")
            query=takeCommand()
        except sr.UnknownValueError:
            speak("Say that again please")
            query=takeCommand()
        except sr.RequestError as e:
           speak("Say that again please")
           query=takeCommand()
        return query

def sendMail(to,content):
    speak("Sending mail sir")
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sidprogrammer321@gmail.com','Sidprogrammer@321')
    server.sendmail('siddheshnalawade2000@gmail.com',to,content)
    server.close()
    



if __name__=='__main__': 
    wishMe()
    speak("What I can do for you")
    while True:
        query=takeCommand()
        
        if 'wikipedia' in query.lower():
            speak("Searching wikipedia..")  
            query = query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
            
        elif 'open youtube' in query.lower():
            speak("opening youtube..")
            #webbrowser.open("youtube.com")      
            url = "youtube.com"
            chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url,new=2)

        elif 'open google' in query.lower():
            speak("opening google.com")
            url="google.com"
            chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url,new=2)
            
        elif 'open' in query.lower():
            reg_ex = re.search('open (.+)',query)
            if reg_ex:
                domain = reg_ex.group(1)
                print(domain)
                url='https://www.'+domain
                chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                webbrowser.get(chrome_path).open(url)
                speak("Opening "+domain)
            else:
                pass

        elif 'play music' in query.lower():
            speak("playing music sir")
            songs_dir="F:\\music"
            songs = os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir,songs[0]))
            
        elif 'email to siddhesh' in query.lower():
            try:
                speak("What should I send")
                content=takeCommand()
                to="siddheshnalawade2000@gmail.com"
                sendMail(to,content)
                speak("Email has been sent successfully")
            except Exception as e:
                print(e)
                
        elif 'joke' in query: 
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke()) 
        
        elif 'the time' in query.lower():
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{MASTER} the time is {strTime}")       
        elif 'shutdown system' in query: 
            speak("Hold On a Sec ! Your system is on its way to shut down") 
            subprocess.call('shutdown / p /f') 
            
        elif "now you can stop" in query.lower():
            speak("Thank You Sir")
            break