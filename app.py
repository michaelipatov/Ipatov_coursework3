import logging

#logger = logging.getLogger()
#file_handler = logging.FileHandler(filename="api.log", encoding='utf-8')
#formatter = logging.Formatter("%(levelname)s : %(asctime)s : %(message)s")
#file_handler.setFormatter(formatter)
#logger.addHandler(file_handler)

logging.basicConfig(filename='api.log', level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s', encoding='utf-8')


from flask import Flask, request, render_template, jsonify
from utils import get_posts_all, get_posts_by_user, get_comments_by_post_id, search_for_posts, \
    get_post_by_post_id, path_data


app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def all_post_page():
    """Вьюшка для главной страницы"""
    posts = get_posts_all(path_data)
    return render_template('index.html', path_data=path_data, posts=posts)


@app.route("/posts/<int:post_id>")
def post_by_id_page(post_id):
    """Вьюшка для вывода поста по его id"""
    post = get_post_by_post_id(post_id)
    comments = get_comments_by_post_id(post_id)
    comments_quantity = 0
    for comment in comments:
        if post_id == comment['post_id']:
            comments_quantity += 1
    return render_template('post.html', post=post, comments=comments, comments_quantity=comments_quantity)


@app.route("/search/")
def search_page():
    """Вьюшка для поиска"""
    query = request.args.get('s', '')
    posts = search_for_posts(query)
    find_post_quantity = 0
    for post in posts:
        find_post_quantity += 1
    return render_template('search.html', query=query, posts=posts, find_post_quantity=find_post_quantity)


@app.route("/user/<user_name>")
def post_by_username(user_name):
    """Вьюшка для вывода постов пользователя"""
    posts = get_posts_by_user(user_name)
    return render_template('user-feed.html', posts=posts, user_name=user_name)


@app.errorhandler(404)
def not_found_error(error):
    """Вьюшка для вывода ошибки 404"""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """Вьюшка для вывода ошибки 500"""
    return render_template('500.html'), 500


@app.route('/api/posts', methods=["GET"])
def get_posts():
    posts = get_posts_all(path_data)
    logging.info("Запрос /api/posts")
    return jsonify(posts)


@app.route('/api/posts/<int:post_id>', methods=["GET"])
def get_posts_by_id(post_id):
    post = get_post_by_post_id(post_id)
    logging.info(f"Запрос /api/posts/{post_id}")
    return jsonify(post)


if __name__ == '__main__':
    app.run()
