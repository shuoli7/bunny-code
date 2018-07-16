# We are asked to implement the following operations (push, pop, peek, empty) of a queue using stacks.
# Time complexity for push is O(1)
# Time complexity for pop is O(n)
# Time complexity for peek is O(n)
# Time complexity for empty is O(1)

# To solve this problem, we need to store the elements in order in stack 1.
# Then we pop elements in stack 1 out and store them in stack 2.
# In this way, we store elements in a reversed order in stack 2.

# When we operate push, we add the new element to stack 1.

# When we operate pop, we get the top element in stack 1 first,
# and pop out the last element in stack 2, which is exactly the front element in stack 1.

# When operating peek, to obtain the top element in stack 1,
# we actually look for the last element in stack 2
# because elements are in a reversed order in stack 2.

# When operating empty, we check the length of both stacks.
# if both stacks are empty, then the queue is empty.

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.peek()
        return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()