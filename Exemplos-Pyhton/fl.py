import flask
from flask import Flask, jsonify

#criando o flask
app = Flask(__name__)

#dados de exmplo
posts = [
    {
        'id': 1,
        'title': 'Post 1',
        'content': 'Conteudo do post 1'
    },
    {
        'id': 2,
        'title': 'Post 2',
        'content': 'Conteudo do post 2'
    }
]
#criando a rota
@app.route('/')
def index():
    return jsonify({'message': 'Bem-vindo à API de Posts!'})
@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)
@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        return jsonify(post)
    else:
        return jsonify({'message': 'Post não encontrado!'}), 404
@app.route('/posts', methods=['POST'])
def create_post():
    new_post = {
        'id': len(posts) + 1,
        'title': flask.request.json['title'],
        'content': flask.request.json['content']
    }
    posts.append(new_post)
    return jsonify(new_post), 201