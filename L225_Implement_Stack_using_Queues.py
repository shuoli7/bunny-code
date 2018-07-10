# In this problem, we want to implement the following operations (push, pop, top, empty) of a stack using queues.

# To keep track of the top element, we use queue 1 to store the top element,
# and we use queue 2 to store previous elements.

# When we operate pop, we remove the top element in queue 1,
# and push all element in queue 2 to the empty queue 1, except one element.
# Then, queue 2 has the top element in the stack.
# At the end, we swap queue 1 and queue 2.

# When operating top, we return the element in queue 1

# When operating empty, we check the length of both queues.
# if both queues are empty, then the stack is empty.

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
        self.curr_top = None
        
    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if self.queue1:
            self.queue2.append(self.queue1.pop())
        self.queue1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if len(self.queue1) > 0:
            self.curr_top = self.queue1.pop()
            
        #self.queue1.pop(0) 
        while len(self.queue2) > 1:
            self.queue1.append(self.queue2.pop(0))   
        self.queue1, self.queue2 = self.queue2, self.queue1
            
        return self.curr_top

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.queue1:
            return self.queue1[0]
        return None

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue1) == 0 and len(self.queue2) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()