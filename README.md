# TaskPro API

Bem-vindo ao TaskPro, uma API simples para gerenciar suas tarefas usando Python e Flask.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

## Recursos

A API TaskPro oferece operações básicas para gerenciar suas tarefas. Os recursos principais incluem:

### 1. Listar todas as tarefas

- **Endpoint:** `/tasks`
- **Método:** GET
- **Descrição:** Retorna a lista de todas as tarefas em formato JSON.

### 2. Criar uma nova tarefa

- **Endpoint:** `/tasks`
- **Método:** POST
- **Descrição:** Cria uma nova tarefa com os parâmetros obrigatórios: `title`, `description`, `date`. O formato da data deve ser "YYYY-MM-DD". O campo `completion` é opcional e possui valor padrão `false`.

#### Exemplo de corpo da solicitação:

```json
{
  "title": "Minha Primeira Tarefa",
  "description": "Uma descrição detalhada da tarefa",
  "date": "2023-11-18"
}
```

### 3. Atualizar o status de conclusão de uma tarefa

- **Endpoint:** `/tasks`
- **Método:** PUT
- **Descrição:** Atualiza o status de conclusão de uma tarefa específica. O corpo da solicitação deve conter o `id` da tarefa e o novo valor de `completion`.

#### Exemplo de corpo da solicitação:

```json
{
  "id": 1,
  "completion": true
}
```

### 4. Excluir uma tarefa

- **Endpoint:** `/tasks`
- **Método:** DELETE
- **Descrição:** Exclui uma tarefa específica com base no `id` fornecido.

#### Exemplo de corpo da solicitação:

```json
{
  "id": 1
}
```

## Como testar a API no localhost

### 1. Clonar o repositório

```bash
git clone https://github.com/victorzllDev/TaskPro.git
```

### 2. Instalar as dependências

#### Recomendamos o uso do virtualenv para isolar o ambiente.

```bash
pip install -r requirements.txt
```

### 3. Configurar as variáveis do banco de dados

#### Crie um arquivo .env na raiz do projeto e configure as variáveis do banco de dados necessárias.

```env
DB_HOST='host.exemplo.com'
DB_USER='admin'
DB_PASSWORD='admin'
DB_DATABASE='taskpro'
```

### 4. Executar a aplicação

#### Inicie a aplicação executando o seguinte comando

```bash
python main.py
```
