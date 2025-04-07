from flask import Flask,jsonify


#criando a instancia
app = Flask(__name__)

#dados de um exemplo real vindo de um banco de dados
posts =[
    {"id":1,"title":"Intrudção as APIs", "author":"Joana"},
    {"id":2,"title":"Trabalhando com Flask", "author":"Ana"}
]

#definindo a rota para o GET/api/posts
@app.route('/api/posts', methods=['GET'])
def get_posts():
    #retornando os posts em formato JSON
    return jsonify(posts)
#definindo a rota para o GET/api/posts/<id>
@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post=next((p for p in posts if p['id'] == post_id), None)
    if post:
        return jsonify(post)
    else:
        return jsonify({"error": "Post não encontrado"}), 404
    
    #Ininciando o servidor Flask
if __name__ == '__main__':
    app.run(debug=True, port=5001)