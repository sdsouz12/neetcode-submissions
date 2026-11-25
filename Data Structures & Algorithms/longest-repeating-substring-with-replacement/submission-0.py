class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count ={} # hashmap
        LengthOfLongestSubstring =0
         
        # windowlENGTH - MAXfreq - if it goes up only then i will recalc result
        for right in range(len(s)):
            count[s[right]] = 1+ count.get(s[right],0)
            
            windowLength = right - left + 1
            maxf = max(count.values())
            if windowLength - maxf > k: # invalid window
                count[s[left]] -=1
                left +=1

            LengthOfLongestSubstring = max (LengthOfLongestSubstring, right - left + 1)
        return LengthOfLongestSubstring


            
