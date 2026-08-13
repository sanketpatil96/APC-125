"""18.	Create a shopping cart using a list.
Perform:
•	Add item 
•	Remove item 
•	Search item 
•	Display cart 
•	Count total items"""

cart = []

while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. Search Item")
    print("4. Display Cart")
    print("5. Count Total Items")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item to add: ")
        cart.append(item)
        print(item, "added to cart.")

    elif choice == 2:
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
            print(item, "removed from cart.")
        else:
            print("Item not found.")

    elif choice == 3:
        item = input("Enter item to search: ")
        if item in cart:
            print(item, "is available in the cart.")
        else:
            print(item, "is not in the cart.")

    elif choice == 4:
        print("Shopping Cart:", cart)

    elif choice == 5:
        print("Total items in cart:", len(cart))

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")