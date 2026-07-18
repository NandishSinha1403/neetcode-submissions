class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ls = []
        i = 0 
        j = 0 
        word1 = list(word1)
        word2 = list(word2)
        for k in range (len(word1) + len(word2)):
            if j >= len(word2):
                ls = ls + word1[i:]
                return "".join(ls)
            if i >= len(word1):
                ls = ls + word2[j:]
                return "".join(ls)
            if k%2==0:
                ls.append(word1[i])
                i+=1
            else:
                ls.append(word2[j])
                j+=1
        return "".join(ls)  
