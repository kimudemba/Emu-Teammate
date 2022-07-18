import speech_recognition as sr

import pyttsx3

import pyautogui

from selenium import webdriver



r = sr.Recognizer()



def texttoCommand(mytext):

mouseUP = "mouse up"

mouseDown = "mouse down"

mouseLeft = "mouse left"

mouseRight = "mouse right"



close = "close the Window"



if mytext == mouseUP:

pyautogui.moveRel(0, -100, duration = 1)

elif mytext == mouseDown:

pyautogui.moveRel(0, 100, duration = 1)

elif mytext == mouseLeft:

pyautogui.moveRel(-100, 0, duration = 1)

elif mytext == mouseRight:

pyautogui.moveRel(100, 0, duration = 1)

def Speaktext(command):

engine = pyttsx3.init()

engine.say(command)

engine.runAndWait()



with sr.Microphone() as source:



print("noise")

r.adjust_for_ambient_noise(source, duration=2)

print("calibrated")

mytext = ""

#while(mytext != "stop"):

audio2 = r.listen(source)

mytext = r.recognize_google(audio2)

mytext = mytext.lower()

print(mytext)

#Speaktext(mytext)

if mytext.split()[0] == "go":

driver = webdriver.Chrome()

url = "https://www." + mytext.split()[2]

print(url)

driver.get(url)

if mytext == "take a screenshot":

myScreenshot = pyautogui.screenshot()

myScreenshot.save(r'C:\Users\wilbert.delarosaperez@libertymutual.com\Documents\hackathon\test.png')



texttoCommand(mytext)
