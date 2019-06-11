# simplifies the adding of functions to be api endpoints
from flask_restful import reqparse, abort, Api, Resource

parser = reqparse.RequestParser()
parser.add_argument('task')

# Person
# shows a single todo item and lets you delete a todo item
class PersonController(Resource):
    def get(self):
        return "All TODODS"

    # def get(self, todo_id):
    #     return "TODOS[todo_id]"

    def delete(self, todo_id):
        #del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        #TODOS[todo_id] = task
        return task, 201