import logging
import ephem
import settings
from datetime import date

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename='bot.log', level=logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text("Здравствуй, пользователь!")

def planet_info(update, context):
    text = update.message.text 
    now = date.today()
    try:
        planet = text.split('/planet ', maxsplit=1)[-1].capitalize()
        planet_code = getattr(ephem, planet)(now)
        location = ephem.constellation(planet_code)
        update.message.reply_text(f'Планета " {planet} " распологается в созвездии {location[1]}.')
    except (AttributeError):
        update.message.reply_text(f'Неверная команда. Введите запрос корректно в формате "/planet название".')
    

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_info))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
