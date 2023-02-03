from aiogram import Bot, Dispatcher, executor, types
from create import dp
from aiogram.dispatcher.filters import Filter
import random
#from main import total, player_score, bot_score

@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}! Мы будем играть в конфеты! Для просмотра правил введите rules!')

@dp.message_handler(text=['rules', 'Rules'])
async def mes_bla(message: types.Message):
    await message.answer('Здравствуйте, Игрок! Правила следующие - на столе есть конфеты, их общее количество устанавливается командой set число. Игрок и бот берут конфеты по очереди, но не больше 28 за раз. Выигрывает тот, у кого на конец игры оказалось больше конфет. Все просто) А теперь установите количество.')

@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer('Помощь пока не установлена.')

@dp.message_handler(commands=['set'])
async def mes_settings(message: types.Message):
    global total
    count = int(message.text.split()[1])
    total = count
    await message.answer(f'Количество конфет на начало игры установлено равным {total}! Мы начинаем')


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
                    bot_num = random.randint(1,28)
                    if bot_num > total:
                        bot_num = random.randint(1,total)
                    else:
                        total = total - bot_num
                        bot_score = bot_score + bot_num
                        await message.answer(f'Ваш счет - {player_score}, счет бота - {bot_score}')
                        await message.answer(f'На столе осталось {total} конфет')
                else:
                    await message.answer('Вы пытаетесь взять больше конфет, чем есть на столе')
        else:
            await message.answer('Введите число от 1 до 28')
    else:
        await message.answer(f'Игра закончена! Ваш счет - {player_score}, счет бота - {bot_score}')
        if player_score > bot_score:
            await message.answer('Вы победили!')
        elif player_score == bot_score:
            await message.answer('Ничья!')
        else:
            await message.answer('Победил бот! А ведь это просто генератор рандомных чисел...')