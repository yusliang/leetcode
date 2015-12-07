class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        table = {}
        i = 0
        for i in range(0, len(nums)):
        	table[nums[i]] = i
        for i in range(0, len(nums)-1):
        	if table.get(target-nums[i]):
        		return [i+1, table.get(target-nums[i])+1]
    def kSum(self, nums, target,k):
    	list.sort(nums)
    	for i in range(k-1, len(nums)):
    		result = self.kSum(nums, target-nums[i],k-1)
            for l in result:
                l.append(i)

s = Solution()
#print s.threeSum([2, 7, 11, 15], 9)