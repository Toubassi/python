from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello():
  return "Hello"

@app.route('/play')
def play():
  return render_template("index.html", box_count=int(3))

@app.route('/play/<x>')
def play2(x):
  return render_template("index.html", box_count=int(x))


@app.route('/play/<x>/<color>')
def play3(x, color):
  return render_template("index.html", box_count=int(x), box_color=color)

if __name__ == "__main__":
  app.run(debug=True)