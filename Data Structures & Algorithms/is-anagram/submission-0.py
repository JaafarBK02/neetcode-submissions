class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}    
        for c in s:
            count[c] = count.get(c,0) +1


        count2 = {}
        for c in t:
            count2[c] = count2.get(c,0) +1

        return count == count2

        


        



    
        


        