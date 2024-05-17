# Como usar a API Flask melhorada Para gerar pontos de crash, como a blazer

Para usar a API Flask melhorada, você precisará interagir com duas rotas principais: a rota raiz ("/") e a rota de verificação ("/verificar"). Abaixo estão os exemplos de como fazer isso usando cURL e Python.

## Passo a Passo para Usar a API

### 1. Inicializar o Servidor

Primeiro, certifique-se de que o servidor Flask está em execução. No terminal, navegue até o diretório onde o script está localizado e execute:

```bash
python seu_script.py
```

O servidor Flask estará disponível em `https://127.0.0.1:5000`.

### 2. Gerar o JSON Inicial

Faça uma solicitação GET para a rota raiz para obter um JSON contendo um `unique_id` e um `crash_point`.

**Exemplo com cURL**:

```bash
curl -k https://127.0.0.1:5000/
```

**Resposta Esperada**:

```json
{
    "id": "e.g., e6652b22-9c71-11ec-b909-0242ac120002",
    "crash_point": 5.23
}
```

**Exemplo com Python**:

```python
import requests

response = requests.get('https://127.0.0.1:5000/', verify=False)
print(response.json())
```

### 3. Verificar o Resultado

Use a rota `/verificar` para comparar o `user_input` com o `max_input_value`. Você precisará gerar um token seguro usando a função fornecida.

**Exemplo com cURL**:

```bash
# Suponha que user_input=4.5 e max_input_value=5.23
user_input=4.5
max_input_value=5.23
token=$(python -c "import hashlib; print(hashlib.sha256(f'{user_input}:{max_input_value}:minha_chave_secreta_super_segura'.encode()).hexdigest())")

curl -k "https://127.0.0.1:5000/verificar?input_value=$user_input&max_input_value=$max_input_value&token=$token"
```

**Resposta Esperada**:

```json
{
    "id": "e.g., 7cfa97a4-9c71-11ec-b909-0242ac120002",
    "result": "Você ganhou!",
    "won": true
}
```

**Exemplo com Python**:

```python
import requests
import hashlib

# Defina os valores de entrada
user_input = 4.5
max_input_value = 5.23

# Gere o token
secret_key = "minha_chave_secreta_super_segura"
token = hashlib.sha256(f"{user_input}:{max_input_value}:{secret_key}".encode()).hexdigest()

# Faça a solicitação GET com os parâmetros
params = {
    'input_value': user_input,
    'max_input_value': max_input_value,
    'token': token
}

response = requests.get('https://127.0.0.1:5000/verificar', params=params, verify=False)
print(response.json())
```

## Resumo das Rotas

- **GET /**: Gera um JSON com um `unique_id` e um `crash_point`.
  - **Resposta**:

    ```json
    {
        "id": "e6652b22-9c71-11ec-b909-0242ac120002",
        "crash_point": 5.23
    }
    ```

- **GET /verificar**: Verifica se `user_input` é menor ou igual a `max_input_value`, utilizando um token de validação.
  - **Parâmetros**:
    - `input_value`: Valor de entrada do usuário.
    - `max_input_value`: Valor máximo permitido.
    - `token`: Token de validação gerado.
  - **Resposta**:

    ```json
    {
        "id": "7cfa97a4-9c71-11ec-b909-0242ac120002",
        "result": "Você ganhou!",
        "won": true
    }
    ```

## Notas de Segurança

- **HTTPS**: Certifique-se de usar HTTPS em produção com certificados válidos.
- **Chave Secreta**: Mantenha a `SECRET_KEY` segura e não a exponha em código cliente.
- **Validação**: Valide todas as entradas e adicione mais verificações conforme necessário para seu caso de uso.

Seguindo esses passos, você poderá utilizar a API de forma segura e eficaz.

