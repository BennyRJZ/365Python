class Solution(object):
    def removeElement(self, nums, val):
        
        count = 0
        for x in nums[:]:
            if x == val:
                nums.remove(val)
            
        # print(count)
        # while(count>=0):
        #     nums.remove(val)
        #     count = count - 1
                
        print(nums)