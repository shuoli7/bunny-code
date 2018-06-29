# Input: An integer

# Output: An string about counting and displaying characters in the former string

# Solution: 
# When n = 1, the res is "1". 
# Set the first character in the res to be the benchmark
# Iterate over the res, if the character is equal to the benchmark,
# Count increases by 1.
# If the character is not equal to the benchmark,
# add the current count and character to res, and update the benchmark character.
# Count is updated to 1 too.

# We continue iterations for (n - 1) times.

class Solution(object):
    def countAndSay(self, n):
        res = "1"
        for i in range(n - 1): # why the time limit will exceed if I use a while loop instead?
            new_seq = ""
            count = 0
            char = res[0]
            for j in range(len(res)):
                if res[j] == char:
                    count += 1   
                else: 
                    new_seq += str(count) + char
                    count = 1
                    char = res[j] 
            res = new_seq + str(count) + char
        return res

# Time  Complexity: O(n)
# Space Complexity: O(n)