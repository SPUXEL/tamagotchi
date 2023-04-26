
from aiogram.types import ContentType, Message

from _bot import bot, dispatcher


@dispatcher.message_handler(
    content_types=[ContentType.NEW_CHAT_MEMBERS]
)
async def new_chat_member(update: Message):
    new_member = update.new_chat_members[0]
    await bot.send_message(
        update.chat.id,
        f"Добро пожаловать {new_member.mention}"
    )
