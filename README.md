# Космический Телеграм

Проект содержит в себе набор скриптов, которые позволяют автоматизировать 
скачивание изображений с сервисов космической тематики и публиковать в telegram-чаты.

- **fetch_spacex_images.py** - скачивает изображения с последнего запуска
 космических кораблей SpaceX.

- **fetch_nasa_apod_images.py** - скачивает изображения с сервиса NASA
Astronomy Picture of the Day.

- **fetch_nasa_epic_images.py** - скачивает изображения с сервиса NASA
Earth Polychromatic Imaging Camera.

- **telegram_post_bot.py** - публикует изображение в telegram-канал.

- **telegram_autopost_bot.py** - бесконечно публикует в случайном порядке изображения
из папки в telegram-канал с заданной периодичностью.

## Как установить

Убедитесь что в системе установлен интерпретатор языка Python 3.6+. 
```
python3 --version
```

Рекомендуется использовать [виртуальное окружение](https://docs.python.org/3/library/venv.html).

```
python3 -m venv env
source env/bin/activate # Unix-based
.\venv\Scripts\activate # Windows
```
Скачайте [архив](https://github.com/6f6e69/telegram-spaceposter/archive/refs/heads/main.zip) с файлами проекта и разархивируйте в рабочую директорию.

Используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Создайте в рабочей директории .env файл с переменными среды необходимыми для работы скриптов.

#### Переменные окружения **fetch_spacex_images.py**
Для работы скрипта необходима актуальная ссылка на [SpaceX REST API](https://github.com/r-spacex/SpaceX-API).
```ini
SPACEX_API_URL=https://api.spacexdata.com/v5/launches/
```
---
#### Переменные окружения **fetch_nasa_apod_images.py**
Для работы скрипта необходим API-token NASA и [актуальная ссылка на APOD API](https://api.nasa.gov/#apod).
Токен можно сгенерировать на сайте [NASA](https://api.nasa.gov/). 
```ini
NASA_APOD_API_URL=https://api.nasa.gov/planetary/apod
NASA_API_KEY=eU8SZOMKo8xYyyqnCm9o7vrnDMXYxXi6EbfbMxq
```
---
#### Переменные окружения **fetch_nasa_epic_images.py**
Для работы скрипта необходим API-token NASA и [актуальная ссылка на EPIC API](https://api.nasa.gov/#epic).
Токен можно сгенерировать на сайте [NASA](https://api.nasa.gov/). 
```ini
NASA_EPIC_API_URL=https://api.nasa.gov/EPIC/
NASA_API_KEY=eU8SZOMKo8xYyyqnCm9o7vrnDMXYxXi6EbfbMxq
```
---
#### Переменные окружения **telegram_post_bot.py**
Для работы скрипта нужен [API-токен бота](https://sendpulse.com/knowledge-base/chatbot/telegram/create-telegram-chatbot), который будет публиковать изображения, [ID группы](https://www.alphr.com/find-chat-id-telegram/) в которую будет происходить публикация, путь к директории с изображениями
для публикации.
```ini
TG_BOT_KEY=6726511440:C1nOjperaxvZmO56bUEM-f1Bjg2gsdg
TG_GROUP_ID=@telegram
DEFAULT_IMAGES_PATH=images
```
---
#### Переменные окружения **telegram_autopost_bot.py**
Для работы скрипта нужен [API-токен бота](https://sendpulse.com/knowledge-base/chatbot/telegram/create-telegram-chatbot), который будет публиковать изображения, [ID группы](https://www.alphr.com/find-chat-id-telegram/) в которую будет происходить публикация, путь к директории с изображениями
для публикации и промежуток в часах с которым будет происходить публикация.
```ini
TG_BOT_KEY=6726511440:C1nOjperaxvZmO56bUEM-f1Bjg2gsdg
TG_GROUP_ID=@telegram
DEFAULT_IMAGES_PATH=images
PUBLICATION_DELAY=4 #в часах
```
---
Пример файла для работы всех скриптов:
```ini
SPACEX_API_URL=https://api.spacexdata.com/v5/launches/
NASA_APOD_API_URL=https://api.nasa.gov/planetary/apod
NASA_EPIC_API_URL=https://api.nasa.gov/EPIC/
NASA_API_KEY=eU8SZOMKo8xYyyqnCm9o7vrnDMXYxXi6EbfbMxq
TG_BOT_KEY=6726511440:C1nOjperaxvZmO56bUEM-f1Bjg2gsdg
TG_GROUP_ID=@telegram
DEFAULT_IMAGES_PATH=images
PUBLICATION_DELAY=4
```

## Как использовать

#### **fetch_spacex_images.py**
```sh
# получить справку по использованию скрипта
python3 fetch_spacex_images.py --help

# скачать фото с последнего запуска в директорию spacex_images
python3 fetch_spacex_images.py --save_dir spacex_images

# скачать фото с конкретного запуска в директорию images
python3 fetch_spacex_images.py --launch_id 5eb87d47ffd86e000604b38a
```
---
#### **fetch_nasa_apod_images.py**
```sh
# получить справку по использованию скрипта
python3 fetch_nasa_apod_images.py --help

# скачать случайное(от 30 до 50) количество изображений в директорию nasa_apod
python3 fetch_nasa_apod_images.py --save_dir nasa_apod

# скачать 25 случайных изображений в директорию images
python3 fetch_nasa_apod_images.py --number 25
```
---
#### **fetch_nasa_epic_images.py**
```sh
# получить справку по использованию скрипта
python3 fetch_nasa_epic_images.py --help

# скачать случайное(от 5 до 10) количество изображений в директорию nasa_epic
python3 fetch_nasa_epic_images.py --save_dir nasa_epic

# скачать 4 случайных изображений в директорию images
python3 fetch_nasa_epic_images.py --number 4
```
---
#### **telegram_post_bot.py**
```sh
# получить справку по использованию скрипта
python3 telegram_post_bot.py --help

# опубликовать случайное изображение из папки по умолчанию
python3 telegram_post_bot.py

# опубликовать конкретное изображение
python3 telegram_post_bot.py --image_path nasa_apod/picture1.jpg
```
Папку по умолчанию и группу куда производится публикация можно изменить в
[переменных окружения](#переменные-окружения-telegram_post_botpy) `TG_GROUP_ID` и `DEFAULT_IMAGES_PATH`.

---
#### **telegram_autopost_bot.py**
```sh
python3 telegram_post_bot.py
```
Папку по умолчанию, группу куда производится публикация и временной промежуток между постами можно изменить в
[переменных окружения](#переменные-окружения-telegram_post_botpy) `TG_GROUP_ID`, `DEFAULT_IMAGES_PATH` и
`PUBLICATION_DELAY`.

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).