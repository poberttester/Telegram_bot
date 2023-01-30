import telebot


hi_bot = telebot.TeleBot('6081579701:AAHlZSH98nnZmqc-KQqNv-FtUL4pmPHmW5g')

@hi_bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == "Привет":
        hi_bot.send_message(message.from_user.id, "Привет,)")
    elif message.text == "/help":
        hi_bot.send_message(message.from_user.id, "Напиши мне 'Привет'")
    else:
        hi_bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

hi_bot.polling(none_stop=True, interval=0)
