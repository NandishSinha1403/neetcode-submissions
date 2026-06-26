class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = 
        # for i in nums :
        #     count[i]+= 1
        # output=[]
        # for i in range(k):
        #     l = max(count)
        #     output.add(count.index(l))
        #     count.remove(l)
        # return output

        count = dict()
        for i in nums :
            if i in count:
                count[i] += 1
            else :
                count[i] = 1
        output = []
        for i in range(k):
            maxIndex = -1
            maxValue = -1
            for key,v in count.items():
                if v > maxValue: 
                    maxIndex = key
                    maxValue  = v
            output.append(maxIndex)
            count.pop(maxIndex,None)
        return output
