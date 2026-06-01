#Question 1 — Small Shop Billing and Inventory System
inventory = {
    "rice": {"price": 120, "stock": 20},
    "milk": {"price": 90, "stock": 10},
    "bread": {"price": 60, "stock": 15},
    "eggs": {"price": 15, "stock": 30}
}
cart = {
    "rice": 2,
    "milk": 3,
    "eggs": 12
}
def process_order(inventory, cart):
    grand_total = 0

    print("---- Bill ----")

    for item, quantity in cart.items():

        if item in inventory and inventory[item]["stock"] >= quantity:

            item_total = inventory[item]["price"] * quantity
            grand_total += item_total

            inventory[item]["stock"] -= quantity

            print(f"{item} x{quantity} = NPR {item_total}")

        else:
            print(f"Sorry, not enough stock for {item}")

    print(f"\nGrand Total: NPR {grand_total}")
    print("--------------")

    print("\nUpdated Stock:")
    for item in inventory:
        print(f"{item} = {inventory[item]['stock']}")

process_order(inventory, cart)