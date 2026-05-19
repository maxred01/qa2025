from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Че, как бро?")


def main() -> None:
    application = Application.builder().token("8844629529:AAHruBBd2Wei-2A7TIG0M9BrqlUrv295W3I").build()
    application.add_handler(CommandHandler("test", help_command))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()