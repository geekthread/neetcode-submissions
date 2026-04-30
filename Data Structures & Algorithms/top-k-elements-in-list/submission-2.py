class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        output = []
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else: 
                freq[num]=freq[num] +1
        
        sorted_dict = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        
        for key in list(sorted_dict.keys())[:k]:
            output.append(key)
        return output