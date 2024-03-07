### Projeto API com FastAPI + PostgreSQL + Docker Compose

## Etapas Realizadas
1. Criar estrutura do Projeto
2. Escrever códigos dos arquivos
3. Integrar com Docker
4. Integrar com DBeaver
5. Criar ambiente virtual 
6. Subir no github

## 1. Estrutura do Projeto:
repo_root:
	/backend 
	  /app
			app.py
	  /db
    main.py
    
	/frontend **
	.gitignore
	readme.md
	docker-compose.yml

## 2. Códigos dos arquivos:
- backend/main.py
- backend/app/api.py
- docker-compose.yml

## 3. Integrando com Docker:
Terminal Integrado do Docker:
docker-compose.yml -> bot dir -> Abrir no terminal integrado

Comandos:
docker-compose ps       ->> lista os containers do docker
docker-compose up -d    ->> cria o container 

  #### Inserir print terminal do docker

## 4. Integrando com DBeaver:
-> DBeaver -> nova conexão -> PostgreSQL

Configurar conexões
-> Testar conexão -> Download -> Ok -> Concluir

## 5. Criando Ambiente Virtual
Terminal: Command Prompt

Comandos terminal Windows:
cd backend
python -m venv env
env/Scripts/activate 

(env)pip install -r requirements.txt
(env)pip freeze
(env)python main.py

ou 

Comandos terminal MacOS:
cd backend
python3 -m venv env
source env/bin/activate 

(env)pip install -r requirements.txt
(env)pip freeze
(env)python3 main.py   -> Startando a aplicação


No browser:
http://localhost:8000/
#### colocar img browser

ou http://localhost:8000/docs
para acessar o Swagger

#### colocar img browser

## 6. Subir no Github
Na pasta root -> Terminal:

git init
git add .
git commit -m "Fazer o commit"
git remote add origin https://...
git push -u origin main




### Passos futuros
cd frontend
npm install
npm run start
ir para http://localhost:3000

docker compose up -d

# default
engine = create_engine("postgresql://scott:tiger@localhost/mydatabase")

# psycopg2
engine = create_engine("postgresql+psycopg2://scott:tiger@localhost/mydatabase")

# pg8000
engine = create_engine("postgresql+pg8000://scott:tiger@localhost/mydatabase")
More notes on connecting to PostgreSQL at PostgreSQL.

MySQL
The MySQL dialect uses mysqlclient as the default DBAPI. There are other MySQL DBAPIs available, including PyMySQL: