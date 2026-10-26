class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()

        for i in range(len(nums)):
            j = i + 1
            k = len(nums)-1

            while (j < k):
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    seen.add(tuple([nums[i], nums[j], nums[k]]))
                    j = j+1
                    k = k-1
                elif sum < 0:
                    j = j + 1
                elif sum > 0:
                    k = k-1

        return [list(t) for t in seen] 







        