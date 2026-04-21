# atividade-somativa1-python

Este projeto foi preparado em **Python** com **Flask**, contendo testes automatizados, fluxo de **CI/CD** com GitHub Actions e execução em **Docker**, conforme os requisitos das atividades formativas e da atividade somativa.

## Funcionalidades

- Endpoint principal `GET /`
- - Endpoint de verificação `GET /health`
  - - Testes automatizados com `pytest`
    - - Pipeline de CI para instalar dependências e rodar testes
      - - Pipeline de CD para empacotar a aplicação
        - - Dockerfile para executar a aplicação em contêiner
         
          - ## Execução local
         
          - ```bash
            pip install -r requirements.txt
            python app/main.py
            ```

            A aplicação ficará disponível em `http://localhost:5000`.

            ## Testes

            ```bash
            pytest
            ```

            ## Docker

            ### Build da imagem

            ```bash
            docker build -t orientacao-somativa1 .
            ```

            ### Execução do contêiner

            ```bash
            docker run -d -p 5000:5000 --name orientacao-app orientacao-somativa1
            ```

            ### Verificação

            ```bash
            curl http://localhost:5000/health
            ```
            
