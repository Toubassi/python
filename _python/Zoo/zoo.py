class Animal:
  def __init__(self, name, age, health=100, happiness=100):
    self.name = name
    self.age = age
    self.health = health
    self.happiness = happiness

  def display_info(self):
    print(f"The animal's name: {self.name}, the animal's age is: {self.age}, the health level is: {self.health}, the happiness level is: {self.happiness}.")

  def feed(self):
    self.health += 10
    self.happiness += 10
    return self

class Lion(Animal):
  def __init__(self, name, age, health=100, happiness=100):
    super().__init__(name, age, health, happiness)

  def feed(self):
    self.health += 15
    self.happiness += 15
    print("Thank you for feeding me!")
    return self

class Monkey(Animal):
  def __init__(self, name, age, health=100, happiness=100):
    super().__init__(name, age, health, happiness)

  def feed(self):
    self.health += 50
    self.happiness += 50
    print("Monkey happy!")
    return self

class Tiger(Animal):
  def __init__(self, name, age, health=100, happiness=100):
    super().__init__(name, age, health, happiness)

  def feed(self):
    self.health += 5
    self.happiness += 5
    print("I want more food!")
    return self

class Zoo:
  def __init__(self, zoo_name):
    self.animals = []
    self.name = zoo_name

  def add_lion(self, name, age):
    self.animals.append(Lion(name, age))
    return self

  def add_tiger(self, name, age):
    self.animals.append(Tiger(name, age))
    return self

  def add_monkey(self, name, age):
    self.animals.append(Monkey(name, age))
    return self

  def feed(self, index):
    self.animals[index].feed()
    return self

  def print_all_info(self):
    print("-"*30, self.name, "-"*30)
    for animal in self.animals:
      animal.display_info()
    return self

zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala", 24).add_monkey("Simba", 20).add_tiger("Rajah", 15).add_tiger("Shere Khan",7).print_all_info()
zoo1.feed(0).feed(1).feed(2).feed(3).print_all_info()








