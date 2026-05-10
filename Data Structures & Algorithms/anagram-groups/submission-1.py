from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            code = [0]*26
            for char in string:
                code[ord(char) - ord('a')] += 1
            
            groups[tuple(code)].append(string)
        
        return [words for code, words in groups.items()]