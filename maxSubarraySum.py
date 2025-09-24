def maxSubarraySum(nums):
    subarray = nums[0]
    curSum = 0
    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        subarray = max(subarray, curSum)
    return subarray
