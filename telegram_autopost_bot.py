from environs import Env
import telegram
import pathlib
import random
import time
from upload_checker import allowed_upload_size
import base64
import io


if __name__ == '__main__':
    env = Env()
    env.read_env()
    TG_BOT_KEY = env('TG_BOT_KEY')
    TG_GROUP_ID = env('TG_GROUP_ID')
    DEFAULT_IMAGES_PATH = pathlib.Path(env('DEFAULT_IMAGES_PATH', 'images'))
    MAX_UPLOAD_IMAGE_SIZE = env('MAX_UPLOAD_IMAGE_SIZE', 20)
    PUBLICATION_DELAY = float(env('PUBLICATION_DELAY', 0.05))
    bot = telegram.Bot(token=TG_BOT_KEY)
    while True:
        images_paths = list(DEFAULT_IMAGES_PATH.iterdir())
        random.shuffle(images_paths)
        for image_path in images_paths:
            image_path = pathlib.Path(image_path)
            if not allowed_upload_size(image_path, MAX_UPLOAD_IMAGE_SIZE):
                continue
            with open(image_path, 'rb') as photo:
                photo_as_base64 = base64.b64encode(photo.read())
            first_reconnect = True
            while True:
                current_photo = base64.b64decode(photo_as_base64)
                try:
                    bot.send_photo(chat_id=TG_GROUP_ID,
                                   photo=io.BytesIO(current_photo))
                    break
                except telegram.error.NetworkError:
                    print('Network error occured, attempt to reconnect.')
                    if first_reconnect:
                        first_reconnect = False
                        continue
                    time.sleep(1)
            time.sleep(PUBLICATION_DELAY * 60 * 60)
