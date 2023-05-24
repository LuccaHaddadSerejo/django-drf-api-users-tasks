# Enxerto-Agro-teste

 1. Instale o seu ambiente virtual com o seguinte comando: **python -m venv venv**
 2. Entre no seu ambiente virtual com o comando: **source venv/Scripts/activate (windows)** ou **source venv/Bin/activate (linux)**
 3. Instale as dependências do projeto que estão no arquivo requirements.txt com o comando: **pip install -r requirements.txt**
 4. A API foi desenvolvida em  **PostgreSQL**. Para iniciar basta criar e configurar um arquivo  **.env** na raiz do projeto com base no arquivo  **.env.example**. Não se esqueça de criar o database com o mesmo nome que colocar no .env
 5. Faça a migração das models com o seguinte comando: **python manage.py migrate**
 6. **Somente o ADMIN consegue criar outros usuários. Para criar um usuário admin, utilize o comando personalizado: _python manage.py create_admin_**
 7. Credenciais do ADMIN > **username: admin | email: admin@mail.com | password: admin1234**

## Requisitos do Serviço

Esse serviço possui uma API REST para criar, listar, atualizar e deletar os dados do banco de dados.

- O banco de dados utilizado foi  o **PostgreSQL**.
- Foi desenvolvido utilizando Django e Django-Rest-Framework.

## Endpoints do serviço

| Método | Endpoint              | Responsabilidade                               | Permissão           |
| ------ | --------------------  | ---------------------------------------------- | ------------------- |
| POST   | api/users/login/      | Faz login do usuário                           | N/A                 |
| POST   | api/users/            | Cria um novo usuário                           | Somente Admin       |
| GET    | api/users/            | Lista todos os usuários                        | Somente Admin       |
| GET    | api/users/id/         | Lê um usuário com base no ID                   | Somente Admin       |
| PATCH  | api/users/id/         | Atualiza um usuário                            | Somente Admin       | 
| DELETE | api/users/id/         | Deleta um usuário                              | Somente Admin       |
| POST   | api/tasks/            | Cria uma task                                  | Admin e Manager     |
| GET    | api/tasks/            | Lista todas as tasks                           | Admin e Manager     |
| GET    | api/tasks/list/todo   | Lista todas as tasks com status = "todo"       | Usuário autenticado |
| GET    | api/tasks/id/         | Lê uma task com base no ID                     | Usuário autenticado |
| PATCH  | api/tasks/id/         | Atualiza uma task                              | Admin e Manager     |
| DELETE | api/tasks/id/         | Deleta uma task                                | Admin e Manager     |
| DOCS   | api/docs/swagger-ui/  | Acesso a documentação                          | N/A                 |


