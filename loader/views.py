"""Импорт необходимых библиотек"""
from flask import render_template, Blueprint, request
from functions import *

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates", url_prefix="/")


@loader_blueprint.route("/post")
def page_post_form():
    return render_template('post_form.html')


"""Загружает информацию от пользователя в файл"""


@loader_blueprint.route("/post", methods=["POST"])
def page_post_upload():
    pictures = request.files.get("picture")
    content = request.form.get("content")
    path_file = get_path(pictures)
    if path_file is False:
        return render_template('post_form.html')
    else:
        save_json({"pic": path_file, "content": content})
        return render_template("post_uploaded.html", path_file=path_file, content=content)
