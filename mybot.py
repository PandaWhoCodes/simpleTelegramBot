import telebot
bot = telebot.TeleBot("MYKEY")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print("Hello There")
    bot.reply_to(message,"Hello There")

"""
normal message handling  // Commented out
@bot.message_handler(func=lambda message: True)
def send_welcome(message):
    bot.reply_to(message,message.text)

"""
#To check the spelling
@bot.message_handler(func=lambda message: True)
def send_welcome(message):
    d = open('diction.dictionary')
    dictionaryItems = d.read().split("\n")
    if message.text in dictionaryItems:
      bot.reply_to(message,"The word exists")
    else:
      bot.reply_to(message,"The word illae")


bot.polling()
