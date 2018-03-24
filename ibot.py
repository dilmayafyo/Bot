import telebot
import myClass

token = "583815699:AAFOFO1yc610WimhNvPo2jAg-Zr219reymI"

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def check_message(message):
    if message.text == 'Список студентов':
        for student in myClass.getListStudents():
            bot.send_message(message.chat.id, 'Имя: ' + student[0])          
    elif message.text == 'Сред. оценка':
        bot.send_message(message.chat.id,myClass.getAverStudMark())
    elif message.text.isdigit():
        bot.send_message(message.chat.id,
                         'Имя: ' + myClass.getStudentByIndex(int(message.text))[0])
        bot.send_message(message.chat.id,
                         'Оценка: ' + myClass.getStudentByIndex(int(message.text))[1])
    else:
         bot.send_message(message.chat.id, "Такой команды я не знаю")                    
bot.polling(none_stop=True)
