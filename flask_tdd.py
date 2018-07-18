from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

import pytest

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('id')

app = Flask(__name__)
api = Api(app)

class SampleApi(Resource):
    def get(self):
        return {'test' : 123 }

api.add_resource(SampleApi, '/')

class details:
    def __init__(self,name,id):
        self.name=name
        self.id= int(id)

class Employee(Resource):
    def post(self):
        args = parser.parse_args()
        user = details(args['name'],args['id'])
        return {'name':user.name,'id': user.id}

    
api.add_resource(Employee,'/emp','/emp/<int:n>')

if __name__ == '__main__':
    app.run(port=12345,debug=True)




@pytest.fixture
def client():
    app.Testing = True
    client = app.test_client()

    yield client

def test_SampleApi_get(client):
    rv = client.get('/')

    print(rv.json)
    assert rv.json['test'] == 123

def test_Employee_post(client):
    rv=client.post('/emp',data={'name':'harshga','id': 123666 })
    

    print(rv.json)
    assert rv.json['id']== 123666