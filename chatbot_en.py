import nltk
from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses.
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created using NLTK.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :)","It was nice talking to you. See you soon :)"]
    ],
]

# This is the chatbot creation. You can replace reflections with a custom dictionary if needed.
chatbot = Chat(pairs, reflections)

# Start conversation
print("Hi! I'm a simple chatbot. Type 'quit' to exit.")
chatbot.converse()
