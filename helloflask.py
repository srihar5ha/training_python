from flask import Flask
from flask_restful import Resource ,Api

app=Flask(__name__)
api=Api(app)

class HelloWorld(Resource):
    def get(self):
        return {hello:'world'}

api.add_resource(HelloWorld,'/helloworld')

class Indexpage(Resource):
    def get(self):
        return ("this is indx page, enter proper end point")
api.add_resource(Indexpage,'/')

if __name__=="__main__":
    app.run(host='192.168.0.47',port='1234',debug=True)