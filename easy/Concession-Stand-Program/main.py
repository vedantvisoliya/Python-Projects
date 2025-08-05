# python concession stand program

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25,
}

cart = []
total = 0

print("------------ MENU ------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------------")

while True:
    food = input("Select an item (q for quit): ").lower()
    if (food == 'q'):
        break
    elif menu.get(food) is not None:
        cart.append(food)
        total += menu.get(food)
    else:
        print("Selected item is not in the menu.")

print("--------- Your Cart ---------")
print("cart :", end=" ")
for food in cart:
    print(f"{food}", end=", ")
print()
print(f"total: ${total:.2f}")
print("-----------------------------")