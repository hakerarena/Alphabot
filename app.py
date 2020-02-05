from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)
bot = ChatBot("Candice")
# chatbot = ChatBot('Training Example')
conversation = [
    "Helo",
    "Hi thre!",
    "How ar you doing?",
    "I'm ding great.",
    "That is god to hear",
    "Thank you.",
    "You're welcome."
]
trainer = ListTrainer(bot)
trainer.train(conversation)

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
