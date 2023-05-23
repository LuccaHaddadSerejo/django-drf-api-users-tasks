# Enxerto-Agro-teste

 - Instale o seu ambiente virtual com o seguinte comando: **python -m venv venv**
 - Entre no seu ambiente virtual com o comando: **source venv/Scripts/activate (windows)** ou **source venv/Bin/activate (linux)**
 - Baixe as dependências do projeto que estão no arquivo requirements.txt com o comando: **pip install -r requirements.txt**
 - A API foi desenvolvida em  **PostgreSQL**. Para iniciar basta criar e configurar um arquivo  **.env** com base no arquivo  **.env_example**. Não se esqueça de criar o database com o mesmo nome que colocar no .env.
 - **Somente o ADMIN consegue criar outros usuários. Para criar um usuário admin, utilize o comando personalizado: python manage.py create_admin**

#

## Requisitos do Serviço

Esse serviço possui uma API REST para criar, listar, atualizar e deletar os dados do banco de dados.

- O banco de dados utilizado foi  o **PostgreSQL**.

#

# Endpoints do serviço

| Método | Endpoint             | Responsabilidade                               | Permissão           |
| ------ | -------------------- | ---------------------------------------------- | ------------------- |
| POST   | api/user/login/      | Faz login do usuário                           | N/A                 |
| POST   | api/user/            | Cria um novo usuário                           | Somente Admin       |
| GET    | api/user/            | Lista todos os usuários                        | Somente Admin       |
| GET    | api/user/id/         | Lê um usuário com base no ID                   | Somente Admin       |
| PATCH  | api/user/id/         | Atualiza um usuário                            | Somente Admin       | 
| DELETE | api/user/id/         | Deleta um usuário                              | Somente Admin       |
| POST   | api/task/            | Cria uma task                                  | Admin e Manager     |
| GET    | api/task/            | Lista todas as tasks                           | Admin e Manager     |
| GET    | api/task/list/todo   | Lista todas as tasks com status = "todo"       | Usuário autenticado |
| GET    | api/task/id/         | Lê uma task com base no ID                     | Usuário autenticado |
| PATCH  | api/task/id/         | Atualiza uma task                              | Admin e Manager     |
| DELETE | api/task/id/         | Deleta uma task                                | Admin e Manager     |
| DOCS   | api/docs/swagger-ui/ | Acesso a documentação                          | N/A                 |


