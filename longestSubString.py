def longestSubString(s):
    # abcabcbb
    # a -> 1
    # ab -> 1
    # abc -> 1
    # abca -> 1
    # abcab -> 1
    # abcabc -> 2
    # abcabcbb -> 1
    
    # s = abcabcbb -> 
    # s[r] -> 
    # s[l] -> bcabcbb
    # s[r] -> a
    # res is correctly handled through returning the max  
    # set () -> two indexes, l,r -> for the set, i wanna see if the v at index r in l, remove dup , res 
    # get out of the loop,then we can add that v in r  
    
    res = 0
    char = set()
    l = 0
    
    for r in range(len(s)):
        while (s[r] in char):
            char.remove(s[l])
            l+=1
        char.add(s[r])
        res = max(res,r-l+1)
    return res
    