# Input:
# A non-empty list of integers, and an integer k, representing the k most frequent elements.

# Output:
# A list with k most frequent elements.

# Solution 1:
# Sort by frequency, pick top k.
# Time complexity: O(nlogn), not meet requirements
# Space complexity: O(n)

# Solution 1:
# Sort by frequency, pick top k.
# Time complexity: O(nlogn), not meet requirements
# Space complexity: O(n)

# Solution 2:
# Priority queue, or min heap

# To solve this problem, we put each number, and its frequency from the input list to the dictionary.

# Then, we push the (frequency, number) list to the heap.
# By default, the smallest item is on the top pf heap. So we need to push each pair by the negative frequency.
# Then the number with most frequency is at the top of heap.

# Next, we iterate over the heap.
# For each round, we pop and return the largest item from the heap.
# As the item is a list with frequency and number,
# we only add the number at index 1 in the list to the result.

# We stopped at the kth round of iteration.
# At this time, we add top k frequent elements in the result. Then we return the result.

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic, res, pq = {}, [], []
        
        # Put number, and its frequency to the dictionary.
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1   
                
        for key in dic:
            heapq.heappush(pq, (-dic[key], key)) # Push the (frequency, number) list to the heap.
                                                 # By default, the smallest item is on the top of heap.
                                                 # So we need to pust each pair by the negative frequency
                                                 # Then the number with most frequency is at the top of heap
        
        for i in range(k):
            res.append(heapq.heappop(pq)[1]) # Pop and return the kth largest item from the heap.
                                             # As the item is a list with frequency and number,
                                             # we only add the number at index 1 in the list to the result 
        return res

# Time complexity: O(nlogk)
# Space complexity: O(k)

# Solution 3:
# bucket sorting

# First we build an empty dictionary. Iterate over the input list,
# put distinct number into the key set, and its frequency into the value set.

# Then, we creat a list with n + 1 empty bucket.
# Insert the key from the dictionary to the bucket at the index of its value.
# In this way, the number with least frequency was put in the first bucket.
# And the number with most frequency was put in the last bucket.
# The index of the bucket represents the frequency of that number in the bucket.

# Next, we iterate the bucket list in a reversed way,
# and concatenate all sorted buckets to the result list.
# We stop until the length of result list is equal to k.
# At this time, we get the top k frenquent element in the result list. So we return the result list.

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic, res = {}, []
        
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1   
                
        bucket = [[] for i in range(len(nums) + 1)]
        
        for key in dic:
            bucket[dic[key]].append(key)
        
        for i in reversed(xrange(len(bucket))):
            if bucket[i]:
                res.extend(bucket[i]) # Extends list by appending elements from the iterable.
            if len(res) == k:
                break
        return res

# Time complexity: O(n)
# Space complexity: O(n)