
from aiogram.types import Message

from api import bot, dispatcher
from data import config, langpack, forbidden_words


@dispatcher.message_handler(
    chat_id=config.MAIN_CHAT_ID
)
async def checking_for_forbidden_words(update: Message):
    received_message = update.text.lower()
    for word in forbidden_words.FORBIDDEN_WORDS:
        if word in received_message:
            await update.delete()
