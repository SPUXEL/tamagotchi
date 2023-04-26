
import random

from aiogram.types import ContentType, Message

from _bot import bot, dispatcher
from data import config, langpack


@dispatcher.message_handler(
    chat_id=config.MAIN_CHAT_ID,
    content_types=[ContentType.NEW_CHAT_MEMBERS]
)
async def new_chat_member(update: Message):
    member = update.new_chat_members[0]

    greeting = random.choice(langpack.GREETINGS)

    await bot.send_message(
        config.MAIN_CHAT_ID,
        greeting.replace("*", member.mention)
    )
