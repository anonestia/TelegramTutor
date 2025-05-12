from telegram.ext import Application
from handlers.ai import handle_ai_message
from handlers.commands import reset_command
from telegram.ext import MessageHandler, CommandHandler, filters
from apikeys import BOTTOKEN

def main():
    app = Application.builder().token(BOTTOKEN).build()

    app.add_handler(CommandHandler("reset", reset_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_ai_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
