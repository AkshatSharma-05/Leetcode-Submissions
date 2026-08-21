class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for n in nums:
            subset = []
            for k in res:
                subset.append(k + [n])
            res += subset
        
        return res