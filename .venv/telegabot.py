import telebot
from telebot import types
bot = telebot.TeleBot("6033590500:AAG2G6Iesoh6KPFv6ILinp_aAwsf4FpwsL0")

####################################################################### ПРИВЕТСТВИЕ ###################################################################

import random 
total_sweet = 221
take_sweet = 0
max_sweet = 28
flag = None

def restart():
    global total_sweet
    total_sweet = 221
    

@bot.message_handler(commands=["start"]) #вызов функции по команде в списке
def start(message):
    global flag
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}") #отправка сообщения(кому отправляем, что отправляем(str))
    bot.send_message(message.chat.id,'На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход')  
    flag = random.choice(['user','bot'])
    if flag == 'user':
        bot.send_message(message.chat.id,f'Ваш ход, количество конфет на столе {total_sweet}')
    elif flag == 'bot':
        bot.send_message(message.chat.id,(f'Ход бота, количество конфет на столе {total_sweet}'))
    
    controller(message)


def controller(message):
    global flag
    if total_sweet > 0:
        if flag == 'user':
            bot.send_message(message.chat.id,'Сколько конфет вы возьмёте? (1-28) :')
            bot.register_next_step_handler(message,intput_sweets)

        elif flag == 'bot':
            bot_turn(message)
    else:
        flag = "user" if flag == "bot" else "bot"
        bot.send_message(message.chat.id, f"Победил {flag}!")
        mrk = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = telebot.types.KeyboardButton("Заново")
        
        mrk.add(key1)
        
        bot.send_message(message.chat.id,"Попробуем еще раз?", reply_markup=mrk)
        bot.register_next_step_handler(message,choose_op)

bot.message_handler(content_types = ["text"])
def choose_op(message):
    if message.text == "Заново":
        restart()
        start(message)
    else:
        exit()
 
    ####################################################################### ХОД 1 ИГРОКА ###################################################################

def intput_sweets(message):
    global flag
    global total_sweet
    global take_sweet

    take_sweet = int(message.text)
    
    if take_sweet == 0:
        bot.send_message(message.chat.id,'Так нельзя, возьми другое количество')
        bot.register_next_step_handler(message,intput_sweets)
    
    elif take_sweet > 28:
        bot.send_message(message.chat.id,'Так может и слипнуться что-то')
        bot.register_next_step_handler(message,intput_sweets) 

    else:
        total_sweet = total_sweet - take_sweet
        take_sweet = take_sweet + take_sweet
        bot.send_message(message.chat.id,f'{total_sweet} осталось')
        flag = 'user' if flag == 'bot' else 'bot'
        controller(message)

        
    
####################################################################### ХОД БОТА ###################################################################
def bot_turn(message):
    global flag
    global total_sweet
    global take_sweet
    global max_sweet

    if total_sweet <= max_sweet:
        take_sweet = total_sweet
    elif total_sweet % max_sweet == 0:
        take_sweet = max_sweet - 1
    else:
        take_sweet = total_sweet % max_sweet - 1

    if take_sweet == 0:
        take_sweet = 1
   
    total_sweet = total_sweet - take_sweet
    # take_sweet = take_sweet + take_sweet
    bot.send_message(message.chat.id,f'взял бот {take_sweet}')
    bot.send_message(message.chat.id,f'{total_sweet} осталось')

    flag = "user" if flag == "bot" else "bot"
    controller(message)
    

bot.infinity_polling()

