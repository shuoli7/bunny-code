class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
         
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                #二分法，先判断中值是属于哪边的升序序列，
                #再根据端点值继续判断 target 该落在左边还是右边区域
                if nums[left] <= target and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1