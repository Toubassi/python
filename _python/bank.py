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






account1 = BankAccount()
account2 = BankAccount()

account1.deposit(100).deposit(100).deposit(100).yield_interest().display_accout_info()

account2.deposit(100).deposit(100).withdraw(50).withdraw(50).yield_interest().display_accout_info()
