from environs import Env
import telegram
import pathlib
import random
import argparse
from upload_checker import allowed_upload_size


def get_random_image_path(path: pathlib.Path) -> pathlib.Path:
    images = list(path.iterdir())
    return pathlib.Path(random.choice(images))


def validate_filepath(filepath: str) -> pathlib.Path:
    filepath = pathlib.Path(filepath)
    if not filepath.is_file():
        print(f"Image file {filepath} doesn't exists!")
        raise argparse.ArgumentError
    if not allowed_upload_size(filepath, MAX_UPLOAD_IMAGE_SIZE):
        print(f'Allowed files less than {MAX_UPLOAD_IMAGE_SIZE}Mb.')
        raise argparse.ArgumentError
    return filepath


if __name__ == '__main__':
    env = Env()
    env.read_env()
    TG_BOT_KEY = env('TG_BOT_KEY')
    TG_GROUP_ID = env('TG_GROUP_ID')
    DEFAULT_IMAGES_PATH = pathlib.Path(env('DEFAULT_IMAGES_PATH', 'images'))
    MAX_UPLOAD_IMAGE_SIZE = env('MAX_UPLOAD_IMAGE_SIZE', 20)
    parser = argparse.ArgumentParser(description='Post images to telegram '
                                                 'group.')
    parser.add_argument('--image_path',
                        default=get_random_image_path(DEFAULT_IMAGES_PATH),
                        type=validate_filepath,
                        help='path to image, if parameter not set posts '
                             'random image')
    args = parser.parse_args()
    bot = telegram.Bot(token=TG_BOT_KEY)
    with args.image_path.open('rb') as photo:
        try:
            bot.send_photo(chat_id=TG_GROUP_ID,
                           photo=photo)
        except telegram.error.NetworkError:
            print('Network error, check internet connection!')
            exit(1)
