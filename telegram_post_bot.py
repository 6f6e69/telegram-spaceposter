from environs import Env
import telegram

if __name__ == '__main__':
    env = Env()
    env.read_env()
    bot = telegram.Bot(token=env('TG_BOT_KEY'))
    bot.send_message(text='Hello!', chat_id=env('TG_GROUP_ID'))
