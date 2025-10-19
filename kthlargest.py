def kthlargest(nums,k):
    n = len(nums)
    # [3,2,1 || 5,6,4] -> nlog n 
    # 
    #          p
    # |3|2|1|| 
    # if 
    def quick(l,r):
        p, pivot = l, nums[r]
        for i in range(l,r):
            if nums[p]<=pivot:
                nums[i],nums[p] = nums[p],nums[i]
                p+=1
        nums[p],nums[r] = nums[r],nums[p]
        # to compare our p to k
        if p>k: return quick(l,p-1)
        elif p<k: return quick(p+1,r)
        else: return nums[p]
    return quick(0,n-1)
        