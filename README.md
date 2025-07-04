# API-Open-meteo-temperatura-por-cidade

Projeto final do curso de IA Generativa oferecido pela Generation Brasil 

# Open Meteo - Temperatura por Cidade

Este é um aplicativo de linha de comando em Python que permite consultar rapidamente a temperatura atual de várias cidades ao mesmo tempo, utilizando APIs públicas e sem necessidade de chave de autenticação.

## O que o app faz?

- Recebe nomes de cidades digitados pelo usuário (separados por vírgula).
- Busca as coordenadas de cada cidade usando a API Nominatim (OpenStreetMap).
- Consulta a temperatura atual de cada cidade na API Open-Meteo.
- Exibe os resultados lado a lado no terminal, facilitando a comparação.

## Como usar

1. **Clone o repositório e entre na pasta:**
    ```bash
    git clone https://github.com/LaisLimaDev/API-Open-meteo-temperatura-por-cidade.git
    cd API-Open-meteo-temperatura-por-cidade
    ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. **Instale as dependências:**
    ```bash
    pip install requests
    ```

4. **Execute o programa:**
    ```bash
    python -m meteo.cli
    ```

5. **Digite as cidades quando solicitado:**
    ```
    Digite os nomes das cidades separados por vírgula: Campinas, São Paulo, Rio de Janeiro
    Campinas: 22.3°C	São Paulo: 21.7°C	Rio de Janeiro: 25.1°C
    ```

## Estrutura do Projeto

```
meteo/
├── __init__.py
├── core.py
└── cli.py
tests/
└── test_core.py
```

## Como funciona

- O usuário informa os nomes das cidades.
- O programa busca as coordenadas e, em seguida, a temperatura de cada cidade.
- Os resultados são exibidos em uma linha, separados por tabulação.

## IA no desenvolvimento

Durante o desenvolvimento, utilizei IA para:
- Sugerir estrutura de pastas e organização do projeto.
- Ajudar a resolver erros de importação e execução.
- Gerar exemplos de código e boas práticas de tratamento de exceções.
- Explicar mensagens de erro e sugerir comandos do Git.

## O que aprendi e desafios

Aprendi sobre organização de projetos Python, uso de APIs públicas, tratamento de exceções e testes automatizados. O maior desafio foi lidar com imports relativos e integração com o GitHub.

