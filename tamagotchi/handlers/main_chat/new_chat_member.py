
import random

from aiogram.types import ContentType, Message

from _bot import bot, dispatcher
from data import langpack


@dispatcher.message_handler(
    content_types=[ContentType.NEW_CHAT_MEMBERS]
)
async def new_chat_member(update: Message):
    member = update.new_chat_members[0]

    greeting = random.choice(langpack.GREETINGS)

    await bot.send_message(
        update.chat.id,
        greeting.replace("*", member.mention)
    )
