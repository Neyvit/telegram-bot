from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

portfolio_kbd = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Открытки/пригласительные", callback_data="cards")
    ],
    [
        InlineKeyboardButton(text="Инфографика", callback_data="infographics"),
        InlineKeyboardButton(text="Визитки", callback_data="business_cards"),
        InlineKeyboardButton(text="Логотипы", callback_data="logos"),
    ],
    [
        InlineKeyboardButton(text="Прайс-листы", callback_data="price_lists"),
        InlineKeyboardButton(text="Листовки", callback_data="leaflets"),
        InlineKeyboardButton(text="Сертификаты", callback_data="certificates"),

    ],
], )

start_portfolio_kbd = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Портфолио",
                          callback_data="portfolio")]
], )

portfolio_and_orders_kbd = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Посмотреть портфолио",
                             url="https://www.behance.net/gallery/213576091/Portfolio"),
    ],
    [
        InlineKeyboardButton(text="Написать дизайнеру / Заказать",
                             url="https://t.me/Angelika_zhu"),
    ],
], resize_keyboard=True)

write_to_me_kbd = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Написать дизайнеру / Заказать",
                             url="https://t.me/Angelika_zhu"),
    ],
], resize_keyboard=True)
