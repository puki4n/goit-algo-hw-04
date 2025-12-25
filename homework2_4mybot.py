import telebot
import random


API_TOKEN = '----'
bot = telebot.TeleBot(API_TOKEN)


answers = [
    "Безумовно так",
    "Навіть не думай",
    "Сконцентруйся і спитай знову",
    "Так",
    "Ні",
    "Спитай пізніше",
    "Зірки кажуть, що так"
]


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт!\nЗадай мені питання, і я дам відповідь!")


@bot.message_handler(func=lambda message: message.text.endswith('?'))
def magic_ball(message):

    random_choice = random.choice(answers)


    bot.reply_to(message, random_choice)


    bot.send_message(message.chat.id, "Чекаю наступне питання...")
@bot.message_handler(func=lambda message: True)
def another_answer(message):
    bot.reply_to(message, "Це не схоже на питання 🤨\nДодай знак питання '?' в кінці, щоб я почав ворожити!")


print("Ворожка на зв'язку...")
bot.infinity_polling()