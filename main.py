import asyncio
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.types import BotCommandScopeAllPrivateChats, CallbackQuery
from aiogram.filters import CommandStart, Command

from dotenv import find_dotenv, load_dotenv

from common.keyboards import start_portfolio_kbd, write_to_me_kbd, portfolio_kbd, portfolio_and_orders_kbd

load_dotenv(find_dotenv())
from common.bot_commands_list import private

bot = Bot(token=os.getenv('TTOKKEN_APE'))
dp = Dispatcher()

HELP = """
/q1 - Сколько времени занимает работа?
/q2 - Сколько вариантов дизайна я получу?
/q3 - Можно ли внести изменения в готовый дизайн?
/q4 - Какие форматы файлов я получу?
/q5 - Поможете ли вы с печатью или размещением работы в интернете?
/q6 - У меня уже есть логотип/идеи. Вы сможете их доработать?
/q7 - Какие данные нужно предоставить для начала работы?
/q8 - Работаете ли со срочными заказами?
/q9 - Можно ли получить исходники?
/q10 - Вы работаете только по предоплате?
/q11 - Вы делаете дизайн или также разрабатываете тексты?
/q12 - Что делать, если не понравился ваш дизайн?
"""


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    # await message.delete()
    await message.answer(
        text="""Привет! \nМеня зовут Анжелика. \nЯ помогу вам создать стильный и профессиональный дизайн. 
        \nПо ссылке 'Портфолио' можете посмотреть, какие я выполняю работы.""",
        reply_markup=start_portfolio_kbd)


@dp.message(Command('help'))
async def help_cmd(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP)


@dp.message(Command('contacts'))
async def see_contacts_cmd(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="""Связаться со мной можно по следующим контактам: 
                           \nTelegram: @Angelika_zhu \nEmail: janjelika934@gmail.com \nInstagram: ange_lika_99""")


@dp.message(Command('prices'))
async def portfolio_cmd(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="""Стоимость зависит от сложности проекта и ваших требований. 
                           \nВот примерные цены: 
                           \n✅ Инфографика: от 200 рублей
                           \n✅ Логотипы:от 1500рублей
                           \n✅ Сертификаты: от 1000 рублей
                           \n✅ Открытки и приглашения: от 1200 рублей
                           \n✅ Листовки: от 1200 рублей
                           \n✅ Визитные карточки: от 1000 рублей
                           \n✅ Прайс-листы: от 1400 рублей (от 4-х историй)
                           \nЧтобы уточнить цену, расскажите подробнее о вашей задаче, и я предложу подходящий вариант.
                           """)


@dp.message(Command('direct'))
async def write_to_me_cmd(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Если возникли вопросы или хотите заказать дизайн, напишите мне!",
                           reply_markup=write_to_me_kbd)
    await message.delete()


@dp.callback_query(F.data == 'portfolio')
async def look_at_portfolio(callback: CallbackQuery):
    await callback.answer("Просмотреть категории")
    await callback.message.answer("Для чего разработать дизайн?", reply_markup=portfolio_kbd)


@dp.callback_query(F.data == 'infographics')
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
        reply_markup=portfolio_and_orders_kbd)


@dp.callback_query(F.data == 'logos')
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
        reply_markup=portfolio_and_orders_kbd)


@dp.callback_query(F.data == 'certificates')
async def choose_logos(callback: CallbackQuery):
    await callback.answer("Загрузка")
    await callback.message.answer(
        """Сертификаты — стильное и профессиональное оформление ваших достижений!
        \n ✅ Дизайн в фирменном стиле
        \n ✅ Подготовка к печати и цифровому использованию
        \n ✅ Быстро и качественно
        \n Стоимость: от 1000 рублей 
        \n Сроки: от 1 дня
        """,
        reply_markup=portfolio_and_orders_kbd)


@dp.callback_query(F.data == 'cards')
async def choose_logos(callback: CallbackQuery):
    await callback.answer("Загрузка")
    await callback.message.answer(
        """Открытки и приглашения — яркий
        \n ✅ Уникальный и креативный дизайн
        \n ✅ Оформление для любых мероприятий
        \n ✅ Подготовка файлов
        \n Стоимость: от 1200 рублей 
        \n Сроки: от 2 дней
        """,
        reply_markup=portfolio_and_orders_kbd)


@dp.callback_query(F.data == 'leaflets')
async def choose_logos(callback: CallbackQuery):
    await callback.answer("Загрузка")
    await callback.message.answer(
        """Листовки — привлеките внимание клиентов!
        \n ✅ Эффектный и информативный дизайн
        \n ✅ Подготовка к печати
        \n ✅ С учетом вашего бренда и целей
        \n Стоимость: от 1200 рублей 
        \n Сроки: от 3 дней
        """,
        reply_markup=portfolio_and_orders_kbd)


@dp.callback_query(F.data == 'business_cards')
async def choose_logos(callback: CallbackQuery):
    await callback.answer("Загрузка")
    await callback.message.answer(
        """Визитные карточки — ваш стильный инструмент для делового общения!
        \n ✅ Элегантный и современный дизайн
        \n ✅ Полное соответствие вашему бренду
        \n ✅ Готовые файлы для печати и цифрового использования
        \n Стоимость: от 1000 рублей 
        \n Сроки: от 3 дней
        """,
        reply_markup=portfolio_and_orders_kbd)


@dp.callback_query(F.data == 'price_lists')
async def choose_logos(callback: CallbackQuery):
    await callback.answer("Загрузка")
    await callback.message.answer(
        """Прайс-листы — четко, понятно и стильно!
        \n ✅ Дизайн, соответствующий вашему бренду
        \n ✅ Удобное и наглядное представление информации
        \n ✅ Форматы для печати и онлайн
        \n Стоимость: от 1400 рублей (от 4-х историй) 
        \n Сроки: от 1 дня
        """,
        reply_markup=portfolio_and_orders_kbd)


@dp.message(Command('q1'))
async def q1_cmd(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="""Срок выполнения зависит от сложности проекта.
                           \n✅ Инфографика: от 2 дней
                           \n✅ Логотипы: от 3 дней
                           \n✅ Сертификаты: от 1 дня
                           \n✅ Открытки и приглашения: от 2 дней
                           \n✅ Листовки: от 3 дней
                           \n✅ Визитные карточки: от 3 дней
                           \n✅ Прайс-листы: от 1 дня
                        \nЕсли вам нужно срочно, я могу ускорить процесс за дополнительную плату. 
                        \nДавайте обсудим сроки, чтобы они подходили вам.
                           """,
                           reply_markup=write_to_me_kbd)


@dp.message(Command('q2'))
async def q2_cmd(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="""Обычно я предлагаю:
                           \n✅ Для логотипов: 2–3 концепта на выбор
                           \n✅ Для листовок и визиток: 1–2 варианта
                        \nПосле выбора концепции я вношу до 3 правок бесплатно. Если потребуется больше правок, мы обсудим это отдельно.
                           """,
                           reply_markup=write_to_me_kbd)


@dp.message(Command('q3'))
async def q3_cmd(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="""Конечно! После завершения работы я предоставляю 3 бесплатные правки.
                        \nЕсли потребуется больше правок или значительные изменения, мы обсудим дополнительную оплату.
                           """,
                           reply_markup=write_to_me_kbd)


@dp.message(Command('q4'))
async def q4_cmd(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="""Я предоставляю готовые работы в следующих форматах:
                        \n✅ Для печати: PDF, TIFF, EPS
                        \n✅ Для использования в интернете: JPEG, PNG
                        \n✅ Для редактирования: исходный файл (например, PSD, AI)
                        \n Если вам нужен другой формат, пожалуйста, сообщите об этом заранее.
                           """,
                           reply_markup=write_to_me_kbd)


@dp.message(Command('q5'))
async def q5_cmd(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="""В случае необходимости я могу помочь со следующим:
                        \n✅ Подготовлю дизайн к печати
                        \n✅ Если работа будет использоваться в интернете, настрою файлы под нужный размер и формат
                        \n✅ Если вам нужна помощь с публикацией, например, в Instagram, расскажите, и мы все настроим вместе
                           """,
                           reply_markup=write_to_me_kbd)


@dp.message(Command('q6'))
async def q6_cmd(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="""Конечно, я могу доработать ваш логотип или идею. Если у вас есть исходные файлы, это ускорит процесс. 
                           \nЕсли вы хотите полностью переработать дизайн, мы начнем с обсуждения ваших пожеланий.
                           """,
                           reply_markup=write_to_me_kbd)


@dp.message(Command('q7'))
async def q7_cmd(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="""Чтобы я могла приступить к работе, мне нужно:
                           \n✅ Подробное описание вашего проекта
                           \n✅ Текстовая информация (если есть - текст для листовки, визитки и т.д.)
                           \n✅ Примеры или референсы, которые вам нравятся
                           \n✅ Логотипы, фирменные цвета и шрифты (если они есть)
                           """,
                           reply_markup=write_to_me_kbd)


@dp.message(Command('q8'))
async def q8_cmd(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="""Да, я могу работать над срочными проектами. 
                           \nЭто будет стоить немного дороже, в зависимости от времени, которое у нас есть. 
                           \nРасскажите подробнее, и я постараюсь помочь!
                           """,
                           reply_markup=write_to_me_kbd)


@dp.message(Command('q9'))
async def q9_cmd(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="""Исходные файлы (например, PSD, AI) я предоставляю за дополнительную плату, так как это требует учета авторских прав и более сложной работы. 
                           \nЕсли они вам нужны, пожалуйста, дайте знать заранее.
                           """,
                           reply_markup=write_to_me_kbd)


@dp.message(Command('q10'))
async def q10_cmd(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="""Обычно я работаю по следующей схеме:
                           \n✅ Предоплата 50% перед началом работы
                           \n✅ Остаток — после утверждения финального дизайна
                           \nЭто стандартная практика для обеспечения комфортной работы для обеих сторон.
                           """,
                           reply_markup=write_to_me_kbd)


@dp.message(Command('q11'))
async def q11_cmd(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="""Я специализируюсь на дизайне, но могу помочь адаптировать ваш текст. 
                           \nЕсли требуется полноценная разработка текста, рекомендую воспользоваться услугами копирайтера.
                           """,
                           reply_markup=write_to_me_kbd)


@dp.message(Command('q12'))
async def q12_cmd(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="""✅ Мы начнем с обсуждения ваших пожеланий, чтобы создать концепцию, которая вам точно понравится. 
                           \n✅ Я предложу несколько вариантов дизайна и внесу до 3 правок бесплатно.
                           \n✅ Если после всех доработок дизайн не устроит, мы обсудим, как лучше действовать дальше.
                           """,
                           reply_markup=write_to_me_kbd)


@dp.message()
async def unknown_requests(message: types.Message):
    await message.answer("Не понимаю вас. Выберите нужную команду.")


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.delete_my_commands(scope=BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=private, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)


asyncio.run(main())
# dp.run_polling(bot)
