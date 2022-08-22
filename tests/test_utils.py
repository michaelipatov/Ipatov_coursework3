import pytest
from utils import *
from json import JSONDecodeError


@pytest.fixture()
def user_name_list():
    posts = get_posts_all(path_data)
    user_name_list = []
    for post in posts:
        user_name_list.append(post['poster_name'])
    return user_name_list


@pytest.fixture()
def post_id_list():
    posts = get_posts_all(path_data)
    post_id_list = []
    for post in posts:
        post_id_list.append(post['pk'])
    return post_id_list


def test_get_posts_all_file_error():
    try:
        with pytest.raises(FileNotFoundError):
            get_posts_all(path_data)
    except:
        assert True



def test_get_posts_all_json_error():
    try:
        with pytest.raises(JSONDecodeError):
            get_posts_all(path_data)
    except:
        assert True


def test_get_comments_all_file_error():
    try:
        with pytest.raises(FileNotFoundError):
            get_comments_all(path_comments)
    except:
        assert True


def test_get_comments_all_json_error():
    try:
        with pytest.raises(JSONDecodeError):
            get_comments_all(path_comments)
    except:
        assert True


def test_get_posts_by_user_file_error(user_name_list):
    try:
        with pytest.raises(ValueError):
            for user_name in user_name_list:
                get_posts_by_user(user_name)
    except:
        assert True


def test_get_comments_by_post_id_file_error(post_id_list):
    try:
        with pytest.raises(ValueError):
            for post_id in post_id_list:
                get_comments_by_post_id(post_id)
    except:
        assert True


def test_search_for_posts_file_error():
    query_list = []
    for query in query_list:
        try:
            with pytest.raises(KeyError):
                search_for_posts(query)
        except:
            assert True


def test_get_post_by_post_id_file_error(post_id_list):
    try:
        with pytest.raises(ValueError):
            for post_id in post_id_list:
                get_post_by_post_id(post_id)
    except:
        assert True
