import pyttsx3
import time
from speech_recognition import *
from os import system
import webbrowser
import sys
import os
from random import randint
import wikipedia
from Color_Console import *

class Jarvis:

    def __init__(self):
        self.engine=pyttsx3.init('sapi5')
        
        voices=self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id) 
    
        self.engine.setProperty('rate',200)

    def speak(self,audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def wishMe(self):
        system('cls')
        hour=int(time.strftime('%H'))
        if hour>=0 and hour<12:
            print('Good Morning!')
            self.speak("Good Morning")
        elif hour>=12 and hour<16:
            print('Good Afternoon!')
            self.speak("Good Afternoon")
        else:
            print('Good Evening!')
            self.speak("Good Evening")
        print("\nI'm Jarvis Sir, Please tell me how may i help you?")
        self.speak("I'm Jarvis Sir, Please tell me how may i help you?")
    
    def current_time(self):
        system('cls')
        hour=time.strftime('%I')
        minute=time.strftime('%M')
        second=time.strftime('%S')
        meridian=time.strftime('%p')
        message='\nThe time is: '+hour+':'+minute+':'+second+' '+meridian
        print(message)
        self.speak(message)
    
    def file_exolorer(self):
        os.startfile("C:\\Windows\\explorer.exe")
        self.speak('Opening File Explorer...')
       
    def notepad(self):
        self.speak('Opening Notepad...')
        os.startfile("C:\\Windows\\notepad.exe")

    def bye(self):
        option=['\nGood Bye Sir!','\nGood Bye and Take Care Sir!','\nBye-Bye']
        choice=randint(0,len(option)-1)
        print(option[choice])
        self.speak(option[choice])
        time.sleep(1)
        sys.exit()

    def on_web(self,query):
        if 'open' in query:
            title=query.replace('open ','')
            webbrowser.open_new_tab('http://'+title+'.com')
            self.speak('Opening '+title) 

    def say_name(self):
      message='\nMy name is Jarvis'
      print(message)
      self.speak(message)

    def info(self,query):
        title=query
        message=wikipedia.summary(title,sentences=5)
        print('\n'+message)
        self.speak(message)

    def play_music(self):
        option=['\nPlaying Music...','\nSurfing Music...']
        choice=randint(0,len(option)-1)
        music_dir='C:\\users\\patel\\documents\\python\\tkinter\\music'
        songs=os.listdir(music_dir)
        os.startfile(os.path.join(music_dir,songs[0]))
        print(option[choice])
        self.speak(option[choice])

    def takeCommand(self):
        recognize = Recognizer()
        with Microphone() as source:    
            system('cls')
            print('\nListening...')
            recognize.energy_threshold = 4000
            recognize.pause_threshold=2
            audio=recognize.listen(source)
        
            try:
                print('\nRecognizing...')
                text=recognize.recognize_google(audio,language='en-in')
                text=text.lower()
                return text

            except Exception as e:
                print(e)
                print('\nSorry Sir!, please say that again!' )
                self.speak('Sorry Sir!, please say that again!')
    
    def things_i_do(self):
        system('cls')
        option=['Wish You','Tell you Current Time','Open File explorer','Open Notepad','Shutdown this app on Good Bye','Open things in browser','Play Music','get information from Wikipedia','Tell my name']

        print('\nI can do following things:-')
        self.speak('I can do following things:-')

        for task in option:
            print('I can '+task)
            self.speak('I can '+task)
    
    def main(self):
        color(text="black",bg="light red")
        self.wishMe()
        while(True):
            query=self.takeCommand()
            if query==None:
                continue
    
            if 'file explorer' in query:
                self.file_exolorer()
    
            elif 'bye' in query or 'good bye' in query:
                self.bye()
    
            elif 'open notepad' in query:
                self.notepad()
    
            elif 'time' in query:
                self.current_time()

            elif 'name' in query or 'who are you' in query:
                self.say_name()
            
            elif 'wikipedia' in query:
                self.info(query)
            
            elif 'open' in query:
                self.on_web(query)

            elif 'music' in query:
                self.play_music()
            
            elif 'things' in query or 'can do' in query:
                self.things_i_do()

            else:
                r=Recognizer()
                with Microphone() as source:
                    system('cls')
                    print('\nListening...')
                    r.energy_threshold = 4000
                    r.pause_threshold=2
                    print(f"\nYou said: {query}\n")
                    self.speak('You said: '+query)
                    time.sleep(1)
                    print('\nAm I right, Sir?')
                    self.speak('Am I right,Sir?')
                    print('\nListening...')
                    audio=r.listen(source)
                    print('\nRecognizing...')
                    query=r.recognize_google(audio,language='en-in')
                    
                    if 'right'in query or 'yes' in query:        
                        print('\nThankyou Sir! I will keep improving myself')
                        self.speak('Thankyou sir! I will keep improving myself')
                    
                    else:    
                        print('\nI am sorry Sir!, I am still learning...')
                        self.speak('I am sorry Sir!, I am still learning...')
    
assistant=Jarvis()
assistant.main()