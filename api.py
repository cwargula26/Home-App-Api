# Handles general API stuffs
from flask import Flask, request

# simplifies the adding of functions to be api endpoints
from flask_restful import reqparse, abort, Api, Resource

# adds swagger documentation
from flask_restful_swagger import swagger

from Controllers.person_controller import PersonController

import json

app = Flask(__name__)

###################################
# Wrap the Api with swagger.docs. It is a thin wrapper around the Api class that adds some swagger smarts
api = swagger.docs(Api(app), apiVersion='0.1')
###################################

# @app.route("/property", methods=['GET'])
# def PropertyGet():
#     return "Hello Property"

# @app.route("/zone", methods=['GET'])
# def ZoneGet():
#     return "Hello Zone!"

# @app.route("/room", methods=['GET'])
# def roomGet():
#     return "Hello Room!"

# @app.route("/person", methods=['GET'])
# def personGet():
#     x = Person()
#     return x.get()

# @app.route("/person", methods=['POST'])
# def personCreate():
#     x = Person()
#     x.name = request.json['name']
#     x.save()
#     test = json.dumps(request.json, indent=4, sort_keys=True)
#     print(test)
#     return x.name

# @app.route("/project", methods=['GET'])
# def projectGet():
#     return "Hello Project!"

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')





# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(PersonController, '/persons/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)