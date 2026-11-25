class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
    
        for word in strs:
            # Sort the word and use it as a key
            key = tuple(sorted(word))
            anagram_map[key].append(word)
        
        # Return the grouped anagrams as a list of lists
        return list(anagram_map.values())