from telegram.ext import Updater, MessageHandler, Filters

updater = Updater(
    token='1249064364:AAFr2nlFtCd0CAQoifExahswHSQ_4GDBfeU')

dispatcher = updater.dispatcher
updater.start_polling()  # 주기적으로 텔레그램 서버에 접속해서 종현이로부터 새로운 메새지가 ㅣㅆ으면 받아오라


def handler(bot, update):
    text = update.message.text
    chat_id = update.message.chat_id

    if '모해' in text:
        bot.send_message(chat_id=chat_id, text="지미니 생각ㅎㅎ")
    elif '사진' in text:
        bot.send_photo(chat_id=chat_id, photo=open(
            'img/Screenshot_8.png', 'rb'))  # rb : 바이너리 형식
    else:
        bot.send_message(chat_id=chat_id, text="몰롸")


echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
