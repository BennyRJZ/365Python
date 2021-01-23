class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        mountain = False

        if len(arr)>=3:

            ### Checks if its a climb
            for i in range(0,len(arr)-1):
                if(arr[i+1]>arr[i]):
                    mountain = True
                else:
                    break ### 

            if mountain == True:
                for x in range(i,len(arr)-1):
                    if(arr[x+1]<arr[x]):
                        mountain = True
                    else:
                        mountain = False
                        break
                
                
        return mountain
            