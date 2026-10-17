from store import Store
from products import Products


supermarket = Store('supermarket')

milk = Products('Milk', 10, 'Dairy')
bread = Products('Bread', 5, 'Bakery')
cheese = Products('Cheese', 20, "Dairy")

supermarket.add_product(milk).add_product(bread).add_product(cheese).sell_product(bread.id).add_product(bread).inflation(10).sell_product(bread.id).add_product(bread).set_clearance('Bakery', 10).sell_product(bread.id)


# supermarket.inflation(10)
# supermarket.set_clearance('Dairy', 20)

# milk.print_info()
# bread.print_info()

# supermarket.sell_product(1)
# supermarket.sell_product(0)
