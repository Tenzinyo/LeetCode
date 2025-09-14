class Solution:
    from collections import defaultdict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # array of strings
        anagram = defaultdict(list)
        result = []
        # anagram = same letters in different sequence
        # group the anagrams together
        # breakdown the letters in a single string
        # base case= empty string
        # base case = one string only
        # compare the letters to other strings is they are present or not
        for s in strs:
            # use tuple since tuple is not mutable
            letters = tuple(sorted(s))
            anagram[letters].append(s)
        for v in anagram.values():
            result.append(v)
        return result
