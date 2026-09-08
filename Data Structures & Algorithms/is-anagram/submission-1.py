class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapS ={}
        mapT ={}

        for i in range(len(s)):
            mapS[s[i]] = 1 + mapS.get(s[i],0)
            mapT[t[i]] = 1 + mapT.get(t[i],0)
        
        print(mapS)
        print(mapT)

        for ch in s:
            if mapS[ch] != mapT.get(ch,0):
                return False
        return True
        


    





        