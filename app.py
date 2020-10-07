from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods=['GET'])
def home():

    json = {
        "123": 123
    }

    return json  

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

