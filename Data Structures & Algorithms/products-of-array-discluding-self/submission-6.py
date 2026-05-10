class Solution:
      def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 4,3,4,7
       # res = [1]* len(nums) # Initialize the array with size equal to nums
        prfix=[1]* len(nums) 
        for i in range(len(nums)): #input => # 4,3,4,7
            if i==0:
                prfix[i]=1
            else:
                prfix[i] = prfix[i-1] * nums[i-1]

        postfix=[1]* len(nums) 
        for i in range(len(nums) -1, -1, -1): # reverse loop from the end to the beginning
            if i==len(nums)-1:
                postfix[i]=1
            else:
               # print(postfix[i+1], nums[i+1])
                postfix[i] = postfix[i+1] * nums[i+1]
        
        #print(prfix)
        #print(postfix)
        # Now we have the prefix and postfix arrays, we can calculate the result by multiplying the corresponding elements from both arrays.
        res = [1] * len(nums) # Initialize the result array with size equal to nums
        for i in range(len(nums)):
            res[i] = prfix[i] * postfix[i] # Multiply the prefix and postfix values to get the final result for each index
        return res




        return res        
                    
                    


            
    


        