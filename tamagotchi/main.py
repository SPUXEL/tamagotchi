
from aiogram import executor

from api import dispatcher
import handlers


async def on_startup(_):
    print("The bot is running")


if __name__ == "__main__":
    executor.start_polling(
        dispatcher=dispatcher,
        on_startup=on_startup,
        skip_updates=True
    )
