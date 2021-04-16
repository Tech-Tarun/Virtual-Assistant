import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")   

    else:
        speak("Good Evening Sir!")  

    speak("My name is Friday. I am an artificial intelligence programe, created by Tech, Tarun Corporations. Please tell me how may I help you Sir")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        command = r.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")

    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return command

def convert(string):
    li=list(string.split(","))
    return li
    
def convert2(input_seq,seperator):
    strr=seperator.join(input_seq)
    return strr

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email_Id', 'your_password')
    server.sendmail('your_email_Id', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:

        command = takeCommand().lower()

        if 'wikipedia' in command:
            speak('Exploring Wikipedia...')
            command = command.replace("wikipedia", "")        #must say wikipedia in the phrase to search from wikipedia
            results = wikipedia.summary(command, sentences=2)
            speak("Sir, According to Wikipedia,")
            print(results)
            speak(results)

        elif 'open youtube' in command:
            webbrowser.open("youtube.com")          #Say open youtube to open it

        elif 'open google' in command:
            webbrowser.open("google.com")           #Say open google to open it

        elif 'open w3schools' in command:
            webbrowser.open("w3schools.com")        #Say open w3school to open it    


        elif 'play music' in command:
            webbrowser.open("jiosaavan.com")        #Say play music to open jiosaavan, you can customise it also

        
        elif 'open whatsapp' in command:
            webbrowser.open("web.whatsapp.com")     #Say open whatsapp to open whatsapp web

        elif 'the time' in command:
            time = datetime.datetime.now().strftime("%I %M %p")     #Ask what's the time to get it
            print(f"Sir, the time is {time}")
            speak(f"Sir, the time is {time}")

         #Update the email list in email_id.txt as per your contacts
                            #Initially, I have kept it empty

        elif 'email' in command:
            try:
                speak("Whome do you want to write, Sir?")
                name=takeCommand().lower()
                speak("What should I write, Sir?")
                content = takeCommand()
                with open("email_id.txt","r")as f:
                    email_list=convert(f.read()) 
                    for i in email_list:
                        if name in i:
                            to = i    
                            sendEmail(to, content)
                            speak("Your Email has been sent successfully!")
                            break
            except Exception as e:
                speak("Sorry Sir due to some error, I am not able to send this email. Please try again")    

        elif "ok" in command:
            speak("I am happy to help you sir, feel free to have my assistance again.")
            exit()

        #Code written below is to open a playlist,VS Code and Google Chrome stored in my PC
             #To open any playlist or any application,customise and use the below code
             
        '''
        elif 'play broken playlist' in command:
            video_dir="D:\\Tripathi's\\Videos\\Broken\\Broken 1"  
            videos=os.listdir(video_dir)
            os.startfile(os.path.join(video_dir,videos[0]))

        elif 'open code' in command:
            codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open chrome' in command:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)'''
            
               