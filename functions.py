import json
import logging

logging.basicConfig(level=logging.INFO)
logger_one = logging.getLogger()


def reading_json():
    """Читаем файл json"""
    try:
        with open("posts.json", "r", encoding="UTF-8") as file:
            file_json = json.load(file)
    except FileNotFoundError:
        logging.info("Файл не найден")
        return
    else:
        return file_json


def find_word(data_key):
    """Находим совпадения из запроса на странице файла"""
    new_list = []
    data_json = reading_json()
    for data in data_json:
        if data_key.lower() in data.get("content").lower():
            new_list.append(data)
    logging.info(f"Запрос постов {data_key}")
    return new_list


def get_path(picture):
    """Проверяем расширение файла при загрузке"""
    path_file = picture.filename
    type_file = path_file.split(".")[-1]
    if type_file in ("jpg", "png", "bmp", "gif", "jpeg", "tif", "tiff"):
        picture.save(f"./uploads/images/{path_file}")
        logging.info(f"Файл {path_file} записан")
        return f"/uploads/images/{path_file}"
    else:
        logging.info(f"Неверный формат файла")
        return False


def save_json(content):
    """Сохраняем пост от пользователя в файл"""
    data_json = reading_json()
    data_json.append(content)
    with open("posts.json", "w", encoding="UTF-8") as file:
        json.dump(data_json, file, ensure_ascii=False)
        logging.info(f"Пост добавлен {content}")
