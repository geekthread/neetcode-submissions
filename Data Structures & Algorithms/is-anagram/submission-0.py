class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store1 = list(s)
        store2 = list(t)
        isAnagram = False
        if len(s) == len(t):
            s1 ={}
            s2 = {}
            for n in store1:
                if n in s1:
                    count1= s1[n]
                    s1[n]= count1+1
                else:
                    s1[n] = 1
            
            for k in store2:
                if k in s2:
                    count2= s2[k]
                    s2[k]= count2+1
                else:
                    s2[k] = 1

            isAnagram = s1 == s2
            return isAnagram
            
        else:
            return False 