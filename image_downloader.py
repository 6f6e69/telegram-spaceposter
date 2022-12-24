import requests
import pathlib
import urllib.parse


def get_extension_from_url(url: str) -> str:
    path = urllib.parse.urlsplit(url).path
    return pathlib.PurePath(path).suffix


def download_images(urls: list,
                    save_directory: str,
                    image_prefix: str,
                    params: dict = None) -> None:
    pathlib.Path(save_directory).mkdir(exist_ok=True, parents=True)
    if not params:
        params = {}
    for url_number, url in enumerate(urls, start=1):
        with requests.get(url=url, params=params) as response:
            response.raise_for_status()
            data = response.content
        image_extension = get_extension_from_url(url)
        if not image_extension:
            continue
        full_save_path = pathlib.Path(save_directory,
                                      f'{image_prefix}_{url_number}'
                                      f'{image_extension}')
        with open(full_save_path, 'wb') as file:
            file.write(data)
