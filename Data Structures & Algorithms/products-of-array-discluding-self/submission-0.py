class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        back = [1]*len(nums)
        front = [1]*len(nums)
        back[0] = 1
        front[-1] = 1
        for i in range(1,len(nums)):
            back[i] = nums[i-1]*back[i-1]
        for i in range(len(nums)-2, -1,-1):
            
            front[i] = nums[i+1]*front[i+1]
        ans = [1]*len(nums)
        for i in range(len(nums)):
            ans[i] = ans[i] *front[i]*back[i]
        return ans
