from flask import Flask
from flask_cors import CORS
from fruits import fruits
from vegetables import vegetables

app = Flask(__name__)
app.config.from_object(__name__)
app.register_blueprint(fruits)
app.register_blueprint(vegetables)



# configuration
DEBUG = True

# enable CORS
CORS(app)



@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    print(app.url_map)
    app.run()
