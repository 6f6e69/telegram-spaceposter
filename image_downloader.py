import requests
import pathlib
import urllib.parse


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
                                      f'{image_prefix}_{_+1}{image_extension}')
        with open(full_save_path, 'wb') as file:
            file.write(data)
