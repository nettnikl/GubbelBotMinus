import logging
import re
from uuid import uuid4

from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext

from config.secrets import TOKEN

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Gubble up your life!')


def gubbleString(string, replaced_chars, glyph="🅱"):
    return re.sub(replaced_chars, glyph, string)


def inlinequery(update: Update, context: CallbackContext) -> None:
    """Handle the inline query."""
    query = update.inline_query.query

    if query:
        results = [
            InlineQueryResultArticle(
                id=str(uuid4()),
                title="Normal",
                input_message_content=InputTextMessageContent(gubbleString(query, '[bp]'))
            ),
            InlineQueryResultArticle(
                id=str(uuid4()),
                title="Advanced",
                input_message_content=InputTextMessageContent(gubbleString(query, '[bpgnmd]'))
            )
        ]
    else:
        results = [
            InlineQueryResultArticle(
                id=str(uuid4()),
                title="GubbelBotMinus",
                url="https://github.com/nettnikl/GubbelBotMinus",
                input_message_content=InputTextMessageContent(
                    "Gubble up your life!\nhttps://github.com/nettnikl/GubbelBotMinus"
                )
            )
        ]

    update.inline_query.answer(results)


def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on noncommand i.e message - gubble the message on Telegram
    dispatcher.add_handler(InlineQueryHandler(inlinequery))

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
