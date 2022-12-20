from environs import Env
import requests
import urllib.parse
from image_downloader import download_images
import argparse


def fetch_spacex_launch(api_url: str,
                        save_directory: str,
                        launch_id: str) -> None:
    launch_url = urllib.parse.urljoin(api_url, launch_id)
    with requests.get(launch_url) as response:
        response.raise_for_status()
        images_urls = response.json()['links']['flickr']['original']
    if not images_urls:
        print('There were no photos during the last launch.')
        return
    download_images(images_urls, save_directory, 'spacex')


if __name__ == '__main__':
    env = Env()
    env.read_env()
    SPACEX_API_URL = env('SPACEX_API_URL',
                         'https://api.spacexdata.com/v5/launches/')
    parser = argparse.ArgumentParser(description='Download spacex launch '
                                                 'photos to specific '
                                                 'directory.')
    parser.add_argument('--launch_id',
                        default='latest',
                        help='launch id, download photos from latest launch '
                        'if argument not set')
    parser.add_argument('--save_dir',
                        default='images',
                        help='directory to save images, using "images" if '
                             'argument not set')
    args = parser.parse_args()
    fetch_spacex_launch(api_url=SPACEX_API_URL,
                        save_directory=args.save_dir,
                        launch_id=args.launch_id)
