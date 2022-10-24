"""Импотр необходимых библиотек"""
from flask import render_template, Blueprint, request
from functions import *

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates", url_prefix="/")


@main_blueprint.route('/')
def home():
    """Загрузка начальной страницы"""
    return render_template('index.html')


@main_blueprint.route("/list")
def page_tag():
    """Загрузка страницы по запросу пользователя"""
    data_key = request.args.get('s')
    if data_key and data_key != '':
        posts = find_word(data_key)
        return render_template('post_list.html', posts=posts, data_key=data_key)
    else:
        return render_template('index.html')
