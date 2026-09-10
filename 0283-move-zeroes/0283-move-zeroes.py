class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes+=1
        
        for _ in range(zeroes):
            nums.remove(0)
        
        for _ in range(zeroes):
            nums.append(0)
        
        return