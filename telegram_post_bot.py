from environs import Env
import telegram
import pathlib
import random


def get_random_image_path(path: str) -> str:
    images = list(pathlib.Path(path).iterdir())
    return str(random.choice(images))


if __name__ == '__main__':
    env = Env()
    env.read_env()
    bot = telegram.Bot(token=env('TG_BOT_KEY'))
    chat_id = env('TG_GROUP_ID')
    random_image_path = get_random_image_path('images')
    bot.send_photo(chat_id=chat_id, photo=open(random_image_path, 'rb'))
