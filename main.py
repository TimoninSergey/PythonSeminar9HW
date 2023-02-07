from aiogram import Bot, Dispatcher, executor, types
from handlers import dp
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

async def on_start(_):
    logging.info('Bot start')
    print('Бот запущен')



executor.start_polling(dp, skip_updates=True, on_startup=on_start)

