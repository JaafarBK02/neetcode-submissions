class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        counts= []
        s = set(nums)

        for element in s:
            count = 0
            if (element - 1) not in s:
                start = element

                while start in s:
                    count = count + 1
                    start = start + 1
                
                counts.append(count)
            

        return max(counts)




        