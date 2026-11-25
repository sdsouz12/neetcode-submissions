class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       if len(s) != len(t):
        return False
       countCharS,countCharT = {}, {}

       for i in range(len(s)):
        countCharS[s[i]] = 1 +  countCharS.get(s[i],0)
        countCharT[t[i]] = 1 +  countCharT.get(t[i],0) 

       for char in countCharS:
        if countCharS[char] != countCharT.get(char,0):
            return False
    
       return True






