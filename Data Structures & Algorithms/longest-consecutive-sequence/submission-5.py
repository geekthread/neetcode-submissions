class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # Created to avoid duplucates , O(n) 
        longestStreak = 0
        for n in numSet:
            if n-1 not in numSet: #  it means that n is the start of a sequence
                length = 1
                while n + length in numSet: # O(k) where k is the length of the longest sequence
                    length += 1
                longestStreak = max(longestStreak, length) 

        return  longestStreak