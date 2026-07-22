class Solution:

    def encode(self, strs: List[str]) -> str:
        new = ""
        for i in strs:
            new = new + i + "~"
        return new 

    def decode(self, s: str) -> List[str]:
        lis = []
        temp = ""
        for i in range(len(s)):
            if s[i] == "~":
                lis.append(temp)
                temp = ""
            else :
                temp = temp + s[i]
        return lis