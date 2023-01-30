import telebot
from telebot import types

from random import randint as ri

total_sweet = 221
take_sweet = 0


bot = telebot.TeleBot("6033590500:AAG2G6Iesoh6KPFv6ILinp_aAwsf4FpwsL0")

####################################################################### ПРИВЕТСТВИЕ ###################################################################

@bot.message_handler(commands=['start']) #вызов функции по команде в списке
def start(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}") #отправка сообщения(кому отправляем, что отправляем(str))
    button(message)
 


@bot.message_handler(commands=['button']) #кнопка
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    but1 = types.KeyboardButton('Начать игру')
    markup.add(but1)
    bot.send_message(message.chat.id, 'Выбери ниже', reply_markup=markup)

@bot.message_handler(content_types='text')
def controller(message):
    if message.text == 'Начать игру':
        bot.send_message(message.chat.id,'На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход')
        bot.register_next_step_handler(message,start_game) #вызов функции на ответ пользователя 
    

####################################################################### ВЫБОР ИГРОКА ###################################################################

def start_game(message):
    global ri
    global total_sweet
    random_number = ri(1,2)
    if random_number == 1:
        bot.send_message(message.chat.id,(f'Ваш ход, количество конфет на столе {total_sweet}'))
        bot.register_next_step_handler(message,player1_turn)
    elif random_number == 2:
        bot.send_message(message.chat.id,(f'Ход бота, количество конфет на столе {total_sweet}'))
        bot.register_next_step_handler(message,bot_turn)
####################################################################### ХОД 1 ИГРОКА ###################################################################

def player1_turn(message):
    global total_sweet
    global take_sweet
    

    bot.send_message(message.chat.id,'Сколько конфет вы возьмёте? (1-28) :')
    take_sweet = list(int,take_sweet.text.split())
    bot.send_message(message.chat.id,str(take_sweet))

    bot.send_message(message.chat.id,f'Вы взяли {take_sweet} конфет')

    # while take_sweet > total_sweet or take_sweet > 28 or take_sweet < 0:
    #     bot.send_message(message.chat.id,'Недопустимое количество конфет, попробуйте еще раз: ')
    #     take_sweet = list(map(int,message.text.split()))
    
    total_sweet -= take_sweet
    take_sweet += take_sweet
   
    if total_sweet > 0:
        bot.send_message(message.chat.id,f'Осталось {total_sweet} конфет')
        bot.register_next_step_handler(message,bot_turn)
    else: bot.send_message(message.chat.id,'Вы победили!!!')
    

####################################################################### ХОД БОТА ###################################################################
def bot_turn(message):
    global total_sweet
    global take_sweet
    
    take_sweet = total_sweet % 29 if total_sweet % 29 != 0 else ri(0,28) 
    total_sweet -= take_sweet
    take_sweet += take_sweet
    bot.send_message(message.chat.id,f'{take_sweet} взял бот, осталось {total_sweet} конфет')
    
    if total_sweet > 0: 
        bot.register_next_step_handler(message,player1_turn)
    else: bot.send_message(message.chat.id,'Победил Бот!!!')

    

bot.infinity_polling()
