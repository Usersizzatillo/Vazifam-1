import os
import sqlite3
import telebot
from telebot import types

# 7-qatorni shundoq mana bu ko'rinishda qo'shtirnoq bilan yozing:
BOT_TOKEN = "8777272457:AAED5CWzd2ewmHYig5BVthb_0MX16dpFFxk"
bot = telebot.TeleBot(BOT_TOKEN)
# Ma'lumotlar bazasi yo'li (Django db.sqlite3 fayli)
# bot.py fayli 'main' papkasida turgani uchun bazani bitta yuqori papkadan qidiradi
DB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "db.sqlite3"
)


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# Boshlang'ich tugmalar
def main_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📋 Talabalar ro'yxati")
    btn2 = types.KeyboardButton("➕ Yangi talaba qo'shish")
    markup.add(btn1, btn2)
    return markup


# /start buyrug'i
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        f"Salom, {message.from_user.first_name}!\nTalabalarni boshqarish botiga xush kelibsiz.",
        reply_markup=main_keyboard(),
    )


# 1. Talabalar ro'yxatini ko'rish
@bot.message_handler(
    func=lambda message: message.text == "📋 Talabalar ro'yxati"
)
def list_students(message):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Sizning bazangizdagi jadval nomi: main_talaba
        cursor.execute("SELECT id, ism, familiya, guruh FROM main_talaba")
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            bot.send_message(message.chat.id, "Hozircha talabalar yo'q.")
            return

        response = "🎓 **Talabalar ro'yxati:**\n\n"
        for row in rows:
            response += f"🆔 {row['id']} | 👤 {row['ism']} {row['familiya']} - Guruh: {row['guruh']}\n"

        bot.send_message(message.chat.id, response, parse_mode="Markdown")

    except Exception as e:
        bot.send_message(
            message.chat.id,
            f"Xatolik yuz berdi. Baza hali yaratilmagan yoki yo'l xato: {e}",
        )


# 2. Yangi talaba qo'shish jarayoni
user_data = {}


@bot.message_handler(
    func=lambda message: message.text == "➕ Yangi talaba qo'shish"
)
def add_student_start(message):
    msg = bot.send_message(
        message.chat.id,
        "Talabaning ismini kiriting:",
        reply_markup=types.ReplyKeyboardRemove(),
    )
    bot.register_next_step_handler(msg, process_ism)


def process_ism(message):
    chat_id = message.chat.id
    user_data[chat_id] = {"ism": message.text}
    msg = bot.send_message(chat_id, "Talabaning familiyasini kiriting:")
    bot.register_next_step_handler(msg, process_familiya)


def process_familiya(message):
    chat_id = message.chat.id
    user_data[chat_id]["familiya"] = message.text
    msg = bot.send_message(chat_id, "Guruhini kiriting (masalan: FNU-1):")
    bot.register_next_step_handler(msg, process_guruh)


def process_guruh(message):
    chat_id = message.chat.id
    user_data[chat_id]["guruh"] = message.text
    msg = bot.send_message(chat_id, "Yoshini kiriting (faqat son):")
    bot.register_next_step_handler(msg, process_yosh)


def process_yosh(message):
    chat_id = message.chat.id
    try:
        yosh = int(message.text)
        user_data[chat_id]["yosh"] = yosh

        # Ma'lumotlarni main_talaba jadvaliga yozish
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO main_talaba (ism, familiya, guruh, yosh, faol) VALUES (?, ?, ?, ?, ?)",
            (
                user_data[chat_id]["ism"],
                user_data[chat_id]["familiya"],
                user_data[chat_id]["guruh"],
                user_data[chat_id]["yosh"],
                1,  # faol = True (1)
            ),
        )
        conn.commit()
        conn.close()

        bot.send_message(
            chat_id,
            "🎉 Talaba muvaffaqiyatli qo'shildi va Django bazasiga saqlandi!",
            reply_markup=main_keyboard(),
        )
        del user_data[chat_id]
    except ValueError:
        msg = bot.send_message(chat_id, "Xato! Iltimos yoshini sonda kiriting:")
        bot.register_next_step_handler(msg, process_yosh)
    except Exception as e:
        bot.send_message(
            chat_id, f"Bazaga yozishda xato: {e}", reply_markup=main_keyboard()
        )


# Botni uzluksiz ishga tushirish
print("Telegram bot ishga tushdi...")
bot.polling(none_stop=True)