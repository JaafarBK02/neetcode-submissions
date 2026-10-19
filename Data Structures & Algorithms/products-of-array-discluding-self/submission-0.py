class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        running = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] = running
            running = nums[i] * running

        running = 1
        for i in range(len(nums)):
            output[i] = running * output[i]
            running = running * nums[i]
        
        return output



