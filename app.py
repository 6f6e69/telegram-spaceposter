from environs import Env
import requests
import pathlib
import urllib.parse
import random
from datetime import datetime


def get_extension_from_url(url: str):
    path = urllib.parse.urlsplit(url).path
    return pathlib.PurePath(path).suffix


def download_images(url_list: list,
                    save_directory: str,
                    image_prefix: str,
                    api_key: str = None):
    pathlib.Path(save_directory).mkdir(exist_ok=True, parents=True)
    params = {}
    if api_key:
        params = {
            'api_key': api_key
        }
    for _, url in enumerate(url_list):
        with requests.get(url=url, params=params) as response:
            response.raise_for_status()
            data = response.content
        image_extension = get_extension_from_url(url)
        if not image_extension:
            continue
        full_save_path = pathlib.Path(save_directory,
                                      f'{image_prefix}_{_}{image_extension}')
        with open(full_save_path, 'wb') as file:
            file.write(data)


def fetch_spacex_last_launch(api_url: str, save_directory: str):
    with requests.get(api_url) as response:
        response.raise_for_status()
        images_urls = response.json()['links']['flickr']['original']
    download_images(images_urls, save_directory, 'spacex')


def fetch_random_nasa_apod_images(api_url: str,
                                  save_directory: str,
                                  api_key: str):
    images_count = random.randint(30, 50)
    payload = {
        'count': images_count,
        'api_key': api_key,
    }
    with requests.get(api_url, params=payload) as response:
        response.raise_for_status()
        images_urls = [image['url'] for image in response.json()]
    download_images(images_urls, save_directory, 'nasa_apod')


def fetch_random_nasa_epic_images(api_url: str,
                                  save_directory: str,
                                  api_key: str):
    payload = {
        'api_key': api_key,
    }
    images_list_url = urllib.parse.urljoin(api_url, 'api/natural')
    with requests.get(images_list_url, params=payload) as response:
        response.raise_for_status()
        images = response.json()
    picked_images = random.sample(images, random.randint(5, 10))
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
    fetch_spacex_last_launch(env('SPACEX_API_URL'), env('SPACEX_SAVE_DIR'))
    fetch_random_nasa_apod_images(env('NASA_APOD_API_URL'),
                                  env('NASA_SAVE_DIR'),
                                  env('NASA_API_KEY'))
    fetch_random_nasa_epic_images(env('NASA_EPIC_API_URL'),
                                  env('NASA_SAVE_DIR'),
                                  env('NASA_API_KEY'))
