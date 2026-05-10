class Solution:
   def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 4,3,4,7
       # res = [1]* len(nums) # Initialize the array with size equal to nums
        res=[1]* len(nums) 
        for i in range(len(nums)): #input => # 4,3,4,7
            if i==0:
                res[i]=1
            else:
                res[i] = res[i-1] * nums[i-1]

        #postfix=1 # to reduce space complexity we can use a variable to store the postfix value instead of creating a separate array for it.
        for i in range(len(nums) -1, -1, -1): # reverse loop from the end to the beginning
            if i==len(nums)-1:
                postfix=1
            else:
                postfix = postfix * nums[i+1]
                res[i] = res[i] * postfix
        
        return res



         
                    
                    


            
    


        