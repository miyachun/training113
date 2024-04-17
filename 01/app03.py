from flask import Flask
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)

output = [
    {
        "pid": "1",
        "title": "Example01",
        "price": 10,
        "img": "https://picsum.photos/id/999/1200/600",
        "isAvailable": True
    },
    {
        "id": "2",
        "title": "Example02",
        "price": 60,
        "img": "https://picsum.photos/id/1070/1200/600",
        "isAvailable": True
    }
]

class Products(Resource):
    def get(self):
        return {"products": {"Message": "Get all products..", "output": output}}, 200

api.add_resource(Products, '/products')
if __name__ == "__main__":
    app.run(debug=True)