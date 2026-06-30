class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # dic = {}
        # for i in nums:
        #     if i in dic:
        #         dic[i] += 1
        #     else :
        #         dic[i] = 1
        # max = -1
        # key , val = 0 , 0 
        # for k,v in dic.items() :
        #     if max < v :
        #         key = k 
        #         val = v
        #         max = v

        # return key
        el = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if count == 0:
                el = nums[i]

            if el == nums[i]:
                count += 1
            else:
                count -= 1
            
        return el
            

            

