class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        seen = set(nums)
        counter=1
        streaks = []
        
        
        sortedset = sorted(seen)  # O(nlogn)
        print(sortedset)

        for i in range(len(sortedset)-1):  # O(n)
            if sortedset[i]+1 == sortedset[i+1]:
               # print(i, sortedset[i], sortedset[i+1])
                counter+=1
            else:
               streaks.append(counter)
               counter=1
        streaks.append(counter)
        return max(streaks) if streaks else 0