# In this problem, we need to design a stack that supports push, pop, top,
# and retrieving the minimum element in constant time.

# To solve the problem, we need to initiate two stacks.
# One is used to store elements pushed in;
# The other one is used to store minimum elements.

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.min_stack) == 0 or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.top() == self.getMin():
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()