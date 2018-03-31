#Это бот, который работает со списком учеников
import telebot
personInfo = {'виктор':'+777777777',
              'нурбол':'+77749685512',
              'искандер':'+78996251485'}


token = "583815699:AAFOFO1yc610WimhNvPo2jAg-Zr219reymI"

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def check_message(message):
    bot.send_message(message.chat.id, message.text)
         
bot.polling(none_stop=True)
