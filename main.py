from listqueue import ListQueue
from item import Item
from prepare import prepare


def menu():
    print("Welcome to Wake Cafeteria: What would you like to order?")
    print()
    print("Press 1 to Order a burger Combo.")
    print("Press 2 To Order a wing Combo.")
    print("Press 3 To Order a salad Combo.")
    print("Press 4 to See the order Queue.")
    print("Press 5 to Clear the order queue.")
    print("Press 6 to Place your order.")
    print("Press 7 to EXIT")
    option = input("Enter Option: ")
    print()

    return option


def main():
    Burger = Item("Burger", 5, 5.50)
    Wings = Item("Wings", 10, 9.00)
    Salad = Item("Salad", 3, 7.00)
    Fries = Item("Fries", 3, 3.50)
    Drink = Item("Drink", 2, 2.50)
    orderList = ListQueue()

    option = menu()
    while option != "7":
        if option == "1":
            orderList.add(Burger)
            orderList.add(Fries)
            orderList.add(Drink)
            print("Added a Burger combo to your order")
        elif option == "2":
            orderList.add(Wings)
            orderList.add(Fries)
            orderList.add(Drink)
            print("Added a Wing combo to your order")
        elif option == "3":
            orderList.add(Salad)
            orderList.add(Drink)
            print("Added a Salad combo to your order")
        elif option == "4":
            print(f"Your order contains {orderList}, totaling {len(orderList)} items for ${orderList.getOrderCost():.2f}")
            print()
        elif option == "5":
            orderList.clear()
            print(f"Order has been cleared")
            print()
        elif option == "6":
            prepare(orderList)
        option = menu()


if __name__ == "__main__":
    main()
