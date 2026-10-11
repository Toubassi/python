from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key = "the_secret_key"

@app.route('/', methods=['POST', 'GET'])

def index():
  if "gold" not in session:
    session['gold']=0
  if "activities" not in session:
    session['activities'] = []
  
  gold = session['gold']
  activities = session['activities']

  return render_template('index.html', gold=gold, activities=activities)

@app.route('/process_money', methods=['POST'])
def process():
  building=request.form['building']
  if building == 'cave':
    earned = random.randint(5, 10)
  elif building == 'farm':
    earned = random.randint(10, 20)
  elif building == 'house':
    earned = random.randint(2, 5)
  elif building == 'casino':
    earned = random.randint(-50, 50)
  else:
    return redirect('/')

  session['gold'] += earned

  if earned >=0:
    activity =f"Earned {earned} gold from the {building}"
  else:
    activity = f"Oh no! You went to the Casino and lost {abs(earned)} gold"

  activities = session['activities']
  activities.append(activity)
  session['activities'] = activities
  return redirect('/')

if __name__ == "__main__":
  app.run(debug=True)