class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        nums1 = set(nums)
        start = []
        for i in nums1:
            if i-1 not in nums1:
                start.append(i)

        lengths = []
        for i in start :
            templen = 1
            while i + 1 in nums1:
                i += 1
                templen += 1
            lengths.append(templen)
        if lengths == []:
            return 0
        return max(lengths)