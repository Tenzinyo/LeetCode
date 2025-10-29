def number_of_ways(lot_sizes: List[int], target: int) -> int:
    """
    Returns the number of different ways to buy exactly `target` barrels of oil 
    using any combination of the available lot sizes. 
    Each supplier can be used any number of times (including zero).
    The order of selection does not matter.
    """
    lot_sizes.sort()
    dp = [0] * (target+1)
    for i in range(1,target+1):
        minn = float('inf')
        for t in target:
            diff = i - t
            if diff<0:
                break
            minn = min(minn,dp[diff]+1)
        dp[i] = minn
    if dp[target] < float('inf'):
        return dp[target]
    else:
        return -1
    