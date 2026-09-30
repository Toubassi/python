class Backpack:
    def __init__(self, owner, coins=0):
        self.owner = owner
        self.coins = coins

    def add_coins(self, amount):
        self.coins += amount
        return self  #Fixed code here

    def spend_coins(self, amount):
        if self.coins >= amount:
            self.coins -= amount
        else:
            print("Not enough coins")
        return self

    def display(self):
        print(f"{self.owner}'s backpack has {self.coins} coins")
        return self


class Hero:
    def __init__(self, name):
        self.name = name
        self.backpack = Backpack(name)

    def collect(self, amount):
        self.backpack.coins += (amount)
        return self

    def buy_item(self, amount):
        self.backpack.spend_coins(amount)
        return self

    def gift_coins(self, other_hero, amount):
        if self.backpack.coins >= amount:
            self.backpack.coins -= amount   #added this line of code, to decrease the money for the hero that is gifting
            other_hero.backpack.add_coins(amount)
        return self


hero1 = Hero("Lina")
hero2 = Hero("Omar")

hero1.collect(50).buy_item(15).gift_coins(hero2, 20)

hero1.backpack.display()
hero2.backpack.display()