from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "review-key"

menu = {
    "Tea": 2.00,
    "Coffee": 3.00,
    "Juice": 4.00
}

@app.route("/")
def home():
    if "orders" not in session:
        session["orders"] = []

    if "total" not in session:
        session["total"] = 0

    return render_template("index.html")


@app.route("/order", methods=["POST"])
def saveOrder():
    item = request.form.get("item")
    quantity = int(request.form.get("quantity"))
    price = menu[item]

    if not item or not quantity:
        return redirect('/')

    try:
        quantity = int(quantity)
    except ValueError:
        return redirect('/')

    if quantity < 1:
        return redirect('/')

    price = menu[item]

    order = {
        "item": item,
        "quantity": quantity,
        "price": price
    }

    orders = session["orders"]
    orders.append(order)
    session["orders"] = orders

    session["total"] += quantity * price

    return redirect("/summary")


@app.route("/summary")
def summary():
    orders = session['orders']
    total = sum(
        order['quantity'] * order['price']
        for order in orders
    )
    return render_template(
        "summary.html",
        orders=orders,
        total=total
    )


@app.route("/clear", methods=['POST'])
def clear():
    session["orders"] = []
    session["total"] = 0

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
