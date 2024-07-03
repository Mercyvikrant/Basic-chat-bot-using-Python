# -*- coding: utf-8 -*-
"""
Created on Wed Jun  28 08:42:20 2024

@author: Vikrant Sinha
"""

import random
import os
import datetime
import webbrowser
import wikipedia
import time

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords



wish_command = ['hey', 'hello', 'yo', 'hi', 'what\'s up', 'how are you']

def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        print("Bot: Good morning, Sir")
    elif 12 <= hour < 18:
        print("Bot: Good afternoon, Sir")
    else:
        print("Bot: Good evening, Sir")

    print("Bot: How can I help you?")

def takecommand():
    try:
        query = input("User: ").strip().lower()
        tokens = word_tokenize(query)
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in tokens if word not in stop_words]
        return " ".join(filtered_tokens)
    except Exception as e:
        print("Bot: Your command is not interpreted. Please try again.")
        return None

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand()
        if query is None:
            continue
        
        query = query.lower()
        
        if "wikipedia" in query:
            print("Bot: Searching, please wait...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print("Bot: According to Wikipedia: " + results)
        
        elif "open youtube" in query:
            print("Bot: Wait for a moment while I open YouTube.")
            webbrowser.open('youtube.com')
        
        elif "open google" in query:
            print("Bot: Wait for a moment while I open Google.")
            webbrowser.open('google.com')
        
        elif "play music" in query:
            print("Bot: Searching for music.")
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir)
            if songs:
                song = random.choice(songs)
                os.startfile(os.path.join(music_dir, song))
            else:
                print("Bot: No songs found in the music directory.")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            print(f"Bot: Sir, the time is {strTime}")
        
        elif "open mail" in query:
            print("Bot: Wait for a moment while I open your mail.")
            webbrowser.open('gmail.com')
        
        elif "wait" in query:
            print("Bot: I am waiting.")
            time.sleep(10)
        
        elif any(command in query for command in wish_command):
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            print("Bot: " ,random.choice(stMsgs))
        
        elif "bye" in query:
            print("Bot: Bye, Sir! Have a good day.")
            break
        
        else:
            print("Bot: Sir, I am not able to process what you said.")
