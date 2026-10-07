from flask import Flask, render_template, request, redirect

app=Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
  print("Got POST info")
  print(request.form)

  name_from_form=request.form['name']
  language_from_form=request.form['language']
  location_from_form=request.form['location']
  comment_from_form=request.form['comment']
  notification_from_form=request.form.get('notification')
  coding_from_form=request.form['coding']
  if notification_from_form== None:
    notification_from_form = "I do not want to recieve notifications"
  else:
    notification_from_form=request.form.get('notification')
  return render_template(
  "show.html",
  name_on_template=name_from_form,
  language_on_template=language_from_form,
  location_on_template=location_from_form,
  comment_on_template=comment_from_form,
  notification_on_template=notification_from_form,
  coding_on_template=coding_from_form
  )


if __name__ == "__main__":
  app.run(debug=True)