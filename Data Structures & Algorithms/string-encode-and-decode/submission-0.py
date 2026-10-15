class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string= ""
        for word in strs:
            encoded_string= encoded_string + str(len(word)) + "#" + word
        return encoded_string 



    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        while i < len(s):
            j = s.find("#", i)        
            length = int(s[i:j])      
            word = s[j + 1 : length + j + 1]  
            decoded_list.append(word)
            i =  length + j + 1
        return decoded_list




