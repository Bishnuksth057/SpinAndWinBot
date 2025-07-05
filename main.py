
import os
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to Spin and Win Bot! Spin to try your luck 🎉")

def spin(update: Update, context: CallbackContext):
    # Simple spin logic: randomly win or lose
    import random
    outcomes = ["🎉 Congratulations! You won!", "😞 Sorry! Try again next time."]
    result = random.choice(outcomes)
    update.message.reply_text(result)

def main():
    TOKEN = os.getenv("BOT_TOKEN")
    if not TOKEN:
        # fallback if environment variable not set
        TOKEN = "7734449850:AAH7pFYY9aX4sqKcKOENR_vzU63miOHcmqA"

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("spin", spin))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
