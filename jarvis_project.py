#Jarvis_Project_Code.py
import pyttsx3                                # Text to speech library
import speech_recognition as sr               # Speech Recongnition 
import datetime                               # Date and time library 
import wikipedia                              # To access and parse data from Wikipedia
import webbrowser                             # To access web browser
import os                                     # For interacting with the operating system
import keyboard                               # To interact with the keys pressed by keyboard
import sys                                    # To interact with the system
import cv2                                    # To use webcam

# Sets the engine to get the voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')                 
engine.setProperty('voice',voices[1].id)              

# Convert text to speech
def speak(audio):  
    engine.say(audio)
    engine.runAndWait()        # Without this command, speech will not be audible to us.


name= ""

# Ask name function
def askname():
    name = input("\nKindly enter your name....\n")
    keyboard.wait('enter')

    speak(f"{name}, such a nice name")
    print(f"How can I help you {name}, let me know, I am there for your service")
    speak(f"How can I help you {name}, let me know, I am there for your service")

    

# If user enters y then program continues else it ends
def keypressed():
    key = keyboard.read_key()

    if keyboard.is_pressed('y'):  
            print(f'You Pressed {key} Key! \nHey there! My name is Jarvis. What is your name?')
            speak(f'You Pressed {key} Key! \nHey there! My name is Jarvis. What is your name?')
            askname()
    elif keyboard.is_pressed(key):  
            print(f'You Pressed {key} Key! \nThanks for coming :)')
            speak(f'You Pressed {key} Key! \nThanks for coming :)')
            sys.exit(0)
            


# Jarvis will greet me according to the time 
def wishMe():
    hour = int(datetime.datetime.now().hour)        #stored the integer value of the current hour 
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("\nGood Morning!\n")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        print("\nGood Afternoon!\n")
    else:
        speak("Good Evening!")
        print("\nGood Evening!")

    speak("\nI am jarvis. Press Y if you want to continue else Press ENTER or any other key if you want to quit......\n")
    print("\nI am Jarvis. Press 'Y' if you want to continue else Press ENTER or any other key if you want to quit......\n")
    keypressed()


# Function to use webcam
def camera():
    webcam = cv2.VideoCapture(0)

    ## Iterate forever over frames
    while True:
        # Read current frame
        successfull_frame_read, frame = webcam.read()

        if not successfull_frame_read:
            break

        # Displaying the screen
        cv2.imshow('Webcam',frame)  

        # cv2.waitKey(1)
        # If ESC key is pressed the window gets shut down
        k = cv2.waitKey(1)

        if k == 27:                  # wait for ESC key to exit (27 is ascii code for ESC)
            break
        elif k == ord('s'):           # wait for 's' key to save and exit
            cv2.imwrite('Saved_Image.png',frame)
            cv2.destroyAllWindows()
            print("Image Saved")
            speak("Image saved")
    webcam.release()


# takecommand() with the help of the microphone of the user's system
# It takes microphone input from the user and returns string output
def takeCommand():
    if keyboard.is_pressed('enter') or keyboard.is_pressed('q'):  # if key 'enter' or 'q' is pressed 
            print('\nYou quited the program! My service ends here! Thanks for coming.')
            speak('You quited the program! My service ends here! Thanks for coming')
            sys.exit(0)

    r = sr.Recognizer()
    with sr.Microphone() as source:                            # use the default microphone as the audio source
        print("\nListening...")
        speak("Listening")
        r.pause_threshold = 1 
        audio = r.listen(source, timeout=5)                    # listen for the first phrase and extract it into audio data
    
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')    # Using google for voice recognition.
        print(f"You said: {query}\n")                          # User query will be printed.
        return query
    except Exception as e:
        print(e)    
        print("Can't understand ! Say that again please...")   # Say that again will be printed in case of improper voice 
        speak("Can't understand ! Say that again please...") 
        return "None"                                          # None string will be returned
    


# Creating Our main() functionS
# __name__ is a built-in variable which evaluates to the name of the current module
# If the source file is executed as the main program, the interpreter sets the __name__ variable to have a value “__main__”
if __name__=="__main__" :
    speak("\a Welcome to Jarvis world")
    wishMe()
    while True: 
            query=takeCommand().lower()                  # Converting user query into lower case
            
            # Task 1
            if 'name' in query:
                speak("My name is Jarvis. What is your good name?")
                name= takeCommand().lower()
                speak(f"{name} such a sweet name! ")     # The letter “f” also indicates that these strings are used for formatting.

            # Task 2
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
                print("Opening Youtube! ")
                speak("Opening Youtube! ")
                break

            # Task 3
            elif 'open google' in query:
                webbrowser.open("google.com")
                print("Opening google in Microsoft edge broswer! Enjoy web surfing")
                speak("Opening google in Microsoft edge broswer! Enjoy web surfing")
                break
            
            # Task 4
            elif 'wikipedia' in query:                   # If wikipedia found in the query then this block will be executed
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia of ", "")
                results = wikipedia.summary(query, sentences=2) 
                speak("According to Wikipedia: ")
                print(results)
                speak(results)
    
            # Task 5
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")   
                print(f"The current time is {strTime}")
                speak(f"The current time is {strTime}")
            
            # Task 6
            elif 'date' in query:  
                strDate = datetime.datetime.now().strftime("%d:%m:%Y")
                print(f"Today's date is {strDate}")
                speak(f"Today's date is {strDate}")

            # Task 7
            elif 'camera' in query:
                print("Opening webcam for you! \nTo save your picture press-'s'.\nTo close the webcam press- 'ESC'")
                speak("Opening webcam for you! \nTo save your picture press 's' \nTo close the webcam press 'ESC'")
                camera()


            # Exiting the loop if user say bye
            elif 'bye' in query:
                print("Bye, It was really nice meeting you. Have a Good day!")
                speak("Bye, It was really nice meeting you. Have a Good day!")
                break

            # If user says something which is not in the task list, then it will search it on wikipedia 
            elif '' in query:
                speak('Searching Wikipedia...')
                results = wikipedia.summary(query, sentences=2) 
                speak("According to Wikipedia: ")
                print(results)
                speak(results)
                



