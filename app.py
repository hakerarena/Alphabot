from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)
bot = ChatBot("Candice")
# chatbot = ChatBot('Training Example')
trainer = ListTrainer(bot)

trainer.train([
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is god to hear",
    "Thank you.",
    "You're welcome."
])
trainer.train([
    "cya", "See you later", "Goodbye", "I am Leaving","bye","Have a Good day",
    "Sad to see you go :(", "Talk to you later", "Goodbye!"
])
trainer.train([
    "tell me about yourself","I am an AI bot created by the Alphabot team","who created you?","Alphabot created me for registration of crime online","team that builds you"
])
trainer.train([
    "i want to register a complaint","Yah sure","register a complaint","Response to the following questions to file a complaint","register fir","Sure, follow along with me","fir","sure, follow me"
])
# trainer.train([
#     "Hello",
#     "Hi there!",
#     "How are you doing?",
#     "I'm doing great.",
#     "That is god to hear",
#     "Thank you.",
#     "You're welcome."
# ])
# trainer.train([
#     "Hello",
#     "Hi there!",
#     "How are you doing?",
#     "I'm doing great.",
#     "That is god to hear",
#     "Thank you.",
#     "You're welcome."
# ])
# trainer.train([
#     "Hello",
#     "Hi there!",
#     "How are you doing?",
#     "I'm doing great.",
#     "That is god to hear",
#     "Thank you.",
#     "You're welcome."
# ])

# trainer.train(conversation)

# trainer.train([
#     "Hi there!",
#     "Hello",
# ])

# trainer.train([
#     "Greetings!",
#     "Hello",
# ])

# trainer = ChatterBotCorpusTrainer(bot)

# trainer.train(
#     "chatterbot.corpus.english"
# )
# trainer.train(
#     "./data/greetings_corpus/custom.corpus.json",
#     "./data/my_corpus/"
# )

@app.route("/")
def home():    
    return render_template("home.html") 
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(bot.get_response(userText)) 
if __name__ == "__main__":    
    app.run()
