from flask import Flask
import json
app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "name": "Miguel",
        "idade":19
    },
    {
        "id": 2,
        "name": "Gustavo",
        "idade": 19
    },
    {
        "id": 3,
        "name": "Gabriel",
        "idade":19
    }
]

tasksJSON = json.dumps(tasks)

@app.route('/teste', methods=['GET'])
def hello_world():
    return tasksJSON, 401

if __name__ == '__main__':
    app.run()
