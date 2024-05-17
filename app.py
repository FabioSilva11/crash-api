import random
import uuid
import json
import hashlib
from flask import Flask, Response, request, jsonify, abort
from functools import wraps

app = Flask(__name__)

# Chave secreta para criar tokens
SECRET_KEY = "minha_chave_secreta_super_segura"

def generate_token(user_input, max_input_value):
    """Gera um token seguro baseado nos valores de entrada."""
    return hashlib.sha256(f"{user_input}:{max_input_value}:{SECRET_KEY}".encode()).hexdigest()

def require_token(f):
    """Decorator para exigir um token válido nas rotas protegidas."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.args.get('token')
        user_input = request.args.get('input_value', type=float)
        max_input_value = request.args.get('max_input_value', type=float)
        
        if not token or not user_input or not max_input_value:
            abort(400, description="Faltam parâmetros ou token inválido")

        expected_token = generate_token(user_input, max_input_value)
        if token != expected_token:
            abort(403, description="Token inválido")
        
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
def generate_json():
    """Gera um JSON com um ID único e um ponto de crash aleatório."""
    unique_id = str(uuid.uuid4())
    limit_value = random.random()
    
    if limit_value < 0.8:
        crash_point = round(random.uniform(0.1, 9.1), 2)
    else:
        crash_point = round(random.uniform(0.1, 19.5), 2)
    
    data = {"id": unique_id, "crash_point": crash_point}
    return jsonify(data)

@app.route("/verificar")
@require_token
def check_result():
    """Verifica se o valor de entrada do usuário é menor ou igual ao valor máximo permitido."""
    unique_id = str(uuid.uuid4())
    user_input = request.args.get('input_value', type=float)
    max_input_value = request.args.get('max_input_value', type=float)
    
    won = user_input <= max_input_value
    result = "Você ganhou!" if won else "Você perdeu."
    
    data = {"id": unique_id, "result": result, "won": won}
    return jsonify(data)

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

@app.errorhandler(403)
def forbidden(error):
    return jsonify({"error": str(error)}), 403

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Página não encontrada"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Erro interno do servidor"}), 500

if __name__ == "__main__":
    app.run(debug=True, ssl_context='adhoc')  # Usar HTTPS (auto-assinado para desenvolvimento)
