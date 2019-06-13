# Input:
# A string, which is an absolute path for a file in unix style

# Output:
# A string, which is simplified path for input

# Solution:
# For a path of unix style,
# it always begin with "/", , which is the root directory;
# a dot "." represents current directory;
# double dot ".." represents parent directory.

# So we use stack to solve this problem.

# First, we split the input string to a list of strings without "/".

# Then, we iterate over the list.

# When we come across "..", we pop the top element out.
# When we come across ".", we do nothing.
# When we come across any file name, we push it to stack.

# At the end, we transform the stack to a string, each element in the stack start by "/".

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/') # split the input string to a list of strings without "/".
        stack = []
        for element in path:
            if element:
                if element == '..':
                    if len(stack) > 0:
                        stack.pop()
                elif element == ".":
                     continue
                else:
                    stack.append(element)
        return '/' + '/'.join(stack)
    
# Time complexity: O(n)
# Space complexity: O(n)