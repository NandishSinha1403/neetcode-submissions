class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = list(s.lower())
        new_s = []
        for i in st:
            if i.isalnum():
                new_s.append(i)
        
        return new_s == new_s[::-1]
