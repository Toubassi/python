class User:
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance
    self.amount = 0

  def make_withdrawal(self, amount):
    self.balance -= amount

  def make_deposit(self, amount):
    self.balance += amount
  
  def display_user_blance(self):
    print(f"User: {self.name}, Balance: ${self.balance}")

  def transfer_money(self, reciever, amount):
    self.balance -= amount
    reciever.balance += amount
    
    print(f"You have sent an amount of ${amount}")
    print(f"Your balance is: ${self.balance}, reciever balance is: ${reciever.balance}")


user1 = User("Emil", 300)
user2 = User("Sajeda", 500)
user3 = User("Manar", 1000)

user1.make_deposit(50)
user1.make_deposit(600)
user1.make_deposit(150)
user1.make_withdrawal(100)
user1.display_user_blance()
user2.make_deposit(400)
user2.make_deposit(600)
user2.make_withdrawal(100)
user2.make_withdrawal(100)
user2.display_user_blance()
user3.make_deposit(100)
user3.make_withdrawal(200)
user3.make_withdrawal(200)
user3.make_withdrawal(300)
user3.display_user_blance()
user1.transfer_money(user3, 300)