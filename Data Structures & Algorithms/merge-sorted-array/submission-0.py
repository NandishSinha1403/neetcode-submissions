class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = 0 
        j = 0
        temp = nums1[:m]
        boo = []
        
        for k in range(len(temp)+len(nums2)):
            if i >= m:
                boo = boo + nums2[j:]
                break
            if j >= n:
                boo = boo + temp[i:]
                break
            if temp[i] <= nums2[j]:
                boo.append(temp[i])
                i+=1 
            else :
                boo.append(nums2[j])
                j+=1
        nums1[:] = boo