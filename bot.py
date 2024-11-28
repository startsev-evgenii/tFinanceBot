import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['go', 'start'])  # Обработка команды для старта
def welcome(message):
    bot.send_message(message.chat.id, "Ola!")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item3 = types.KeyboardButton("Приложения")
    item2 = types.KeyboardButton("Мероприятия")
    item1 = types.KeyboardButton('О нас')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\\n\\nЯ - <b>{1.first_name}</b>, бот команды Projector в НГТУ, "
                     "создан для того, "
                     "чтобы помочь Вам влиться в нашу команду,"
                     "просто узнать что-то о нас или же просто пообщаться и весело провести время.\\n\\n"
                     "<i>Have a nice time</i>".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


# RUN
if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except ConnectionError as e:
        print('Ошибка соединения: ', e)
    except Exception as r:
        print("Непридвиденная ошибка: ", r)
    finally:
        print("Здесь всё закончилось")

# cjdcjdbcj
