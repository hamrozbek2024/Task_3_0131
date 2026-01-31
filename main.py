class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Shop:
    def __init__(self):
        self.items = []
        self.cart = []
        self.total = 0

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        for i, item in enumerate(self.items):
            print(i, item.name, item.price)

    def add_to_cart(self, index):
        self.cart.append(self.items[index])
        self.total += self.items[index].price

    def checkout(self):
        print("Xarid qilindi:", self.total)
        self.cart.clear()
        self.total = 0


shop = Shop()
shop.add_item(Item("Telefon", 3000000))
shop.add_item(Item("Naushnik", 250000))

while True:
    print("\n1.Mahsulotlar 2.Savatcha 3.To‘lov 0.Exit")
    c = input(">>> ")

    if c == "1":
        shop.show_items()
    elif c == "2":
        shop.add_to_cart(int(input("Index: ")))
    elif c == "3":
        shop.checkout()
    elif c == "0":
        break
