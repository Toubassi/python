class BankAccount:
  def __init__(self, int_rate = 1.1, balance=0):
    self.int_rate = int_rate
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    print(f"you have deposited an amount of: ${amount}, your balance is: ${self.balance}")
    return self

  def withdraw(self, amount):
    if (self.balance - amount <= 0):
      print(f"Insufficient funds!")
      self.balance += amount
    else:
      self.balance -= amount
      print(f"you have withdrawn an amount of: ${amount}, your balance is: ${self.balance}")
    return self

  def display_accout_info(self):
    print(f'Balance: ${self.balance}')
    return self

  def yield_interest(self):
    if self.balance > 0:
      self.balance =+ self.balance * self.int_rate
    return self

#################################################################

class User:
  def __init__(self, name):
    self.name = name
    self.account = BankAccount(int_rate = 1.1, balance=0)

  def make_withdrawal(self, amount):
    self.account.withdraw(amount)
    return self

  def make_deposit(self, amount):
    self.account.deposit(amount)
    return self
  
  def display_user_blance(self):
    print(f"User: {self.name}, Balance: ${self.account.balance}")
    return self
  
  def yield_interest(self):
    self.account.yield_interest()
    return self

acc1 = User("Emil")
acc1.make_deposit(1000).make_withdrawal(50).yield_interest().display_user_blance()

















  # def transfer_money(self, reciever, amount):
  #   self.account -= amount
  #   reciever.account += amount
  #   print(f"You have sent an amount of ${amount}")
  #   print(f"Your balance is: ${self.account}, reciever balance is: ${reciever.account}")
  #   return self