# A Basic Chatbot



# Chatbot Project

## Overview
This project is a basic chatbot implemented in Python. The chatbot is capable of recognizing and responding to various user commands, such as opening websites, searching Wikipedia, playing music, and more. It uses Natural Language Processing (NLP) techniques to preprocess user input, making the bot more flexible and user-friendly.

## Features
- **Greeting**: Greets the user based on the time of day.
- **Wikipedia Search**: Searches Wikipedia and provides a summary of the requested topic.
- **Open YouTube**: Opens YouTube in a web browser.
- **Open Google**: Opens Google in a web browser.
- **Play Music**: Plays a random song from a specified directory.
- **Tell Time**: Provides the current time.
- **Open Mail**: Opens Gmail in a web browser.
- **Wait**: Pauses for a specified time.
- **Respond to Greetings**: Responds to various greeting commands.

## Installation
To get started with this project, you'll need to have Python installed. Additionally, you need to install the following libraries:

```bash
pip install wikipedia
pip install nltk
```

## Setup
After installing the necessary libraries, you need to download the required NLTK data:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

## Usage
To run the chatbot, simply execute the script. The bot will greet you based on the current time and prompt you for a command. You can interact with the bot using various commands as described in the features section.

```python
python chatbot.py
```

## Code Explanation

### Importing Libraries
```python
import random
import os
import datetime
import webbrowser
import wikipedia
import time
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
```
- **random**: For selecting random items (e.g., random song).
- **os**: For interacting with the operating system (e.g., listing files).
- **datetime**: For getting the current time.
- **webbrowser**: For opening web pages.
- **wikipedia**: For searching Wikipedia.
- **time**: For pausing execution.
- **nltk**: For NLP tasks.

### Greeting the User
```python
def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        print("Bot: Good morning, Sir")
    elif 12 <= hour < 18:
        print("Bot: Good afternoon, Sir")
    else:
        print("Bot: Good evening, Sir")

    print("Bot: How can I help you?")
```
- Greets the user based on the current time.

### Taking and Preprocessing Commands
```python
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
```
- **Input**: Takes user input from the command line.
- **Preprocessing**: Tokenizes the input and removes common stop words to focus on essential keywords.

### Main Function
```python
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
```
- **wishme()**: Calls the greeting function.
- **takecommand()**: Captures and preprocesses user input.
- **Command Matching**: Matches the preprocessed input with various commands and executes the corresponding actions.


