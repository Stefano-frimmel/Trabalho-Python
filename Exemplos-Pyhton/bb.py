import flask
from flask import Flask, request, jsonify

#criando a instancia flask
app = Flask(__name__)

#dados de exemplo (em um cenario real, vieram de um banco de dados)
posts= [
    {
        'id': 1,
        'title': 'Introdução as APIs',
        'content': 'author: João Silva'
    },
    {
        'id': 2,
        'title': 'Post 2',
        'content': 'Conteudo do post 2'
    }
]

#defininfo a rota para o get

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

#definindo a rota para o post
@app.route('/posts', methods=['POST'])
def create_post():
    new_post = request.get_json()
    new_post['id'] = len(posts) + 1
    posts.append(new_post)
    return jsonify(new_post), 201
#definindo a rota para o delete
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        posts.remove(post)
        return jsonify({'message': 'Post deleted successfully'}), 200
    else:
        return jsonify({'message': 'Post not found'}), 404
#definindo a rota para o put
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        updated_post = request.get_json()
        post.update(updated_post)
        return jsonify(post), 200
    else:
        return jsonify({'message': 'Post not found'}), 404
#iniciando o servidor
if __name__ == '__main__':
    app.run(debug=True)
# Teste com o Postman