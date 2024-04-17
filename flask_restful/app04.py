from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

class Todo1(Resource):
    def get(self):
        # Default to 200 OK
        return {'task': 'Todo1_Hello world'}

class Todo2(Resource):
    def get(self):
        # Set the response code to 201
        return {'task': 'Todo2_Hello world'}, 201

class Todo3(Resource):
    def get(self):
        # Set the response code to 201 and return custom headers
        return {'task': 'Todo3_Hello world'}, 201, {'Etag': 'some-opaque-string'}


api.add_resource(TodoSimple, '/<string:todo_id>')
api.add_resource(Todo1, '/')
api.add_resource(Todo2, '/a')
api.add_resource(Todo3, '/b')
if __name__ == '__main__':
    app.run(debug=True)