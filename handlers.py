from aiogram import Bot, Dispatcher, executor, types
from create import dp
from aiogram.dispatcher.filters import Filter
import random

total = 0
player_score = 0
bot_score = 0

@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}! Мы будем играть в конфеты! Для просмотра правил введите /rules!')

@dp.message_handler(commands=['rules', 'Rules'])
async def mes_rules(message: types.Message):
    await message.answer('Здравствуйте, Игрок! Правила следующие - на столе есть конфеты, их общее количество устанавливается командой /set число. Игрок и бот берут конфеты по очереди, но не больше 28 за раз. Выигрывает тот, у кого на конец игры оказалось больше конфет. Все просто) А теперь установите количество.')

@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer('Помощь пока не установлена.')

@dp.message_handler(commands=['set'])
async def mes_settings(message: types.Message):
    global total
    count = int(message.text.split()[1])
    total = count
    await message.answer(f'Количество конфет на начало игры установлено равным {total}! Мы начинаем, ваш ход.')

@dp.message_handler(commands=['null'])
async def mes_null(message: types.Message):
    global total
    global player_score
    global bot_score
    total = 0
    player_score = 0
    bot_score = 0
    await message.answer('Значения обнулены. Чтобы начать новую игру, введите /set число.')

@dp.message_handler()
async def mes_game(message: types.Message):
    global total
    global player_score
    global bot_score
    if total > 0:
        if message.text.isdigit():
            if int(message.text) > 28 or int(message.text) < 1:
                await message.answer('Можно взять только от 1 до 28 конфет')
            else:
                if total >= int(message.text):
                    total = total - int(message.text)
                    player_score = player_score + int(message.text)
                    if 0 < total < 28:
                        bot_num = random.randint(1, total)
                    elif total > 28:
                        bot_num = random.randint(1,28)
                    elif total == 0:
                        bot_num = 0
                    total = total - bot_num
                    bot_score = bot_score + bot_num
                    await message.answer(f'Бот взял {bot_num} конфет')
                    await message.answer(f'Ваш счет - {player_score}, счет бота - {bot_score}')
                    if total != 0:
                        await message.answer(f'На столе осталось {total} конфет')
                    else:
                        await message.answer('Конфет не осталось, введите 0, чтобы закончить игру!')
                else:
                    await message.answer('Вы пытаетесь взять больше конфет, чем есть на столе')
        else:
            await message.answer('Введите число от 1 до 28')
    elif total == 0:
        await message.answer(f'Игра закончена! Ваш счет - {player_score}, счет бота - {bot_score}')
        if player_score > bot_score:
            await message.answer('Вы победили!')
        elif player_score == bot_score:
            await message.answer('Ничья!')
        else:
            await message.answer('Победил бот! А ведь это просто генератор рандомных чисел...')
        await message.answer('Чтобы обнулить значения, введите /null.')