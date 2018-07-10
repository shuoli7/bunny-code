# We are asked to implement the following operations (push, pop, peek, empty) of a queue using stacks.

# To solve this problem, we need to store the elements in order of pushing in queue 1
# Then we pop out elemens in queue 1 and store them in queue 2
# In this way, we store elements in a reversed order in queue 2

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.queue1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.peek()
        return self.queue2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.queue2:
            while self.queue1:
                self.queue2.append(self.queue1.pop())
        return self.queue2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.queue1) == 0 and len(self.queue2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()