class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_lst = list(s)
        t_lst= list(t)
        for i in t_lst:
            if i in s_lst:
                s_lst.remove(i)
            else:
                return False
        if len(s_lst) != 0:
            return False

        return True