from datetime import datetime
import random, re

def checkthis():
    yeah = ("Yes","Sure","Absolutely","Definitely","Certainly","Of course","Yes, please","Yes, I'd like that","Yes, I'm interested","Yes, I agree","Yah","Yep","Yeah")
    return random.choice(help).capitalize()
    if checkup in yeah:
        print("Ok")
    
def sample_response(input_text):
    global help
    user_message = str(input_text).lower()
    
    help = ("I can certainly help you to check up the meaning of any word something in the English dictionary\nShould I?","I can look up the meaning of any word for you in the English dictionary. Do you need help with that?","I'm here to help you find the meaning of any word in the English dictionary. Is that something you'd like to do?""If you need help finding the meaning of a word in the English dictionary, I'm happy to assist. Would you like to do that now?","I'm able to help you look up the meaning of any word in the English dictionary. Do you need me to do that for you?","If you have a word you need the meaning of, I can help you find it in the English dictionary. Shall I do that for you?")
    
    notcomprehensible = ("I'm sorry, but that's not something I can help with. Could you try typing 'help' instead?", "Oops, sorry I didn't catch that, try typing 'help'","I can't comprehend, but you can certainly try typing 'help' instead", "I'm not sure how to help with that. Maybe you should try tying 'help' instead")
    
    unclear = ("I'm sorry, but I'm not quite sure what you're asking. Could you please clarify your question or request?","I'm not understanding your question. Could you try rephrasing it in a different way?","I'm sorry, but I'm unable to process your request as it stands. Could you please provide more information or context?")
    
    madeyou = ("I was created by Eden Iyanda an AI engineer who specializes in building artificial intelligence and chatbot technology.","I was developed by Eden Iyanda n AI engineer who focuses on creating chatbots and other AI-powered technologies.","I was created by Eden Iyanda using programming languages and algorithms that allow me to understand and respond to user input.","I was built by Eden Iyanda using a combination of machine learning techniques and pre-programmed responses.","I was designed by Eden Iyanda to assist with a variety of tasks and provide information to users, and my capabilities are constantly being updated and improved.")
    
    greetings = ("Hello! :)\nHow can I help you today?","Hi there!:)\nWhat can I do for you?","Good day:),\nHow can I assist you?")
    
    
    if user_message in  ("hello", "hi","hey", "sup?","What's up?","hi there", "greetings","sup", "hi there", "greetings","good morning","good afternoon","what's up?","what's new?"):
        return random.choice(greetings)
    
    if user_message in  ("who are you", "who are you?", "","wnat is your name?", "what's your name?", "what is your name", "what's your name","are you a robot?", ):
        return "I am I-bot, a chat bot created by Eden"
    
    if user_message in  ("time", "what is time?", "what's time?","time?","what is time", "what's time"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        
        return str(date_time)
    
    if re.search("eden", user_message) or re.search("iyanda", user_message) or re.search("inioluwa", user_message):
        return "Your are probably refering to Eden Iyanda.All I know about him is that he created me :)"
    
    if user_message.startswith("how are you"):
        return "As a chatbot, I don't have feelings or emotions like humans do. However, I am always ready and willing to help you with any questions or tasks you may have."
    
    if user_message.startswith("can you recommend"):
        return "I'm sorry, but I am unable to provide recommendations for specific businesses or locations as I do not have access to current information about them. However, I can provide general tips and suggestions for finding good restaurants in an area, such as looking up reviews or asking for recommendations from friends or locals."
    
    if user_message.startswith("can you"):
        return "It depends on the task you have in mind. I may be able to assist with tasks such as looking up information, providing directions, or helping you complete a form online. If I am unable to help with a specific task, I will do my best to point you in the right direction or suggest an alternative solution :)"
    
    
    if user_message.startswith("what is the capital"):
        return "The capital of a country is the city where the government is located and where the head of state (such as a king, queen, or president) resides."
    
    if re.search("created you", user_message ) or re.search("create you", user_message) or re.search("made you", user_message) or re.search("programmed you",user_message) or re.search("who.+ you", user_message):
        return random.choice(madeyou)
    
    
    if user_message in ("help", 'assist'):
        return checkthis()
        
    
        
    
    
    
    
    return random.choice(notcomprehensible)


    