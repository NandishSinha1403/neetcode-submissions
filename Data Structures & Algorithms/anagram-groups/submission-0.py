class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new = strs.copy()
        for i in range(len(strs)):
            strs[i] = ''.join(sorted(strs[i]))
        
        dic = {}
        for i in range(len(strs)):
            if strs[i] not in dic:
                dic[strs[i]] = []
                dic[strs[i]].append(i)
            else :
                dic[strs[i]].append(i)
        
        ans = []
        for i in range(len(dic)):
            ans.append([])

        j = 0
        for k, v in dic.items():
            for i in v :
                ans[j].append(new[i])
            j+=1
        return ans

