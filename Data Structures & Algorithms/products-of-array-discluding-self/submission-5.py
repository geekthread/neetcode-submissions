class Solution:
     def productExceptSelf(self, nums: List[int]) -> List[int]:
        product ={}
        idx = len(nums)
        for i in range(len(nums)):  # Time Comple
            for j in range(len(nums)):
                if i!=j:
                    if i not in product:
                         product[i]= nums[j]
                    else:
                        product[i] = product[i] * nums[j]
        result = []
        print(product)
        for i in range(len(nums)):
            result.append(product[i])
        return result        
                    
                    


            
    


        