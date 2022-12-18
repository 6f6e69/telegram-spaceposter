from environs import Env
import requests
import urllib.parse
from image_downloader import download_images
import argparse
import random
from datetime import datetime


def fetch_random_nasa_epic_images(api_url: str,
                                  api_key: str,
                                  save_directory: str,
                                  pictures_number: int) -> None:
    payload = {
        'api_key': api_key,
    }
    images_list_url = urllib.parse.urljoin(api_url, 'api/natural')
    with requests.get(images_list_url, params=payload) as response:
        response.raise_for_status()
        images = response.json()
    picked_images = random.sample(images, pictures_number)
    images_urls = []
    for _, image in enumerate(picked_images):
        date = datetime.fromisoformat(image['date'])
        formatted_date = date.strftime('%Y/%m/%d')
        name = image['image']
        image_url = f'{api_url}archive/natural/{formatted_date}/png/{name}.png'
        images_urls.append(image_url)
    download_images(images_urls, save_directory, 'nasa_epic', api_key)


if __name__ == '__main__':
    env = Env()
    env.read_env()
    parser = argparse.ArgumentParser(description='Download nasa apod images')
    parser.add_argument('--number',
                        default=random.randint(5, 10),
                        choices=range(1, 11),
                        help='number of pictures between 1 and 10 to '
                             'download, by default random amount from 5 to 10')
    parser.add_argument('--save_dir',
                        default='images',
                        type=str,
                        help='directory to save images, using "images" if '
                             'parameter not set')
    args = parser.parse_args()
    fetch_random_nasa_epic_images(api_url=env('NASA_EPIC_API_URL'),
                                  api_key=env('NASA_API_KEY'),
                                  save_directory=args.save_dir,
                                  pictures_number=args.number)
