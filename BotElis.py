import telebot
from telebot import types

# создаем бота
bot = telebot.TeleBot("6838743657:AAHeZ2JxYKr91N1x33a72yrPEk-S98ocse4")


# Ответ на команду /start
@bot.message_handler(commands=['start'])
def start(message):
    nark = types.InlineKeyboardMarkup(row_width=1)
    btn1reg = types.InlineKeyboardButton(text='📱РЕГИСТРАЦИЯ', callback_data='btn1')
    btn2sin = types.InlineKeyboardButton(text='🚀Получить сигнал🚀', callback_data='btn2')
    btn3sin2 = types.InlineKeyboardButton(text='💣Получить сигнал💣', callback_data='btn3')
    btnob = types.InlineKeyboardButton(text='📩Обратная связь📩', url='https://t.me/CallBack_Elisium_bot')
    btncan = types.InlineKeyboardButton(text='✅НАШ КАНАЛ✅', url='https://t.me/elisium1win')
    nark.add(btn1reg, btn2sin, btn3sin2, btncan, btnob)
    bot.send_photo(message.chat.id, 'https://telegra.ph/file/a814d1fc3e7032846757e.jpg', caption="🍀 Приветствуем тебя в @elisiumteam_bot \n\nБот основан и обучен на кластере нейросети 🖥 [bitsgap]. \nДля тренировки бота было сыграно 🎰10.000+ игр. \n\nНа данный момент доступны сигналы по таким играм: \n\n💣 MINES - высокая точность достигается постоянными тренировками на базе ИИ \n\n🚀 LuckyJet - высокая точность достигается благодаря хранению последних 5.000 игр, математическому анализу и обучении ИИ \n\nПроходи регистрацию и получай доступ к сигналам👇", reply_markup=nark)

# Ответ на инлайн-кнопку регистрации
@bot.callback_query_handler(func=lambda callback: callback.data == 'btn1')
def check_callback(callback):
    nark1 = types.InlineKeyboardMarkup(row_width=1)
    btn1reg = types.InlineKeyboardButton(text='🚀Регистрация🚀', url='https://1wnurc.com/casino/list?open=register#d3af')
    btn2pr = types.InlineKeyboardButton(text='🔍Проверить регистрацию', callback_data='btn4')
    nark1.add(btn1reg, btn2pr)
    bot.send_photo(callback.message.chat.id, 'https://telegra.ph/file/e8fd0bf7dcee84db34fbd.jpg', caption='🌐Шаг 1 - Зарегистрируйся. \n\n✦ Для синхронизации с нашим ботом необходимо зарегистрировать новый аккаунт по ранее неиспользованному на этом сайте номеру телефона, а также без использования социальных сетей. \n\nПри регистрации ОБЯЗАТЕЛЬНО нажать кнопку «добавить промокод» - ввести промокод HACKBIGWIN \n\nПосле регистрации вносите депозит на сумму от 2000 RUB для открытия раздела сигналов. \n\n● после завершения регистрации, нажмите кнопку \n🔍 Проверить регистрацию. \n\nДля получения более точной информации можете обратиться к модераторам в разделе 📩Обратная связь📩 \n\n\n(Для вызова меню введите команду /start)', reply_markup=nark1)

# Ответ на получение сигнала
@bot.callback_query_handler(func=lambda callback: callback.data == 'btn2')
def check_sigh(callback):
    bot.send_photo(callback.message.chat.id, 'https://telegra.ph/file/a44440357c5ee23195720.jpg', caption='Упс… похоже вы не прошли процедуру регистрации на 1win \n\nПожалуйста, пройдите регистрацию, после этого раздел автоматически будет открыт🍀 \n\n(Для вызова меню введите команду /start)')
@bot.callback_query_handler(func=lambda callback: callback.data == 'btn3')
def check_sigh(callback):
    bot.send_photo(callback.message.chat.id, 'https://telegra.ph/file/a44440357c5ee23195720.jpg', caption='Упс… похоже вы не прошли процедуру регистрации на 1win \n\nПожалуйста, пройдите регистрацию, после этого раздел автоматически будет открыт🍀 \n\n(Для вызова меню введите команду /start)')

# Ответ на проверку регистра
@bot.callback_query_handler(func=lambda callback: callback.data == 'btn4')
def check_registration(callback):
    nark2 = types.InlineKeyboardMarkup(row_width=1)
    btnvv = types.InlineKeyboardButton(text='🛠написать тех. специалисту🛠', url='https://t.me/alternativelyy')
    nark2.add(btnvv)
    bot.send_message(callback.message.chat.id, 'Упс… похоже вы не зарегистрировались😢\n\nЕсли вы считаете, что произошла ошибка и вы прошли регистрацию - напишите техническому специалисту, он проверит все вручную 👇 \n\n(Для вызова меню введите команду /start)', reply_markup=nark2)



print('БОТ ЗАПУЩЕН')

bot.polling()

