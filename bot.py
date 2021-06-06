from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Bienvenido al bot')
if __name__ == '__main__':

    updater= Updater(token='1817000727:AAEo2uWuWutI9xKpZx_FCB7eX5gPtKlHfa0', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))


    # add handler

    updater.start_polling()
    updater.idle()
