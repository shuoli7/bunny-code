#Input is a list of numbers, and a target nuber; output should be coresponding index of two integers, whose sum is the target number
#use hashmap to store the value of the integer in "key" and coresponding index in "value"
#
#
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #First, check the boundary cases
        
        res = []
        if not nums:
            return res
        
        #Interate over the list of given nums
        dict = {}
            
        for i in range(len(nums)):
        
        #Before storing key value pair to the hashmap
        #check whether the diffrence between target and the current integer exists in the hashmap
        
            if target - nums[i] in dict:
                res.append(dict[target - nums[i]])
                res.append(i)
                
        #Creat a hashmap to store key value pair 
        
            dict[nums[i]] = i
        return res

       
#Time complexity: O(n)
#Space complexity: O(n)
                
        