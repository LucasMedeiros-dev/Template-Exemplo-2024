# Template Exemplo

Este é um projeto Django básico que demonstra como configurar e executar um aplicativo web usando o framework Django.

## Pré-requisitos

Certifique-se de ter os seguintes requisitos instalados em sua máquina:

- Python 3.x
- Django

## Configuração do Ambiente

1. Clone este repositório em sua máquina local.
2. Navegue até o diretório do projeto:

    ```bash
    cd nome_da_pasta
    ```

3. Crie um ambiente virtual:

    ```bash
    python -m venv venv
    ```

4. Ative o ambiente virtual:

    - No Windows:

      ```bash
      venv\Scripts\activate
      ```

    - No macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

5. Instale as dependências do projeto:

    ```bash
    pip install -r requirements.txt
    ```

## Executando o Projeto

1. Execute as migrações do banco de dados:

    ```bash
    python manage.py migrate
    ```

2. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

3. Abra o navegador e acesse `http://localhost:8000` para ver o aplicativo em execução.

## Informativo

1. Para alterar o Banco de Dados, antes das migrações usa-se o comando:

    ```bash
    python manage.py makemigrations
    ```
2. Para erros com o Ambiente Virtual (VENV) no Windows Com relação a permissão

    ```bash
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```


## Template Criado por:

    ```bash
     _                          __  __          _      _               
    | |   _   _  ___ __ _ ___  |  \/  | ___  __| | ___(_)_ __ ___  ___ 
    | |  | | | |/ __/ _` / __| | |\/| |/ _ \/ _` |/ _ \ | '__/ _ \/ __|
    | |__| |_| | (_| (_| \__ \ | |  | |  __/ (_| |  __/ | | | (_) \__ \
    |_____\__,_|\___\__,_|___/ |_|  |_|\___|\__,_|\___|_|_|  \___/|___/
                                                                        
    ```
