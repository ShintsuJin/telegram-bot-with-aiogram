from main import bot, dp
from aiogram.types import Message
from operators import operators
import datetime
from buttons import kb_client1


date = datetime.datetime.now().date()
dateStr = date.strftime('%d')


@dp.message_handler(commands=['start'])
async def command_start(message: Message):
    try:
        await message.reply(
            'Привет, хочешь узнать кто сегодня дежурный? Напиши мне в ЛС любой символ или нажми кнопку или введи /duty') #todo reply_murkdown=kb_client1
    except:
        await bot.send_message(message.from_user.id,
                               'Привет, хочешь узнать кто сегодня дежурный? Напиши мне в ЛС любой символ или введи /duty')


@dp.message_handler(commands=['duty'])
async def duty(message: Message):
    for k,v in operators.items():
        if k == dateStr:
            try:
                await message.reply(text=f'Сегодня дежурный команды внедрения и сопровождения:\n{v}')
            except:
                await bot.send_message(message.from_user.id, text=f'Сегодня дежурный команды внедрения и сопровождения:\n{v}')


@dp.message_handler()
async def giving_info(message: Message):
    for k,v in operators.items():
        if k == dateStr:
            await bot.send_message(message.from_user.id, text=f'Сегодня дежурный команды внедрения и сопровождения:\n{v}')


