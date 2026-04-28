class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorteddict={}
       
        for s in strs:
            sort = "".join(sorted(s))
            if sort not in sorteddict:
                sorteddict[sort]=[s]
            else:
                l = sorteddict[sort]
                l.append(s)
                sorteddict[sort]=l
        print(sorteddict)
        
        return list(sorteddict.values())