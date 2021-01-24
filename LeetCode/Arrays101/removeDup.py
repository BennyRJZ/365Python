class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # SHOR SOLUTION nums = (list(dict.fromkeys(nums)))
        

        if len(nums) < 2: return len(nums)
   
        i = 0  
        for j in range(1, len(nums)):
            if nums[j] == nums[i]: 
                continue 
            if nums[j] != nums[i]: 
                i += 1
                nums[i] = nums[j] 
        return i + 1