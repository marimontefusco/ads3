from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

tarefas = [
    {
        "id": "1",
        "item": "Escrever matéria revista."
    },
    {
        "id": "2",
        "item": "Revisar artigo jornal."
    }
]

# nome da app
app = FastAPI()
origins = [
    "http://localhost:3000",
    "localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"]
)

# Métodos
@app.get("/", tags=["root"])
async def read_root() -> dict:  # converte o retorno em dicionario
    return {"message": "Welcome to your tarefa list."}


@app.get("/tarefa", tags=["tarefas"])
async def get_tarefas() -> dict:
    return {"data": tarefas}


@app.post("/tarefa", tags=["tarefas"])
async def add_tarefa(tarefinha: dict) -> dict:
    tarefas.append(tarefinha)
    return {
        "data": {"Tarefa added."}
    }


# crossorigin -> permite que a aplicação deixe passar os métodos para o frontend
