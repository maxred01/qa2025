from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Как у вас дела!")

async def allure_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Вы использовали команду аллюре")

def main() -> None:
    application = Application.builder().token("8866805088:AAHsddR2gsAKzDZ_d0jUehn56Oi6cDW9ho0").build()
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("allurereport", allure_command))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()