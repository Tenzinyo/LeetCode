class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # create a hashmap
        hashmap = {}
        # loop over the array of num
        for i in range(len(nums)):
            # check if value i has been added to the hashmap and if so then check if the diff of duplicate <=k
            if nums[i] in hashmap and i - hashmap[nums[i]] <= k:
                # if so, return True
                return True
                # add the duplicate to the hashmap
            hashmap[nums[i]] = i
        return False

        # while (r<len(nums)):
        #     if nums[l]==nums[r]:
        #         diff = r-l
        #         if diff<=k:
        #             return True
        #     else:
        #         l=r
        #     r+=1
        # return False

        # subtract their indices
        # if the diff is less than or  equal to k value
        # return true
