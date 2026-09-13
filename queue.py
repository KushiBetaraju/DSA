# Queue Implementation

class Queue:
    def __init__(self):
        self.queue = []

    # Adding an element to the queue
    def enqueue(self, item):
        self.queue.append(item)
        print(item, "Added an element")

    # Checking whether the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # Removing an element from the queue
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print(self.queue.pop(0), "removed from queue")

    # Returns the value of the front element
    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Front element is:", self.queue[0])

    # Returns the size of the queue
    def size(self):
        return len(self.queue)

    # Removes all elements from the queue
    def clear(self):
        self.queue.clear()
        print("Queue is cleared")

    # Displays the queue
    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Queue:", self.queue)


# Creating a Queue object
Q = Queue()

while True:
    print("\nChoose the following operation to perform on Queue:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Is Empty")
    print("4. Peek")
    print("5. Size")
    print("6. Clear")
    print("7. Display Queue")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        ele = int(input("Enter the Element to insert to the queue: "))
        Q.enqueue(ele)

    elif choice == 2:
        Q.dequeue()

    elif choice == 3:
        print("Is Queue empty?", Q.isEmpty())

    elif choice == 4:
        Q.peek()

    elif choice == 5:
        print("Queue size:", Q.size())

    elif choice == 6:
        Q.clear()

    elif choice == 7:
        Q.display()

    elif choice == 8:
        print("Program ended")
        break

    else:
        print("Invalid Choice")
