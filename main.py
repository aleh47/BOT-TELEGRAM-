from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Seu token do Bot
BOT_TOKEN = "8362697266:AAGQcV-vSHwopAgHmT7WtpoqAWwzWnCOMnU"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Olá! Eu sou seu bot do Telegram, estou online 🚀")

# Resposta para mensagens de texto
async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"Você disse: {user_message}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Comandos
    app.add_handler(CommandHandler("start", start))

    # Resposta para qualquer mensagem
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message))

    # Iniciar bot
    app.run_polling()

if __name__ == "__main__":
    main()
