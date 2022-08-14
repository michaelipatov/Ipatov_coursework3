import pytest
from app import app
from utils import get_posts_all, path_data


@pytest.fixture()
def posts_by_id():
    posts = get_posts_all(path_data)
    posts_id = []
    for post in posts:
        posts_id.append(post['pk'])
    return posts_id


needed_keys = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}


def test_list():
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200
    assert isinstance(response.json, list) is True


def test_id(posts_by_id):
    posts_id = posts_by_id
    for post_id in posts_id:
        response = app.test_client().get(f"/api/posts/{post_id}")
        assert response.status_code == 200
        assert isinstance(response.json, dict) is True
        for keys in needed_keys:
            assert keys in response.json.keys(), 'Неверные ключи у полученного словаря'
