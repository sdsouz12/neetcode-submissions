class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {[act]:[act,cat], [p,o,t,s] : [pots, tops]}
        # array - [act, cat] ,[ pots, tops]

        res = defaultdict(list) # 'a,c,c' : ['cac','acc']
        for s in strs:
            count = [0] * 26 
            for c in s: 
                count[ord(c)- ord('a')] += 1
            print(count)
        
                

            res[tuple(count)].append(s)
            #print(res)
        return list(res.values())
            


       

        

        