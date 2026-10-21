class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""


        for c in s:
            if c.isdigit() or c.isalpha(): 
                string += c.lower()


        i = 0
        j = len(string)-1

        while i<=j:
            if string[i] != string[j]:
                return False
            i = i + 1
            j = j - 1
        
        return True

                


        


