import telegram
import random

TOKEN = '<>'
UPDATE_ID = None

def main():

    bot = telegram.Bot(TOKEN)
    global UPDATE_ID

    # This will be our global variable to keep the latest update_id when requesting
    # for updates. It starts with the latest update_id if available.
    try:
        UPDATE_ID = bot.getUpdates()[-1].update_id
    except IndexError:
        UPDATE_ID = None

    while True:
        msg(bot)


def msg(bot):
    global UPDATE_ID

    for update in bot.getUpdates(offset=UPDATE_ID, timeout=10):
        chat_id = update.message.chat_id
        message = update.message.text

        if message == "/alive":
            # Reply the message
            bot.sendMessage(chat_id=chat_id,
                            text="I am alive")
        elif message == "/ping":
            bot.sendMessage(chat_id=chat_id, text="pong")

            UPDATE_ID = update.update_id + 1
        else:
            # If the message is only a word without any command
            bot.sendMessage(chat_id=chat_id, text=read_file("database_file.db")) 

def read_file(file_name):
    try:
        lines = open(file_name).read().splitlines()
    except Exception as e:
        print(str(e)) # If the file was not found.
    return random.choice(lines)

if __name__ == '__main__':
    main()