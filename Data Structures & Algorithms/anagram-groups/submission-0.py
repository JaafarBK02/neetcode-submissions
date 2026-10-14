class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            count = {}

            for char in string:
                count[char] = count.get(char,0) + 1
            key= tuple(sorted(count.items()))

            if key not in groups:
                words = []
                words.append(string)
                groups[key] = words
            else: 
                groups[key].append(string)
        
        return list(groups.values())
                



            
        

            

        