import logging
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, Application, ContextTypes
from datetime import datetime
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(rf'Hi {user.mention_html()}!👋 this is a telegram bot that improve with python')


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("I can't understand what are you saying😕")
    print(update.effective_user)


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(rf'OK {user.mention_html()}! have good one👋, Byeeeee')


async def describe(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html('hmmm \nI\'m actually a programmer who want learning something about everything')


async def moment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now().time()
    formatted_time = now.strftime("%H:%M:%S")
    await update.message.reply_html(rf'the time is {formatted_time}')


def main():
    TOKEN = ""
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.add_handler(CommandHandler('stop', stop))
    application.add_handler(CommandHandler('desc', describe))
    application.add_handler(CommandHandler('time', moment))
    application.run_polling()


if __name__ == "__main__":
    main()
