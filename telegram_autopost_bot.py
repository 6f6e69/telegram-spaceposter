from environs import Env
import telegram
import pathlib
import random
import time
from upload_checker import allowed_upload_size


if __name__ == '__main__':
    env = Env()
    env.read_env()
    TG_BOT_KEY = env('TG_BOT_KEY')
    TG_GROUP_ID = env('TG_GROUP_ID')
    DEFAULT_IMAGES_PATH = pathlib.Path(env('DEFAULT_IMAGES_PATH', 'images'))
    MAX_UPLOAD_IMAGE_SIZE = env('MAX_UPLOAD_IMAGE_SIZE', 20)
    PUBLICATION_DELAY = float(env('PUBLICATION_DELAY', 4))
    bot = telegram.Bot(token=TG_BOT_KEY)
    while True:
        images_paths = list(DEFAULT_IMAGES_PATH.iterdir())
        random.shuffle(images_paths)
        for image_path in images_paths:
            image_path = pathlib.Path(image_path)
            if not allowed_upload_size(image_path, MAX_UPLOAD_IMAGE_SIZE):
                continue
            with open(image_path, 'rb') as photo:
                bot.send_photo(chat_id=TG_GROUP_ID,
                               photo=photo)
            time.sleep(PUBLICATION_DELAY * 60 * 60)
