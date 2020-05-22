import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')  # to take voices and sythesis voices  by microsoft for windows (inbuilted)
voices = engine.getProperty("voices")
print(voices)

# print(voices[1].id)
engine.setProperty('voice',voices[1].id ) #  index positions - types of voices 



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour) # 24 - hr formated 
    if hour >= 0 and hour<12 :
        speak('Good Morning !')
    elif hour >= 12 and hour < 18 :
        speak("Good Afternoon !")
    else :
        speak("Good Evening !")
    
    speak('I am Kedi, How may I help you ?') 
def takeCommand():
    # takes microphone input from user and returns string output

    r=sr.Microphone() 
    with sr.Microphone as source :
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print('Recognizing....')
            query = r.recognize_google(audio, language = 'en-in')
            print(f "user said :{query}\n")
        except Exception as e:
            print(e)
            print("Say that again please....")
            return "None" 
        return query
def sendEmail(to, comment): #  these works when you enable less secure apps
    server = smtplib.SMTP('smpt.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mail-id', ur- password)
    server.sendmail('mail-id', to, content)





if  __name__ == "__main__" :
    wishMe()
    while True :
     # if 1:



        query = takeCommand().lower()

        # logic for executing tasks based on query 
        if 'wikipedia ' in query :
            
            speak('Searching wikipedia....')
            query=query.replace("Wikipedia ", " ")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query :
            webbrowser.open("youtube.com")
        elif 'open google' in query :
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query :
            webbrowser.open("stackoverflow.com")
        elif 'play music ' in query :
            music_dir = 'c:\\music\\songs  ' # enter your musoc folder path 
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'time ' in query :
            strTime = datetime.datetime.now().strftime('%H:%H:%S')
            speak(f"The time is {strTime}")
        elif 'open code ' in query :
            codePath = "C:\Users\seetharam\AppData\Local\Programs\Microsoft VS Code\Code.exe" # enter your file path 
            os.startfile(codePath)
        elif 'mail to seetharam' in query :
            try :
                speak('what should i say ...')
                content = takeCommand()
                to = "orugantiseetaram@gmail.com" 
                sendEmail(to, content)
                speak('Email sent successfully ...')
            except Exception as e :
                print(e)
                speak('sorry sir , I cannot send mail ...')









