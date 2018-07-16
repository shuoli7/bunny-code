# In this problem, we need to design a stack that supports push, pop, top,
# and retrieve the minimum element all in constant time.

# To solve the problem, we need to initiate two stacks.
# One is used to store elements pushed in;
# The other one is used to keep track of min element
# at each moment we push a new element in first stack.

# push():
# If the number we add is less or equal to the minimum value in the min_stack,
# Or if the min_stack is empty,
# then, we add this number to both min_stack, and stack.

# pop():
# If the number we pop out is equal to the current minimum value,
# then, we pop out this number from both min_stack, and stack.

# top():
# In stack, the top element is the last added element.

# getMin():
# The minimum element is the top element in the min_stack.


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
        if len(self.min_stack) == 0 or x <= self.min_stack[-1]: # The reason we use <= instead of <:
                                                                # is because there could be multiple appearances 
                                                                # of one current min element.
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