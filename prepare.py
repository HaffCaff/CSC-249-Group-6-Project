"""
File: prepare.py
Logic to handle the "cooking" of the menu items
"""
from item import Item
from listqueue import ListQueue


def prepare(order_queue):
    total = 0
    stations = 2
    while len(order_queue) > 0:
        # var to hold current job
        order = order_queue.peek() # .getCookTime()
        # ugly, but var to hold current job that is mutable
        currentOrder = order_queue.peek()
        # minus 2 ( 1 per oven?), if remainder do the thing (probably should use modulo (%) here....)
        currentOrder.cookTime -= stations
        if currentOrder.cookTime <= 0:  # if current minus 2 is less than 0, job is complete and popped, on to next job
            print(f"Current item being prepared: {order}")
            print("Item is finished!")
            order_queue.pop()
            total += 1
            print(f"Order Queue: {order_queue}")
            print()
        else:
            print(
                f"Current item being prepared: {order}")  # if current - 2 is greater than 0, job is not done, added to end, popped from beginning and on to next task
            print(f"Item is still cooking, Remaining cook time: {order.getCookTime()} minutes. Returning to end of queue")
            order_queue.add(currentOrder)
            order_queue.pop()
            print(f"Job Queue: {order_queue}")
            print()
    print(f"Order Completed in {total} cycles for an total cook time of {total * 2} minutes")
    print()

# Uncomment to test!, Comment when done testing
# def main():
#
#     orders = ListQueue()
#     Burger = Item("Burger", 5, 5.50)
#     Wings = Item("Wings", 10, 9.00)
#     Salad = Item("Salad", 3, 7.00)
#     Fries = Item("Fries", 3, 3.50)
#     Drink = Item("Drink", 2, 2.50)
#
#     orders.add(Burger)
#     orders.add(Drink)
#     orders.add(Fries)
#     orders.add(Wings)
#     orders.add(Drink)
#     orders.add(Fries)
#     orders.add(Salad)
#     orders.add(Drink)
#
#
#     print("Initial job queue:", orders)
#     prepare(orders)
#
#
# if __name__ == "__main__":
#     main()
