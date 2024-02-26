from flask import Flask
from flask_cors import CORS
from api import character_bp

# Criando uma instância do Flask para a aplicação principal
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Configurações adicionais da aplicação podem ser definidas aqui

# Registrando as rotas da API
app.register_blueprint(character_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
