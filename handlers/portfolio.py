from aiogram import Router, F
from aiogram.types import CallbackQuery
from common.keyboards import Keyboards

router = Router()

@router.callback_query(F.data == 'portfolio')
async def look_at_portfolio(callback: CallbackQuery):
    await callback.answer("Просмотреть категории")
    await callback.message.answer(
        "Для чего разработать дизайн?", 
        reply_markup=Keyboards.get_portfolio_keyboard())

@router.callback_query(F.data == 'infographics')
async def choose_infographics(callback: CallbackQuery):
    await callback.answer("Загрузка")
    await callback.message.answer(
        """Инфографика — это отличный способ донести сложную информацию легко и красиво!
        \n ✅ Креативный дизайн 
        \n ✅ Использование ваших данных и бренда 
        \n ✅ Быстрое выполнение
        \n Стоимость: от 200 рублей 
        \n Сроки: от 2 дней
        """,
        reply_markup=Keyboards.get_portfolio_and_orders_keyboard())

@router.callback_query(F.data == 'logos')
async def choose_logos(callback: CallbackQuery):
    await callback.answer("Загрузка")
    await callback.message.answer(
        """Логотипы — ваш уникальный знак, который запомнят клиенты!
        \n ✅ Индивидуальный подход и креативный дизайн
        \n ✅ Учет ваших идей и бизнес-задач
        \n ✅ Варианты на выбор и правки.
        \n Стоимость: от 1500 рублей 
        \n Сроки: от 3 дней
        """,
        reply_markup=Keyboards.get_portfolio_and_orders_keyboard())

@router.callback_query(F.data == 'certificates')
async def choose_certificates(callback: CallbackQuery):
    await callback.answer("Загрузка")
    await callback.message.answer(
        """Сертификаты — стильное и профессиональное оформление ваших достижений!
        \n ✅ Дизайн в фирменном стиле
        \n ✅ Подготовка к печати и цифровому использованию
        \n ✅ Быстро и качественно
        \n Стоимость: от 1000 рублей 
        \n Сроки: от 1 дня
        """,
        reply_markup=Keyboards.get_portfolio_and_orders_keyboard())

@router.callback_query(F.data == 'cards')
async def choose_cards(callback: CallbackQuery):
    await callback.answer("Загрузка")
    await callback.message.answer(
        """Открытки и приглашения — яркий
        \n ✅ Уникальный и креативный дизайн
        \n ✅ Оформление для любых мероприятий
        \n ✅ Подготовка файлов
        \n Стоимость: от 1200 рублей 
        \n Сроки: от 2 дней
        """,
        reply_markup=Keyboards.get_portfolio_and_orders_keyboard())

@router.callback_query(F.data == 'leaflets')
async def choose_leaflets(callback: CallbackQuery):
    await callback.answer("Загрузка")
    await callback.message.answer(
        """Листовки — привлеките внимание клиентов!
        \n ✅ Эффектный и информативный дизайн
        \n ✅ Подготовка к печати
        \n ✅ С учетом вашего бренда и целей
        \n Стоимость: от 1200 рублей 
        \n Сроки: от 3 дней
        """,
        reply_markup=Keyboards.get_portfolio_and_orders_keyboard())

@router.callback_query(F.data == 'business_cards')
async def choose_business_cards(callback: CallbackQuery):
    await callback.answer("Загрузка")
    await callback.message.answer(
        """Визитные карточки — ваш стильный инструмент для делового общения!
        \n ✅ Элегантный и современный дизайн
        \n ✅ Полное соответствие вашему бренду
        \n ✅ Готовые файлы для печати и цифрового использования
        \n Стоимость: от 1000 рублей 
        \n Сроки: от 3 дней
        """,
        reply_markup=Keyboards.get_portfolio_and_orders_keyboard())

@router.callback_query(F.data == 'price_lists')
async def choose_price_lists(callback: CallbackQuery):
    await callback.answer("Загрузка")
    await callback.message.answer(
        """Прайс-листы — четко, понятно и стильно!
        \n ✅ Дизайн, соответствующий вашему бренду
        \n ✅ Удобное и наглядное представление информации
        \n ✅ Форматы для печати и онлайн
        \n Стоимость: от 1400 рублей (от 4-х историй) 
        \n Сроки: от 1 дня
        """,
        reply_markup=Keyboards.get_portfolio_and_orders_keyboard())