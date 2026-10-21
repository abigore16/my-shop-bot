import telebot
from telebot import types

# ВСТАВЬТЕ ВАШ ТОКЕН В КАВЫЧКАХ
import os
bot = telebot.TeleBot(os.environ.get("8049747251:AAHjxCk6S-x1pNU9fa7EWpPR6OZzqN2eEjs"))
# --- ГЛАВНОЕ МЕНЮ (появляется внизу) ---
@bot.message_handler(commands=['start'])
def start(message):
    # Создаем клавиатуру
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_catalog = types.KeyboardButton('🛍 Каталог товаров')
    btn_about = types.KeyboardButton('ℹ️ О магазине')
    btn_contact = types.KeyboardButton('📞 Связаться с нами')
    markup.add(btn_catalog, btn_about, btn_contact)
    
    # Приветственное сообщение
    bot.send_message(message.chat.id, 
                     f"Привет, {message.from_user.first_name}! 👋\n"
                     f"Добро пожаловать в наш магазин. Выберите нужный раздел в меню ниже:", 
                     reply_markup=markup)

# --- ОБРАБОТКА КНОПОК ГЛАВНОГО МЕНЮ ---

@bot.message_handler(func=lambda message: message.text == '🛍 Каталог товаров')
def show_catalog(message):
    # Здесь мы создаем Inline-кнопки (кнопки под сообщением)
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_cat1 = types.InlineKeyboardButton('👕 Одежда', callback_data='cat_clothes')
    btn_cat2 = types.InlineKeyboardButton('📱 Электроника', callback_data='cat_electronics')
    btn_cat3 = types.InlineKeyboardButton('🏠 Для дома', callback_data='cat_home')
    markup.add(btn_cat1, btn_cat2, btn_cat3)
    
    bot.send_message(message.chat.id, "Выберите категорию товаров:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'ℹ️ О магазине')
def show_about(message):
    bot.send_message(message.chat.id, 
                     "🏪 *Наш магазин*\n\n"
                     "Мы продаем качественные вещи по доступным ценам. "
                     "Работаем с 2026 года. Доставка по всей Беларуси!", 
                     parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == '📞 Связаться с нами')
def show_contact(message):
    bot.send_message(message.chat.id, 
                     "Для оформления заказа или вопросов напишите нашему менеджеру:\n"
                     "👉 @abigore16")

# --- ОБРАБОТКА НАЖАТИЙ НА INLINE-КНОПКИ (КАТАЛОГ) ---
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'cat_clothes':
        bot.send_message(call.message.chat.id, "👕 *Одежда:*\n\n1. Футболка — 30 BYN\n2. Джинсы — 80 BYN\n\nДля покупки нажмите 'Связаться с нами' в меню.", parse_mode='Markdown')
    elif call.data == 'cat_electronics':
        bot.send_message(call.message.chat.id, "📱 *Электроника:*\n\n1. Наушники — 150 BYN\n2. Чехол для телефона — 20 BYN\n\nДля покупки нажмите 'Связаться с нами' в меню.", parse_mode='Markdown')
    elif call.data == 'cat_home':
        bot.send_message(call.message.chat.id, "🏠 *Для дома:*\n\n1. Подушка — 40 BYN\n2. Лампа — 50 BYN\n\nДля покупки нажмите 'Связаться с нами' в меню.", parse_mode='Markdown')
    
    # Обязательно отвечаем Telegram, чтобы кнопка перестала "грузиться"
    bot.answer_callback_query(call.id)

# Запуск бота
print("Бот запущен и готов к работе...")
bot.polling(none_stop=True)