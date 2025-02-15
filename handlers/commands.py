from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from common.keyboards import Keyboards
from common.faq import HELP

router = Router()

@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(
        text="""Привет! \nМеня зовут Анжелика. \nЯ помогу вам создать стильный и профессиональный дизайн. 
        \nПо ссылке 'Портфолио' можете посмотреть, какие я выполняю работы.""",
        reply_markup=Keyboards.get_start_portfolio_keyboard())

@router.message(Command('help'))
async def help_cmd(message: Message):
    await message.answer(text=HELP)

@router.message(Command('prices'))
async def prices_cmd(message: Message):
    await message.answer(
        text="""Стоимость зависит от сложности проекта и ваших требований. 
        \nВот примерные цены: 
        \n✅ Инфографика: от 200 рублей
        \n✅ Логотипы: от 1500 рублей
        \n✅ Сертификаты: от 1000 рублей
        \n✅ Открытки и приглашения: от 1200 рублей
        \n✅ Листовки: от 1200 рублей
        \n✅ Визитные карточки: от 1000 рублей
        \n✅ Прайс-листы: от 1400 рублей (от 4-х историй)
        \nЧтобы уточнить цену, расскажите подробнее о вашей задаче, и я предложу подходящий вариант.""")

@router.message(Command('direct'))
async def direct_cmd(message: Message):
    await message.answer(
        text="Если возникли вопросы или хотите заказать дизайн, напишите мне!",
        reply_markup=Keyboards.get_write_to_me_keyboard())
    await message.delete()

@router.message(Command('contacts'))
async def see_contacts_cmd(message: Message):
    await message.answer(
        text="""Связаться со мной можно по следующим контактам: 
        \nTelegram: @Angelika_zhu \nEmail: janjelika934@gmail.com \nInstagram: ange_lika_99""")