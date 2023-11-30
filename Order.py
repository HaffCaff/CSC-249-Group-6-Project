# The throught process here is to have an order system, that is a queue, that will cook and complete items
# which have a time variable. Similar to the Round Robin lab, as a que is entered, the cook time will start recursively and start to 
# cook the orders. This is my thought anyway!

# Are we supposed to write the queue ourselves using List, or do we use the actual data object?
# For sake of this being a prototype - wireframe idea, I am using queue to get point across
# Though now thinking about it....maybe its better to write it ourselves via list?
import queue


class Order(object):
    def __init__(self, sourceCollection = None):
        self.orders = queue.Queue(maxsize = 3) # Our "kitchen" can only cook 3 meals at a time

    def addToQ(self, item): # Puts the item in the queue
        self.orders.put(item)
    
    def getSize(self):
        self.orders.qsize()