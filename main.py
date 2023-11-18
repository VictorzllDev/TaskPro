from dotenv import load_dotenv, find_dotenv
from os import getenv
from flask import Flask, request, make_response, jsonify
from mysql import connector

load_dotenv(find_dotenv())

myDb = connector.connect(
    host=getenv("HOST"),
    user=getenv("USER"),
    password=getenv("PASSWORD"),
    database=getenv("DATABASE"),
)

myCursor = myDb.cursor()


app = Flask(__name__)

# rotas de chamadas


# GET TASKS
@app.route("/tasks", methods=['GET'])
def getTaskpro():
    command = 'SELECT * FROM tasks'
    myCursor.execute(command)
    result = myCursor.fetchall()
    data = []
    for item in result:
        data.append({
            'id': item[0],
            'title': item[1],
            'description': item[2],
            'date': item[3],
            'completion': item[4],
        })
    return make_response(jsonify(data))

# POST TASK


@app.route("/tasks", methods=['POST'])
def postTaskpro():
    data = request.json
    command = f'INSERT INTO tasks VALUES (default, "{data['title']}", "{
        data['description']}", "{data['date']}", default)'
    myCursor.execute(command)
    myDb.commit()
    return "ADD COM SUCESSO"

# CHECK COMPLETION TASK


@app.route("/tasks", methods=['PUT'])
def putTaskpro():
    data = request.json
    command = f'UPDATE tasks SET completion_task = {
        data['completion']} WHERE id = {data['id']}'
    myCursor.execute(command)
    myDb.commit()
    return "UPDATE COM SUCESSO"


# DELETE TASK

@app.route("/tasks", methods=['DELETE'])
def deleteTaskpro():
    data = request.json
    command = f'DELETE FROM tasks WHERE id = {data['id']}'
    myCursor.execute(command)
    myDb.commit()
    return "DELETE COM SUCESSO"


if __name__ == '__main__':
    app.run()

myDb.close()
myCursor.close()
