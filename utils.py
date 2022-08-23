import json
from json import JSONDecodeError
import pathlib

path_data = pathlib.Path('data', 'data.json')
path_comments = pathlib.Path('data', 'comments.json')


def get_posts_all(path_data):
    """Возвращает список постов"""
    try:
        with open(path_data, encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return "FileNotFoundError"
    except JSONDecodeError:
        return "JSONDecodeError"


def get_comments_all(path_comments):
    """Возвращает список постов"""
    try:
        with open(path_comments, encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return "FileNotFoundError"
    except JSONDecodeError:
        return "JSONDecodeError"


def get_posts_by_user(user_name):
    """Находит посты пользователя user_name и добавляет в список post_list"""
    post_list = []
    try:
        for user_post in get_posts_all(path_data):
            if user_name.lower() in user_post['poster_name'].lower():
                post_list.append(user_post)
        return post_list
    except ValueError:
        return "У пользователя нет постов"


def get_comments_by_post_id(post_id):
    """Находит комменты к посту post_id и добавляет в список comments_list"""
    comments_list = []
    try:
        for comments in get_comments_all(path_comments):
            if post_id == comments['post_id']:
                comments_list.append(comments)
        return comments_list
    except ValueError:
        return "У пользователя нет комментов"


def search_for_posts(query):
    """Находит посты по ключевому слову query и добавляет в список post_list"""
    post_by_query_list = []
    if query == []:
        raise KeyError
    else:
        for post in get_posts_all(path_data):
            if query.lower() in post['content'].lower():
                post_by_query_list.append(post)
        return post_by_query_list


def get_post_by_post_id(post_id):
    """Находит пост по его id"""
    try:
        for post in get_posts_all(path_data):
            if post_id == int(post['pk']):
                return post
    except ValueError:
        return "Такого поста не существует"
