class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for string in strs:
            count = [0] * 26  # Changed: fixed-size list instead of dict

            for char in string:
                count[ord(char) - ord('a')] += 1  # Changed: count by index

            key = tuple(count)  # Changed: no sorting needed

            if key not in groups:
                groups[key] = []

            groups[key].append(string)  # Your original grouping logic

        return list(groups.values())