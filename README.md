# Enxerto-Agro-teste

 - Instale o seu ambiente virtual com o seguinte comando: **python -m venv venv**
 - Entre no seu ambiente virtual com o comando: **source venv/Scripts/activate (windows)**
 - Baixe as dependências do projeto que estão no arquivo requirements.txt com o comando: **pip install -r requirements.txt**
 - A API foi desenvolvida em  **PostgreSQL**. Para iniciar basta criar e configurar um arquivo  **.env** com base no arquivo  **.env_example**. Não se esqueça de criar o db com o mesmo nome que colocar no .env.

#

## Requisitos do Serviço

Esse serviço possui uma API REST para que os demais serviços consigam criar, listar, atualizar e deletar os links do banco de dados.

- O banco de dados utilizado foi  o **PostgreSQL**.
- **Somente o ADMIN consegue criar outros usuários. Para criar um usuário admin, utilize o comando: python manage.py create_admin**

#

# Endpoints do serviço

| Método | Endpoint             | Responsabilidade                               |
| ------ | -------------------- | ---------------------------------------------- |
| POST   | api/user/login/      | Faz login do usuário                           |
| POST   | api/user/            | Cria um novo usuário                           |
| GET    | api/user/            | Lista todos os usuários                        |
| GET    | api/user/id/         | Lê um usuário com base no ID                   |
| PATCH  | api/user/id/         | Atualiza um usuário                            |
| DELETE | api/user/id/         | Deleta um usuário                              |
| POST   | api/task/            | Cria uma task                                  |
| GET    | api/task/            | Lista todas as tasks                           |
| GET    | api/task/list/todo   | Lista todas as tasks com status = "todo"       |
| GET    | api/task/id/         | Lê uma task com base no ID                     |
| PATCH  | api/task/id/         | Atualiza uma task                              |
| DELETE | api/task/id/         | Deleta uma task                                |
| DOCS   | api/docs/swagger-ui/ | Acesso a documentação                          |


