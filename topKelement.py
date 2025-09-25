def topKFrequent(self, nums, k):
    count = {}
    freq = [[] for i in range(len(nums)+1)]
    
    # loop over the nums
    for i in n:
        count[i] = 1+ count.get(i,0)
    #  loop over the number and the counter
    for n,c in count.items():
        # append the number of times a counter has been frequently added
        freq[c].append(n)
    
    result = []
    for i in range(len(nums)-1,0,-1):
        for n in freq[i]:
            result.append(i)
            if len(result)==k:
                return result