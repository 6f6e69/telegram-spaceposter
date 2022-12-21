from environs import Env
import telegram
import pathlib
import random
import time


if __name__ == '__main__':
    env = Env()
    env.read_env()
    TG_BOT_KEY = env('TG_BOT_KEY')
    TG_GROUP_ID = env('TG_GROUP_ID')
    DEFAULT_IMAGES_PATH = pathlib.Path(env('DEFAULT_IMAGES_PATH', 'images'))
    PUBLICATION_DELAY = float(env('PUBLICATION_DELAY', 4))
    bot = telegram.Bot(token=TG_BOT_KEY)
    while True:
        images_paths = list(DEFAULT_IMAGES_PATH.iterdir())
        random.shuffle(images_paths)
        for image_path in images_paths:
            if pathlib.Path(image_path).stat().st_size > (1024 * 1024 * 20):
                continue
            with open(image_path, 'rb') as photo:
                bot.send_photo(chat_id=TG_GROUP_ID,
                               photo=photo)
            time.sleep(PUBLICATION_DELAY * 60 * 60)
