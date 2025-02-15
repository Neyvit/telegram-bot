from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from common.constants import CallbackData, URLs

class Keyboards:
    """Класс для хранения всех клавиатур бота"""
    
    @classmethod
    def get_portfolio_keyboard(cls) -> InlineKeyboardMarkup:
        """Клавиатура для выбора категории портфолио"""
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Открытки/пригласительные", callback_data=CallbackData.CARDS)
            ],
            [
                InlineKeyboardButton(text="Инфографика", callback_data=CallbackData.INFOGRAPHICS),
                InlineKeyboardButton(text="Визитки", callback_data=CallbackData.BUSINESS_CARDS),
                InlineKeyboardButton(text="Логотипы", callback_data=CallbackData.LOGOS),
            ],
            [
                InlineKeyboardButton(text="Прайс-листы", callback_data=CallbackData.PRICE_LISTS),
                InlineKeyboardButton(text="Листовки", callback_data=CallbackData.LEAFLETS),
                InlineKeyboardButton(text="Сертификаты", callback_data=CallbackData.CERTIFICATES),
            ],
        ])

    @classmethod
    def get_start_portfolio_keyboard(cls) -> InlineKeyboardMarkup:
        """Клавиатура для перехода к портфолио"""
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Портфолио", callback_data=CallbackData.PORTFOLIO)]
        ])

    @classmethod
    def get_portfolio_and_orders_keyboard(cls) -> InlineKeyboardMarkup:
        """Клавиатура для просмотра портфолио и связи с дизайнером"""
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Посмотреть портфолио", url=URLs.PORTFOLIO),
            ],
            [
                InlineKeyboardButton(text="Написать дизайнеру / Заказать", url=URLs.DESIGNER),
            ],
        ], resize_keyboard=True)

    @classmethod
    def get_write_to_me_keyboard(cls) -> InlineKeyboardMarkup:
        """Клавиатура для связи с дизайнером"""
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Написать дизайнеру / Заказать", url=URLs.DESIGNER),
            ],
        ], resize_keyboard=True)
