from itertools import count

class Products():
  _id_counter = count(1)
  def __init__(self, name, price, category):
    self.id = next(Products._id_counter)
    self.name=name
    self.price = price
    self.category = category
    

  def update_price(self, percent_change, is_increased = True):
    change = self.price * (percent_change/100)
    
    if is_increased == True:
      self.price = self.price + change
    else:
      self.price = self.price - change
    return self

  def print_info(self):
    print(f"ID: {self.id}, product: {self.name}, "
      f"Price: {self.price}, Category: {self.category}")
    return self