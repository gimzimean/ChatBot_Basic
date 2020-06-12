import telegram

api_key = '1249064364:AAFr2nlFtCd0CAQoifExahswHSQ_4GDBfeU'

bot = telegram.Bot(token=api_key)

#chat_id = bot.get_updates()[-1].message.chat_id
chat_id = 933726710

bot.send_message(chat_id=chat_id, text="지민아 , 나.. 사실 ...")
print('1', chat_id)
