import nltk
from nltk.chat.util import Chat


pairs=[
    [
        r"Hi|Hello|Hey there|Hola|Namaste",
        ["Hello my name is Aditya"]
    ],
    [
        r"Who are you?",
        ["Hello I am Aditya!"]
    ],
    [
        r"What are you?",
        ["I am chatbot named Aditya"]
    ]]

def chat():
    print('Welcome to the chatbot. Say hii! ')
    chat=Chat(pairs)
    chat.converse()

if __name__== "__main__":
    chat()

