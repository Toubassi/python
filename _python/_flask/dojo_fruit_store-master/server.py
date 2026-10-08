from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    strawberry_from_form=request.form['strawberry']
    raspberry_from_form=request.form['raspberry']
    apple_from_form=request.form['apple']
    blackberry_from_form=request.form['blackberry']
    first_name_from_form=request.form['first_name']
    last_name_from_form=request.form['last_name']
    student_id_from_form=request.form['student_id']
    return render_template(
        "checkout.html", 
        first_name_on_template=first_name_from_form,
        last_name_on_template=last_name_from_form,
        strawberry_on_template=strawberry_from_form,
        raspberry_on_template=raspberry_from_form,
        apple_on_template=apple_from_form,
        blackberry_on_template=blackberry_from_form,
        student_id_on_template=student_id_from_form,
        count=int(request.form['blackberry'])+int(request.form['apple'])+int(request.form['strawberry'])+int(request.form['raspberry'])
        )

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    