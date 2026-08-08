class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #First create a Hash map

        hm = {}

        # Go through the array
        for i, n in enumerate(nums):
        #then we find the number we need to get the target
            difference = target - n
            #if that difference in hm
            if difference in hm:
                #Just return the difference in hm and i
                return [hm[difference],  i]
            # Save the current number and its index for future numbers to find
            hm[n] = i