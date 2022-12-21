from environs import Env
import requests
from image_downloader import download_images
import argparse
import random


def fetch_random_nasa_apod_images(api_key: str,
                                  save_directory: str,
                                  pictures_number: int) -> None:
    payload = {
        'count': pictures_number,
        'api_key': api_key,
    }
    with requests.get(NASA_APOD_API_URL, params=payload) as response:
        response.raise_for_status()
        images_urls = [image['url'] for image in response.json() 
                       if image['media_type'] == 'image']
    download_images(images_urls, save_directory, 'nasa_apod')


def validate_images_number(number: str) -> int:
    number = int(number)
    if not 0 < number:
        raise argparse.ArgumentError
    return number


if __name__ == '__main__':
    env = Env()
    env.read_env()
    NASA_APOD_API_URL = env('NASA_APOD_API_URL',
                            'https://api.nasa.gov/planetary/apod')
    NASA_API_KEY = env('NASA_API_KEY')
    parser = argparse.ArgumentParser(description='Download nasa apod images')
    parser.add_argument('--number',
                        default=random.randint(30, 50),
                        type=validate_images_number,
                        help='number of pictures to download, '
                             'by default random amount from 30 to 50')
    parser.add_argument('--save_dir',
                        default='images',
                        help='directory to save images, using "images" if '
                             'argument not set')
    args = parser.parse_args()
    fetch_random_nasa_apod_images(api_key=NASA_API_KEY,
                                  save_directory=args.save_dir,
                                  pictures_number=args.number)
