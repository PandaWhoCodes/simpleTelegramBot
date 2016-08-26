import telebot
bot = telebot.TeleBot("myapikey")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print("Hello There")
    bot.reply(message,"Hello There")

"""
normal message handling  // Commented out
@bot.message_handler(func=lambda message: True)
def send_welcome(message):
    bot.reply(message,message.text)

"""
#To check the spelling
@bot.message_handler(func=lambda message: True)
def send_welcome(message):
    d = open('diction.txt')
    dictionaryItems = d.read().split("\n")
    if message.text in dictionaryItems:
      bot.reply(message,"The word exists")
    else:
      bot.reply(message,"The word illae")


bot.polling()
