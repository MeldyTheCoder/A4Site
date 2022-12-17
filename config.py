import os

# имя сайта
site_name = 'Сайт от Кирилла Грошелева'

# youtube ключ авторизации
youtube_api_key = 'AIzaSyCGvU_3YzJhzk6pp3U-KZyL8FRRzPxa32s'

# ссылка на видео с канала
channel_id = 'UC2tsySbe9TNrI-xh2lximHA'

# корневой каталог
root_path = os.path.dirname(__file__)

# каталог со страницами
templates_path = os.path.join(root_path, 'templates')

# каталог со статическими файлами
static_path = os.path.join(root_path, 'static')
