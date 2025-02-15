from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from common.keyboards import Keyboards
from common.faq import FAQ_ANSWERS

router = Router()

@router.message(Command('q1'))
async def q1_cmd(message: Message):
    await message.answer(
        text=FAQ_ANSWERS['q1'],
        reply_markup=Keyboards.get_write_to_me_keyboard())

@router.message(Command('q2'))
async def q2_cmd(message: Message):
    await message.answer(
        text="""Обычно я предлагаю:
        \n✅ Для логотипов: 2–3 концепта на выбор
        \n✅ Для листовок и визиток: 1–2 варианта
        \nПосле выбора концепции я вношу до 3 правок бесплатно. Если потребуется больше правок, мы обсудим это отдельно.""",
        reply_markup=Keyboards.get_write_to_me_keyboard())

@router.message(Command('q3'))
async def q3_cmd(message: Message):
    await message.answer(
        text="""Конечно! После завершения работы я предоставляю 3 бесплатные правки.
        \nЕсли потребуется больше правок или значительные изменения, мы обсудим дополнительную оплату.""",
        reply_markup=Keyboards.get_write_to_me_keyboard())

@router.message(Command('q4'))
async def q4_cmd(message: Message):
    await message.answer(
        text="""Я предоставляю готовые работы в следующих форматах:
        \n✅ Для печати: PDF, TIFF, EPS
        \n✅ Для использования в интернете: JPEG, PNG
        \n✅ Для редактирования: исходный файл (например, PSD, AI)
        \nЕсли вам нужен другой формат, пожалуйста, сообщите об этом заранее.""",
        reply_markup=Keyboards.get_write_to_me_keyboard())

@router.message(Command('q5'))
async def q5_cmd(message: Message):
    await message.answer(
        text="""В случае необходимости я могу помочь со следующим:
        \n✅ Подготовлю дизайн к печати
        \n✅ Если работа будет использоваться в интернете, настрою файлы под нужный размер и формат
        \n✅ Если вам нужна помощь с публикацией, например, в Instagram, расскажите, и мы все настроим вместе""",
        reply_markup=Keyboards.get_write_to_me_keyboard())

@router.message(Command('q6'))
async def q6_cmd(message: Message):
    await message.answer(
        text="""Конечно, я могу доработать ваш логотип или идею. Если у вас есть исходные файлы, это ускорит процесс. 
        \nЕсли вы хотите полностью переработать дизайн, мы начнем с обсуждения ваших пожеланий.""",
        reply_markup=Keyboards.get_write_to_me_keyboard())

@router.message(Command('q7'))
async def q7_cmd(message: Message):
    await message.answer(
        text="""Чтобы я могла приступить к работе, мне нужно:
        \n✅ Подробное описание вашего проекта
        \n✅ Текстовая информация (если есть - текст для листовки, визитки и т.д.)
        \n✅ Примеры или референсы, которые вам нравятся
        \n✅ Логотипы, фирменные цвета и шрифты (если они есть)""",
        reply_markup=Keyboards.get_write_to_me_keyboard())

@router.message(Command('q8'))
async def q8_cmd(message: Message):
    await message.answer(
        text="""Да, я могу работать над срочными проектами. 
        \nЭто будет стоить немного дороже, в зависимости от времени, которое у нас есть. 
        \nРасскажите подробнее, и я постараюсь помочь!""",
        reply_markup=Keyboards.get_write_to_me_keyboard())

@router.message(Command('q9'))
async def q9_cmd(message: Message):
    await message.answer(
        text="""Исходные файлы (например, PSD, AI) я предоставляю за дополнительную плату, так как это требует учета авторских прав и более сложной работы. 
        \nЕсли они вам нужны, пожалуйста, дайте знать заранее.""",
        reply_markup=Keyboards.get_write_to_me_keyboard())

@router.message(Command('q10'))
async def q10_cmd(message: Message):
    await message.answer(
        text="""Обычно я работаю по следующей схеме:
        \n✅ Предоплата 50% перед началом работы
        \n✅ Остаток — после утверждения финального дизайна
        \nЭто стандартная практика для обеспечения комфортной работы для обеих сторон.""",
        reply_markup=Keyboards.get_write_to_me_keyboard())

@router.message(Command('q11'))
async def q11_cmd(message: Message):
    await message.answer(
        text="""Я специализируюсь на дизайне, но могу помочь адаптировать ваш текст. 
        \nЕсли требуется полноценная разработка текста, рекомендую воспользоваться услугами копирайтера.""",
        reply_markup=Keyboards.get_write_to_me_keyboard())

@router.message(Command('q12'))
async def q12_cmd(message: Message):
    await message.answer(
        text="""✅ Мы начнем с обсуждения ваших пожеланий, чтобы создать концепцию, которая вам точно понравится. 
        \n✅ Я предложу несколько вариантов дизайна и внесу до 3 правок бесплатно.
        \n✅ Если после всех доработок дизайн не устроит, мы обсудим, как лучше действовать дальше.""",
        reply_markup=Keyboards.get_write_to_me_keyboard())
