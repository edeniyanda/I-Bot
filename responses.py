from datetime import datetime

def sample_response(input_text):
    user_message = str(input_text).lower()
    
    if user_message in  ("hello", "hi","hey", "sup?","What's up?","hi there", "greetings","sup", "hi there", "greetings"):
        return "Hey :)"
    
    if user_message in  ("who are you", "who are you?", "","What's up?","wnat is your name?", "what's your name?", "what is your name", "what's your name","are you a robot?", ):
        return "I am I-bot, a chat bot created by Eden"
    
    if user_message in  ("time", "what is time?", "what's time?","time?","what is time", "what's time"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        
        return str(date_time)
    
    
    
    
    return "Sorry, I don't understand what you said"


    