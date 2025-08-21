import telebot
from telebot import types
from telebot.types import InputMediaPhoto
from django.conf import settings
import requests



bot = telebot.TeleBot(token=settings.BOT_TOKEN)



def send_order(order):
    chat_id = settings.ADMIN
    yandex_url = f"https://yandex.com/maps/?pt={order.lon},{order.lat}&z=14&l=map"

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📍 Manzilni ko‘rish", url=yandex_url))

    if order.payment_type == "cash":
        payment_type = "Naqt pul"
    else:
        payment_type = order.payment_type

    caption = (
        f"📦 <b>Yangi Buyurtma</b> #{order.id}\n\n"
        f"👤 <b>Buyurtmachi:</b> {order.first_name}\n"
        f"📞 <b>Telefon:</b> {order.phone}\n"
        f"💰 <b>Jami summa:</b> {int(order.total):,} so'm\n"
        f"💳 <b>To'lov turi:</b> {payment_type}\n"
        f"🏘 <b>Viloyat:</b> {order.region}\n"
        f"📍 <b>Tuman:</b> {order.district}\n"
        f"🏠 <b>Manzil:</b> {order.address}\n\n"
        f"📚 <b>Buyurtmadagi Mahsulotlar:</b>\n"
    )


    image_paths = []
    order_items = order.order_items.all()

    for idx, item in enumerate(order_items, 1):
        product = item.product
        caption += (
            f"\n<b>{idx}. Mahsulot nomi: {product.title}</b>\n"
            f"   💵 <b>Narxi:</b> {int(item.total_price):,} so'm\n"
            f"   📦 <b>Miqdori:</b> {item.quantity} dona\n"
        )
        if product.image and product.image.path:
            image_paths.append(product.image.path)

    if len(image_paths) == 1:
        with open(image_paths[0], 'rb') as img:
            bot.send_photo(
                chat_id=chat_id,
                photo=img,
                caption=caption,
                parse_mode="HTML",
                reply_markup=markup
            )
    elif len(image_paths) > 1:
        media_group = []
        for i, path in enumerate(image_paths):
            with open(path, 'rb') as img:
                media = InputMediaPhoto(img.read())
                if i == 0:
                    media.caption = caption
                    media.parse_mode = "HTML"
                media_group.append(media)

        bot.send_media_group(chat_id=chat_id, media=media_group)
    else:
        bot.send_message(chat_id=chat_id, text=caption, parse_mode="HTML")


