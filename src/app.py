from flask import Flask

# __name__
app = Flask(__name__)

@app.route('/')
def hello_method():
    return 'Hello world'

if __name__ == '__main__':
    app.run(port=4999)
