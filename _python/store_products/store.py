class Store:
  def __init__(self, name):
    self.name = name
    self.products = []

  def add_product(self, new_product):
    self.products.append(new_product)
    return self

  def sell_product(self, id):
    product = self.products[id]
    product.print_info()
    self.products.pop(id)
    return self

  def inflation(self, percent_increase=1.1):
    for product in self.products:
      product.update_price(percent_increase, True)
    return self

  def set_clearance(self, category, percent_discount):
    self.category = category
    self.discount = percent_discount
    for product in self.products:
          if product.category == category:
            product.update_price(percent_discount, False)
    return self

class Product:
  def __init__(self, name, price, category):
    self.name = name
    self.price = price
    self.category = category

  def update_price(self, percent_change, is_increased=True):
    self.percent = percent_change / 100
    self.increase = is_increased
    if is_increased == True:
      self.price = self.price * (1+self.percent)
    else:
      self.price = self.price * (1-self.percent)
    return self

  def print_info(self):
    print(f"The name of the product: {self.name}, it's category is: {self.category}, the price is: {self.price}.")
    return self

product1 = Product('chocolate', 15, 'sweets')
product2 = Product('Milk', 10, 'dairy')
product3 = Product('cake', 20, 'sweets')

superstore = Store("SuperStore")

superstore.add_product(product1).add_product(product2).add_product(product3)

for product in superstore.products:
  product.print_info()

superstore.inflation(10)

superstore.set_clearance("sweets", 20)

superstore.sell_product(1)

print("\nRemaining products:")
for product in superstore.products:
  product.print_info()