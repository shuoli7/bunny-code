# Input: An integer, which represents how many rounds we need to do count and say.
# Note that n = 1, we start with "1".

# Output: A string, which contains digits that represents count and say result 
# after all rounds specified by given integer.
# For example, n = 3, "1" -> "11" -> "21".

# Solution: 
# The given integer n represents how many rounds we need to do count and say.

# The first round started with n = 1, res = "1".

# For next n - 1 rounds, we take res as the input string and iterate over it to 
# build res for next iteration.

# In each iteration, we set the first char in res as the benchmark char to count.
# We also declare a variable called count, and initiate it to 1.

# During string iteration,
# if the current char is equal to the benchmark char,
# we increment count by 1,
# if the current char is not equal to the benchmark char,
# we add count and benchmark char to res, 
# then update benchmark char with current char and reset count to 1.

class Solution(object):
    def countAndSay(self, n):
        res = "1"
        for i in range(n - 1):
            new_seq = ""
            count = 1
            char = res[0]
            for j in range(1, len(res)):
                if res[j] == char:
                    count += 1   
                else: # if the current char is not equal to the benchmark char
                    new_seq += str(count) + char # we add count and benchmark char to res
                    count = 1 # reset count to 1
                    char = res[j] # update benchmark char with current char
            res = new_seq + str(count) + char # After all iterations, 
            # we will need to add the last character and its count to the result.
        return res

# Time  Complexity: O(n * 2^n) # We have a for loop to iterate n - 1 times, 
# and in each iteration, we iterate through a 2^n long string to build input string for next iteration.

# Space Complexity: O(2^n) # through out our codes, we always maintain a string with length 2^n.