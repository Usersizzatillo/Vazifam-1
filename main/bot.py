import os
import sqlite3
import telebot
from telebot import types

# 1. Bot tokenini sozlash
BOT_TOKEN = "8777272457:AAED5CWzd2ewmHYig5BVthb_0MX16dpFFxk"
bot = telebot.TeleBot(BOT_TOKEN)

# 2. Ma'lumotlar bazasi yo'lini to'g'rilash (Django db.sqlite3 fayli uchun)
# Bot 'main' papkasida turinganligi sababli, bitta yuqori papkadagi bazaga ulanadi
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "db.sqlite3")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# 3. Boshlang'ich tugmalar paneli
def main_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📋 Talabalar ro'yxati")
    btn2 = types.KeyboardButton("➕ Yangi talaba qo'shish")
    markup.add(btn1, btn2)
    return markup

# 4. /start buyrug'i
@bot.message_handler(commands=["start"])
def send_welcome(message):
    user_name = message.from_user.first_name if message.from_user.first_name else "Foydalanuvchi"
    bot.send_message(
        message.chat.id,
        f"Salom, {user_name}!\nTalabalarni boshqarish botiga xush kelibsiz.",
        reply_markup=main_keyboard()
    )

# 5. Talabalar ro'yxatini ko'rish handler (Saytga avtomatik ulanadi)
@bot.message_handler(func=lambda message: message.text == "📋 Talabalar ro'yxati")
def show_students_list(message):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Django odatda jadval nomini 'appname_modelname' ko'rinishida saqlaydi -> main_talaba
        # Hamma ustunlarni (id, ism, familiya, guruh) yuklab olamiz
        cursor.execute("SELECT id, ism, familiya, guruh FROM main_talaba")
        students = cursor.fetchall()
        conn.close()
        
        if not students:
            bot.send_message(message.chat.id, "Hozircha bazada talabalar mavjud emas.")
            return
            
        text = "🎓 **Talabalar ro'yxati (Saytdan yangilangan):**\n\n"
        for student in students:
            # Har bir ustunni Django modeli formatida to'g'ri o'qiymiz
            student_id = student["id"]
            ism = student["ism"]
            familiya = student["familiya"] if student["familiya"] else ""
            guruh = student["guruh"] if student["guruh"] else "Kiritilmagan"
            
            text += f"🆔 {student_id} | 👤 {ism} {familiya} - Guruh: {guruh}\n"
            
        bot.send_message(message.chat.id, text, parse_mode="Markdown")
        
    except sqlite3.OperationalError as e:
        bot.send_message(
            message.chat.id, 
            "Xatolik: Django jadvali topilmadi. Jadval nomini tekshiring!"
        )
    except Exception as e:
        bot.send_message(message.chat.id, f"Xatolik yuz berdi: {str(e)}")

# 6. Yangi talaba qo'shish tugmasi handler
@bot.message_handler(func=lambda message: message.text == "➕ Yangi talaba qo'shish")
def ask_student_info(message):
    text = (
        "Telegram bot orqali talaba qo'shish hozircha FSM (State) tizimida sozlangan.\n\n"
        "Yangi talabalarni brauzer orqali paneldan qo'shishingiz mumkin:\n"
        "🔗 http://127.0.0.1:8000/yangi/\n\n"
        "Saytdan qo'shganingizdan so'ng, yuqoridagi **📋 Talabalar ro'yxati** tugmasini bossangiz, shu zahoti botda ham paydo bo'ladi!"
    )
    bot.send_message(message.chat.id, text)

# 7. Botni doimiy ishga tushirish
if __name__ == "__main__":
    print("Telegram bot ishga tushdi...")
    bot.infinity_polling()