class Stack:
    # Constructing a class
    def __init__(self):
        self.stack = []

    # Inserting a element to the stack
    def push(self, item):
        self.stack.append(item)
        print(item, "pushed into stack")

    # Checking whether the stack is empty
    def isEmpty(self):
        return len(self.stack) == 0

    # Removing the element from the stack
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print(self.stack.pop(), "popped from stack")

    # Returns the value of the topmost element without removing it
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Top of the element is:", self.stack[-1])

    # Returns the size of the stack
    def size(self):
        return len(self.stack)

    # Returns the very first element inserted into the stack
    def base_index(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("The base index is:", self.stack[0])

    # Resets the data structure to an empty state
    def clear(self):
        self.stack.clear()
        print("Stack cleared")


# Creating Stack object
s = Stack()

while True:
    print("\nChoose the following operations to perform on stack:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Is Empty")
    print("5. Size")
    print("6. Base Element")
    print("7. Clear")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter element: "))
        s.push(item)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        print("Is stack empty?", s.isEmpty())

    elif choice == 5:
        print("Stack size:", s.size())

    elif choice == 6:
        s.base_index()

    elif choice == 7:
        s.clear()

    elif choice == 8:
        print("Program ended")
        break

    else:
        print("Invalid choice")

    

    
        
