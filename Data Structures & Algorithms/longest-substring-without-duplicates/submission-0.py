class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setchar= set()
        result =0

        left=0

        for right in range(len(s)):
            while(s[right] in setchar):
                setchar.remove(s[left])
                left+=1
            setchar.add(s[right])
            result = max(result, len(setchar))
        
        return result
