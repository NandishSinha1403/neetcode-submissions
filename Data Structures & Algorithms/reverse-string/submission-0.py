class Solution:
    def reverseString(self, nums: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(nums)//2):
            nums[i] , nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[i]


    