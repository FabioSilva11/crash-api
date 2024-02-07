# API crash de Exemplo com Flask

Esta é uma simples API construída com Flask que fornece informações sobre um jogo fictício. A API possui duas rotas principais:

## Como Executar Localmente

1. Certifique-se de ter o Python instalado.
2. Instale as dependências usando `pip install -r requirements.txt`.
3. Execute o script com `python app.py`.
4. Acesse as rotas utilizando as URLs fornecidas abaixo.

## Rota Principal ("/")

- **Descrição:** Retorna um JSON com um ID único e um valor aleatório para o ponto de crash do jogo.
- **Nenhum parâmetro necessário:** Esta rota não requer nenhum parâmetro. Ao acessá-la, você receberá um JSON com um ID único e um valor aleatório para o ponto de crash do jogo.
- **Exemplo de Resposta:**
  ```json
  {
    "id": "56d976e1-e92f-43dc-a7be-2dc27ae7e926",
    "crash_point": 8.73
  }
  ```
- **Exemplo de Uso (curl):**
  ```bash
  curl http://127.0.0.1:5000/
  ```

## Rota de Verificação ("/verificar")

- **Descrição:** Recebe dois parâmetros, `input_value` e `max_input_value`, e determina se o usuário ganhou ou perdeu com base nesses valores. Retorna um JSON com um ID único, o resultado da verificação e um indicador booleano se o usuário ganhou ou não.
- **input_value (float):** Este parâmetro representa o valor de entrada fornecido pelo usuário para o jogo. É o valor que será comparado com `max_input_value` para determinar se o usuário ganhou ou perdeu.
- **max_input_value (float):** Este parâmetro representa o valor máximo que o `input_value` pode ter para o usuário ganhar o jogo. Se `input_value` for menor ou igual a `max_input_value`, o usuário ganha; caso contrário, ele perde.
- **Exemplo de Resposta:**
  ```json
  {
    "id": "56d976e1-e92f-43dc-a7be-2dc27ae7e926",
    "result": "Você ganhou!",
    "won": true
  }
  ```
- **Exemplo de Uso (curl):**
  ```bash
  curl http://127.0.0.1:5000/verificar?input_value=5.0&max_input_value=10.0
  ```

Lembre-se de ajustar as URLs e os valores dos parâmetros conforme necessário para a sua aplicação.
```

Agora, a documentação inclui informações sobre os parâmetros necessários para a rota principal e a rota de verificação.
