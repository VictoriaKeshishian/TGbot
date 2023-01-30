# #скачиваем библиотеку pip install pytelegrambotapi
# import telebot
# from telebot import types
# user_sweets = 0
# bot = telebot.TeleBot("5782756209:AAG-Rzx3ieL-JGwzHm5kGucQGT3TZ6nBhUw")

# @bot.message_handler(commands = ['start'])#вызов функции по команде в списке
# def start(message):
#     bot.send_message(message.chat.id,f"/button")#отправка сообщения (кому отправляем, что отправляем(str))
# print(user_sweets)

# def summa(message):
#     summ = sum(list(map(int,message.text.split())))
# bot.send_message(message.chat.id, str(summ))
# button(message)

# @bot.message_handler(commands=["button"])
# def button(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)#создание клавиатуры
# but1 = types.KeyboardButton("сумма")#создание кнопок
# but2 = types.KeyboardButton("разность")
# markup.add(but1)#добавление кнопок
# markup.add(but2)#добавление кнопок
# bot.send_message(message.chat.id,"Выбери ниже", reply_markup=markup)


# @bot.message_handler(content_types=["text"])#вызов функции если тип сообщения - текст
# def controller(message):
#     if message.text == "сумма":
#         bot.send_message(message.chat.id,"введи два числа для суммы")
#         bot.register_next_step_handler(message, summa) # вызов функции на ответ пользователя
#     elif message.text == "разность":
#         pass
# bot.infinity_polling()

####################################################################################################################################################################

