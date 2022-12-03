import telebot;
bot = telebot.TeleBot('5730873851:AAGZRxTwpx2PVAC5UMkM_v0wKq7-m3-dg1I');
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    @bot.message_handler(content_types=['text', 'document', 'audio'])

    if message.text == "Привіт":
        bot.send_message(message.from_user.id, "Привіт, чим я можу тобі помогти?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привіт")
    else:
        bot.send_message(message.from_user.id, "Я тебя не розумію. Напиши /help.")
bot.polling(none_stop=True, interval=0)
name = '';
surname = '';
age = 0;
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Як тебя звати?");
        bot.register_next_step_handler(message, get_name);
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg');

def get_name(message):
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Яка в тебя фамилия?');
    bot.register_next_step_handler(message, get_surnme);

def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message('Скільки тобі років?');
    bot.register_next_step_handler(message, get_age);

def get_age(message):
    global age;
    while age == 0:
        try:
             age = int(message.text)
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, Будьласка');
      bot.send_message(message.from_user.id, 'Тобі '+str(age)+' років, тебе звати '+name+' '+surname+'?')
def get_age(message):
    global age;
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, будьласка');
    keyboard = types.InlineKeyboardMarkup();
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes');
    keyboard.add(key_yes);
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no');
    keyboard.add(key_no);
    question = 'Тобі ' + str(age) + ' років, тебя звати ' + name + ' ' + surname + '?';
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Запамятаю : )');
    elif call.data == "no":
from telebot import types