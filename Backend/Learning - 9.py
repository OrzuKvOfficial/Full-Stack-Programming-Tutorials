from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Chatbot yaratish
bot = ChatBot('GapiruvchiRobot')

# Chatbotni o'rgatish
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

# Chatbot bilan muloqot qilish
while True:
    try:
        user_input = input("Siz: ")
        response = bot.get_response(user_input)
        print(f"Robot: {response}")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
