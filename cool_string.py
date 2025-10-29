"""  
    Example:

aaabbb -> true
Explanation: Both a and b have same frequencies
aaabbbcccc -> true
Explanation: a and b occur 3 times but c occurs 4 times, we can remove 1 c to make this into a cool string
aaabbbccccdddd -> false
Explanation: a and b occur 3 times but c and d occur 4 times we'd have to remove 1 c and 1 d to make it cool string
aabbcccdddeeee -> false
Explanation: a and b occur 2 times, c and d occur 3 times, and e occurs 4 times. We'd have to remove 1 c and 2 e's to make it cool string

    count = every repeating letter
    set -> freq
    aaabbb
    {"a":3,"b":3 }
    get the values -> {3,3} -> 3 -> check if len of set == 1
    aaabbbcccc
    {"a":3,"b":3 ,"4"}
    {3,3,4} -> cool string
    -> temp -> {3,3,4} 
    -> subtract 1 from each index
        -> {3,3,4} 
        -> {3,4}
        loop through the freq set -> {2,4}
                                -> {3,3} -> set () check if the len  = 1
    
    aabbcccdddeeee
    {"a":2,"b":2 ,c:"3","d" = 3,"e":4}
    {2,2,3,3,4}
    {2,3,4}
    temp -> {1,3,4}
    temp -> {2,2,4}
    temp -> {2,3,3} ->set(temp) -> {2,3} len>1 so return false
     
    

"""

from collections import Counter
def cool_string(s):
    count = Counter(s)
    freq = list(count.values())
    if len(set(freq))==1:
        return True
    for i in range(len(freq)):
        temp = freq.copy()
        temp[i]-=1
        temp = [j for j in temp if j!=0] #remove 0 to make that character disappear
        if len(set(temp))==1:
            return True
    return False
cool_string("aaabbbcccc")
 