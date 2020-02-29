from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
import speech_recognition as sr
from time import ctime
import time
import pyttsx3
engine = pyttsx3.init()

bot= ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(bot)

corpus_path = 'C:/Users/MISBAHUR RAHMAN\Desktop\chatbot\english/'
for file in os.listdir(corpus_path):
    trainer.train(corpus_path + file)

def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    message = ""
    try:
        message = r.recognize_google(audio)
        print("You said: " + message)
    except sr.UnknownValueError:
        print("sorry can you please repeate")
    except sr.RequestError as e:
        print("not connected to internet; {0}".format(e))

    return message

time.sleep(2)
engine.say("Hi ifrahur, what can I do for you?")
print("Hi ifrahur, what can I do for you?")
engine.runAndWait()
while 1:
    message = recordAudio()
    if message.strip() == 'Bye':
        print('ChatBot: Bye')
        break
    else:
        reply = bot.get_response(message)
        engine.say(reply)
        print('ChatBot:', reply)
        engine.runAndWait()