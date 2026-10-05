from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello():
  return "Hello world!"

@app.route('/Champion')
def hello():
  return "Champion!"

@app.route('/say/<name>')
def hello2(name):
  return f"Hi {name}!"

app.route('/repeat/<num>/hello')
def hello3(num):
  return (f"Hi"*35)

if __name__ == "__main__":
  app.run(debug=True)