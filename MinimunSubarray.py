class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i, j, sum = 0, 0, 0
        min = len(nums)+1
        while(i < len(nums) and j < len(nums)):
        	#print "%s sum = %d i = %d j = %d" %("1",sum, i, j)
        	while(sum < s and j < len(nums)):
        		sum += nums[j]
        		j = j + 1
        	#print "%s sum = %d i = %d j = %d" %("2",sum, i, j)
        	while(sum >= s and i < len(nums)):
        		sum -= nums[i]
        		i = i + 1
        	#print "%s sum = %d i = %d j = %d" %("3",sum, i, j)
        	if min > j-i+1:
        		min = j-i+1
        	if min == 1:
        		return 1
        	#print(min)
        if min == len(nums)+1:
        	return 0
        return min
s = Solution();
array = [1,2,1,4,5,6]
print(s.minSubArrayLen(1, array))
