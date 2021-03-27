class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        pivot = 0
        counter = 0
        for i in range(0,len(heights)-1):
            if heights[i]> heights[i+1]:
                pivot = heights[i+1]
                heights[i+1] = heights[i]
                heights[i] = pivot
                i = 0
                counter = counter + 1
                print(counter)
        print()
        
        return counter
##pendientes
            