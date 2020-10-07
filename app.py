# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource#, Api
from flask_cors import CORS

app = Flask(__name__)
#api = Api(app)
cors = CORS(app)

'''
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}  

api.add_resource(HelloWorld, '/')
'''

@app.route('/', methods=['GET'])
def home():
    return {'hello': 'world Teste'}  

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)