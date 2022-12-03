import telebot
bot = telebot.TeleBot('5730873851:AAGZRxTwpx2PVAC5UMkM_v0wKq7-m3-dg1I')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Напиши шось мені нудно? <:(')
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Ви напичатали: ' + message.text)
bot.polling(none_stop=True, interval=0)