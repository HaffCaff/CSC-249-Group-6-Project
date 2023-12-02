from listqueue import ListQueue
from item import Item

def menu():
    print("Welcome to Wake Cafeteria")
    print()
    print("Press 1 for OPTION")
    print("Press 2 for OPTION")
    print("Press 3 for OPTION")
    print("Press 4 for OPTION")
    print("Press 5 to EXIT")
    option = input("What can we do for you?")

    return option

def main():
    orderList = ListQueue()

    option = menu()
    while option != "5":
        if option == "1":
            Burger = Item("Burger", 5)
            orderList.add(Burger)
        elif option == "2":
            pass
        elif option == "3":
            pass
        elif option == "4":
            pass
        elif option == "5":
            pass
        option = menu()

    #Do we want to also have a people queue? So people can see the wait time to get a table?
    # Maybe I am just deleriously tired, just need to upload this to GH
    
    # Testing implmentations - its horrible dont look
    #Maybe its better to create our own using List?
    # orders = Order()

    # burger = Item()

    # burger.setName("Burger")
    # burger.setCookTime(5)
    
    # orders.getSize
    # orders.addToQ(burger)

    #print(orders)




if __name__ == "__main__":
    main()
