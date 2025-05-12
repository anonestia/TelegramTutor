from telegram import Update
from telegram.ext import ContextTypes
from utils.history_utils import get_history_file_path, clear_history_file

async def reset_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    user = update.effective_user
    is_group = chat.type in ["group", "supergroup"]

    file_path = get_history_file_path(chat.id, user.id, is_group)
    clear_history_file(file_path)

    await update.message.reply_text("History has been reset.")
