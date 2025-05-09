import telebot
from telebot import types


TOKEN = ''
bot = telebot.TeleBot(TOKEN)

# Словарь с расписаниями. Ключ - класс, затем день недели
schedule = {
    '1': {'понедельник': 'Математика, Русский',
          'вторник': 'Физкультура, Русски',
          'среду': 'Литература, Англиский, Русский',
          'четверг': 'Физкультура, Русский, Математика',
          'пятницу': 'Математика, Русский'},
    '2': {'понедельник': 'Чтение, Письмо',
          'вторник': 'Технология, Физкультура, Русский',
          'среду': 'Чтение, Музыка, Русский, Математика',
          'четверг': 'Технология, Физкультура',
          'пятницу': 'Чтение, Письмо'},
'3': {'понедельник': 'Чтение, Письмо',
          'вторник': 'Технология , Физкультура, Русский',
          'среду': 'Чтение, Музыка, Русский, Математика',
          'четверг': 'Технология, Физкультура',
          'пятницу': 'Чтение, Письмо'},
    '4': {'понедельник': 'Чтение, Письмо, Английский',
          'вторник': 'Технология , Физкультура, Русский, Английский',
          'среду': 'Чтение, Музыка, Русский, Математика',
          'четверг': 'Технология, Физкультура',
          'пятницу': 'Чтение, Письмо'},
    '5': {'понедельник': 'Чтение, Письмо, Английский',
          'вторник': 'Технология , Физкультура, Русский, Английский',
          'среду': 'Чтение, Музыка, Русский, Математика',
          'четверг': 'Технология, Физкультура',
          'пятницу': 'Чтение, Письмо'},
    '6': {'понедельник': 'Чтение, Письмо, Английский',
          'вторник': 'Технология , Физкультура, Русский, Английский',
          'среду': 'Чтение, Музыка, Русский, Математика',
          'четверг': 'Технология, Физкультура',
          'пятницу': 'Чтение, Письмо'},
    '7': {'понедельник': 'Чтение, Письмо, Английский',
          'вторник': 'Технология , Физкультура, Русский, Английский',
          'среду': 'Чтение, Музыка, Русский, Математика',
          'четверг': 'Технология, Физкультура',
          'пятницу': 'Чтение, Письмо'},
    '8': {'понедельник': 'Чтение, Письмо, Английский',
          'вторник': 'Технология , Физкультура, Русский, Английский',
          'среду': 'Чтение, Музыка, Русский, Математика',
          'четверг': 'Технология, Физкультура',
          'пятницу': 'Чтение, Письмо'},
    '9': {'понедельник': 'Чтение, Письмо, Английский',
          'вторник': 'Технология , Физкультура, Русский, Английский',
          'среду': 'Чтение, Музыка, Русский, Математика',
          'четверг': 'Технология, Физкультура',
          'пятницу': 'Чтение, Письмо'},
    '10': {'понедельник': 'Чтение, Письмо, Английский',
          'вторник': 'Технология , Физкультура, Русский, Английский',
          'среду': 'Чтение, Музыка, Русский, Математика',
          'четверг': 'Технология, Физкультура',
          'пятницу': 'Чтение, Письмо'},
    '11': {'понедельник': 'Чтение, Письмо, Английский',
          'вторник': 'Технология , Физкультура, Русский, Английский',
          'среду': 'Чтение, Музыка, Русский, Математика',
          'четверг': 'Технология, Физкультура',
          'пятницу': 'Чтение, Письмо'}
}





@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     "Привет! Я бот для онлайн школы, который будет скидывать тебе расписание в зависимости от твоего класса и дня на который надо расписание. Напиши /help чтобы увидеть команды.")


@bot.message_handler(commands=['help'])
def help_command(message):
    # Создаем клавиатуру
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_start = types.KeyboardButton("/start")
    button_Description = types.KeyboardButton("/Description")


    keyboard.add(button_start, button_Description,)

    bot.send_message(message.chat.id, "Список команд:", reply_markup=keyboard)

@bot.message_handler(commands=['Description'])
def start(message):
    bot.send_message(message.chat.id, "Список команд:/start - выдаст краткое описание бота,/help - показывает список команд,чтобы найти расписание для нужного дня и нужного класса надо написать /Расписание для ... класса на ... к примеру /Расписание для 1 класса на понедельник")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text.lower()
    # Проверяем, есть ли в сообщении упоминание класса и дня недели
    for grade in schedule:
        for day in schedule[grade]:
            if grade in text and day in text:
                # Отправляем расписание
                bot.reply_to(message, f"Расписание для {grade} класса на {day}: {schedule[grade][day]}")
                return

    bot.reply_to(message, "Не могу найти расписание. Пожалуйста, укажите класс и день недели.")


bot.infinity_polling()
