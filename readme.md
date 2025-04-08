<h1 align="center"> Django CRM (Customer Relationship Manager) <img src="https://github.com/FelRFDev/Django_CRM/assets/89205473/6cf36a03-36c5-4703-b1e8-1be4499c28a3" align="center" height="100" width="280" >  
</h1>

Este repositório contém o código desenvolvido para o sistema de CRM feito utilizando Python, Django, PostgreSQL e Bootstrap 4.
<br><br>

<h2 id="DesafioDeProjeto">Características do Projeto</h2>

O objetivo do projeto é criar um sistema capaz de realizar login, autenticação e logout do usuário, além de possibilitar o cadastro de clientes
através de um formulário, editar informações de clientes cadastrados e realizar a exclusão quando necessário. Foram utilizadas ferramentas e funcionalidades
importantes do Django como:

* Class Based View e Function Based View.
* TemplateView, ListView, CreateView, UpdateView, DeleteView.
* Django Forms.
* Authenticate, login, logout.

<h3 id="Funcionalidades">Funcionalidades</h3>

- [✅] Cadastro de Clientes.
- [✅] Busca de Clientes por Nome e Sobrenome.
- [✅] Edição e exclusão de Clientes cadastrados.
- [✅] Autenticação com login e logout.

---

<h2 id="ComoExecutar">💻 Como executar o projeto</h2>

### ✅ Opção 1: Usando Docker + Docker Compose (recomendado)

> Esta é a forma ideal para rodar o projeto com todas as dependências corretamente configuradas, incluindo PostgreSQL.

1. Clone o repositório:
   ```bash
   git clone git@github.com:FelRFDev/Django_CRM.git
   ```
    ```bash
   cd Django_CRM
   ```
    ```bash
   cd crm
   ```

2. Suba os containers com:
   ```bash
   docker-compose up
   ```

3. Acesse a aplicação no navegador:
   ```
   http://localhost:8000
   ```

4. Crie o superusuário (caso ainda não tenha criado):
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

---

### ⚙️ Opção 2: Rodando localmente SEM Docker (com SQLite)

> Se você não quiser utilizar Docker, pode rodar a aplicação localmente com SQLite, uma alternativa leve e simples para testes.

1. Clone o repositório:
   ```bash
   git clone git@github.com:FelRFDev/Django_CRM.git
   ```
    ```bash
   cd Django_CRM
   ```
    ```bash
   cd crm
   ```

2. Abra o arquivo `settings.py` e substitua o bloco `DATABASES` por este:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```

3. Instale as dependências (utilize um ambiente virtual se desejar):
   ```bash
   pip install -r requirements.txt
   ```

4. Aplique as migrações:
   ```bash
   python manage.py migrate
   ```

5. Crie o superusuário:
   ```bash
   python manage.py createsuperuser
   ```

6. Rode o servidor:
   ```bash
   python manage.py runserver
   ```

7. Acesse:
   ```
   http://127.0.0.1:8000
   ```

---

<h2 id="autor">👨‍💻 Autor</h2>

- Felipe Rodrigues Fonseca

---

<h3 id="Screenshots">📸 Alguns Screenshots do Programa (Clique na imagem para ampliar!)</h3>
<div align="center">
<img src="https://github.com/FelRFDev/Django_CRM/assets/89205473/9a3c0eb7-d09c-426a-a8d3-eed8f991ffc6" align="center" height="300" width="700" ><br>
<img src="https://github.com/FelRFDev/Django_CRM/assets/89205473/2bbb7211-a8b9-4659-bef5-661f9a2091a3" align="center" height="300" width="700" >
</div>
