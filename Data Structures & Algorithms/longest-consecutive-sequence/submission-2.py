class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        seen = set()
        counter=1
        streaks = []
        for n in nums:  # O(n)
            if n not in seen:
                seen.add(n)
        
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