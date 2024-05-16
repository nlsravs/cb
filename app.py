from flask import Flask, render_template, request
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm feeling good, how about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's okay, no worries.", "No problem.",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye, have a great day!"]
    ],
]

# Create a Chatbot with the defined pairs
chatbot = Chat(pairs, reflections)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get("msg")
    response = chatbot.respond(user_input)
    return response

if __name__ == "__main__":
    app.run(debug=True)
