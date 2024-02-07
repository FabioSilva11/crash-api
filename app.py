import random
import uuid
import json
from flask import Flask, Response, request

app = Flask(__name__)

@app.route("/")
def generate_json():
    unique_id = str(uuid.uuid4())  # Gera um ID único
    limit_value = random.random()
    
    if limit_value < 0.8:
        crash_point = round(random.uniform(0.1, 9.1), 2)
    else:
        crash_point = round(random.uniform(0.1, 19.5), 2)
    
    data = {"id": unique_id, "crash_point": crash_point}
    
    json_data = json.dumps(data, ensure_ascii=False)
    return Response(json_data, content_type='application/json; charset=utf-8')

@app.route("/verificar")
def check_result():
    unique_id = str(uuid.uuid4())  # Gera um ID único
    user_input = request.args.get('input_value', type=float)
    max_input_value = request.args.get('max_input_value', type=float)
    
    won = user_input <= max_input_value
    result = "Você ganhou!" if won else "Você perdeu."
    
    data = {"id": unique_id, "result": result, "won": won}
    
    json_data = json.dumps(data, ensure_ascii=False)
    return Response(json_data, content_type='application/json; charset=utf-8')

if __name__ == "__main__":
    app.run(debug=True)
