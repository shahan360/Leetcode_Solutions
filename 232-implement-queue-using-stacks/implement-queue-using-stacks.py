class MyQueue:

    def __init__(self):
        # Initialize two stacks
        self.stack1 = []
        self.stack2 = []
        # No need to initialize size as we can use len() on the stacks
        

    def push(self, x: int) -> None:
        # Push element to the first stack
        self.stack1.append(x)
        # No need to return anything as per problem statement
        return None
        

    def pop(self) -> int:
        # If stack2 is empty, move elements from stack1 to stack2
        if self.stack2 == []:
            while self.stack1 != []:
                self.stack2.append(self.stack1.pop())
        # Pop the top element from stack2 and return it
        if self.stack2 == []:
            return None
        return self.stack2.pop()   

    def peek(self) -> int:
        # If stack2 is empty, move elements from stack1 to stack2
        if self.stack2 == []:
            while self.stack1 != []:
                self.stack2.append(self.stack1.pop())
        # Return the top element from stack2 without removing it
        if self.stack2 == []:
            return None
        return self.stack2[-1]  # Return the last element of stack2, which is the front of the queue

    def empty(self) -> bool:
        # Return True if both stacks are empty, False otherwise
        return self.stack1 == [] and self.stack2 == []
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()