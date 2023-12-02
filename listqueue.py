"""
File: listqueue.py
A list-based implementation of queue
Extended for Project
"""


class ListQueue(object):

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = []
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if the queue is empty, or False otherwise."""
        return len(self) == 0

    def __len__(self):
        """Returns the number of items in the queue."""
        return len(self.items)

    def __str__(self):
        """Returns the string representation of the queue."""
        return "{" + ", ".join(map(str, self.items)) + "}"

    def __iter__(self):
        """Supports iteration over a view of the queue."""
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def __add__(self, other):
        """Returns a new queue containing the contents
        of self and other."""
        newList = self
        for item in other:
            newList.items.append(item)
        return newList

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        otherIter = iter(other)
        for item in self:
            if item != next(otherIter):
                return False
        return True

    def peek(self):
        """Returns the item at the front of the queue.
        Raises IndexError if queue is not empty."""
        return self.items[0]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        return self.items.clear()

    def add(self, item):
        """Inserts item at the rear of the queue."""
        self.items.append(item)

    def pop(self):
        """Removes and returns the item at the front of the
        queue. Raises IndexError if queue is not empty."""
        try:
            return self.items.pop(0)
        except IndexError:
            return "Queue is empty"

    # Project Specific Methods

    def getOrderCost(self):  # Get total cost of order
        total = 0
        for items in self.items:
            total += items.getCost()
        return total

# def main():
#     lyst = [8, 2, 4, 7, 6, 1]
#     print("The list of items added is:", lyst)
#     b = ListQueue(lyst)
#     print("The queue's size:", len(b))
#     print("The queue's string:", b)
#     print()

#     print("Add 5")
#     b.add(5)
#     print("The queue's string:", b)
#     print()
#     print("Peek")
#     print("Item at front of the queue:", b.peek())
#     print("The queue's string:", b)
#     print()
#     print("Pop")
#     print("Item popped:", b.pop())
#     print("The queue's string:", b)
#     print()
#     print("c = ListQueue(b)")
#     c = ListQueue(b)
#     print("b == c?", b == c)
#     print()
#     print("d = ListQueue([1, 2, 3, 4, 5, 6])")
#     d = ListQueue([1, 2, 3, 4, 5, 6])
#     print("b == d?", b == d)
#     print()
#     print("e = b + d")
#     e = b + d
#     print("Queue e's string:", e)
#     print("Is e empty?", e.isEmpty())
#     e.clear()
#     print("Clear e")
#     print("Is e empty?", e.isEmpty())
#     print("The queue's string:", e)
