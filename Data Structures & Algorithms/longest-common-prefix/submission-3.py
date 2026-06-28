class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        strs.sort()
        m = strs[0]
        for i in range(len(m)):
            k = strs[0][i]
            flag = True
            for j in range(1,len(strs)):
                l = strs[j][i]
                if k != l:
                    flag = False
                    return "".join(ans)
            if flag == True:
                ans.append(k)
        return "".join(ans)

def minlenstr(strs):
    a =[]
    for i in strs:
        a.append(len(i))
    k = min(a)
    index= a.index(k)
    return strs[index]