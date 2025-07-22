import telebot
from django.conf import settings

bot = telebot.TeleBot(token=settings.BOT_TOKEN)


def send_message(message):
    first_name = message.first_name
    phone = message.phone
    user_message = message.message

    caption = f"""
<b>📩 Yangi Murojaat!</b>\n
<b>👤 Ism:</b> {first_name}\n
<b>📞 Telefon:</b> {phone}\n
<b>📝 Xabar:</b> {user_message}
    """

    bot.send_message(
        chat_id=settings.ADMIN,
        text=caption,
        parse_mode="HTML"
    )
