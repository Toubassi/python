from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "secret key"

@app.route('/', methods=['GET', 'POST'])
def home():

  if 'number' not in session:
    session['number'] = random.randint(1, 100)
    session['attempts'] = 0
    session['game_over'] = False
  if 'attempts' not in session:
    session['attempts'] = 0

  message = None
  message_color=""

  if request.method == 'POST':
    if request.form.get('action') == 'restart':
      session['number'] = random.randint(1, 100)
      session['attempts'] = 0
      session['game_over'] = False
    else: 
      guess = request.form.get('guess', type=int)        
      if guess is not None:
        session['attempts'] += 1
        if guess > session['number']:
          message = "Your number is too big"
          message_color="red"
        elif guess < session['number']:
          message = "Your number is too small"
          message_color="red"
        else:
          message = (f"You got it right, the number was {session['number']}! It took you {session['attempts']} attempts to get it right!")
          message_color="green"
          session['game_over']= True

  return render_template(
    'index.html', 
    message=message, 
    game_over=session.get('game_over', False),
    message_color=message_color, attempts=session['attempts'])



if __name__ == "__main__":
  app.run(debug=True)