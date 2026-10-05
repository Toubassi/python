from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/Champion')
def Champion():
    return "Champion"

@app.route('/say/<name>')
def hello(name):
    return f"Hi {name}"

@app.route('/repeat/<num>/hello')
def repeat(num):
    return f"Hello"*int(num)

@app.route('/repeat/<num>/bye')
def repeat(num):
    return f"bye"*int(num)    

@app.route('/repeat/<num>/dogs')
def repeat(num):
    return f"dogs"*int(num)

if __name__ == "__main__":
    app.run(debug=True)