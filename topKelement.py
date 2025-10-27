import heapq
from collections import Counter
def topKFrequent(self, nums, k):
    count = {}
    freq = [[] for i in range(len(nums)+1)]
    
    # loop over the nums
    for i in nums:
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

def topk(self,nums,k):
    count = Counter(nums)
    heap = []
    for k,v in count.items():
        if len(heap) < k:
            heapq.heappush(heap,(v,k))
        else:
            heapq.heappushpop(heap,(v,k))
    return [h[1] for h in heap]
            
    