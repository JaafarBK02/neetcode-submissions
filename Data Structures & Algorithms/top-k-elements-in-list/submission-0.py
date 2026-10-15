class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        result = []

        for num in nums:
            count[num] = count.get(num,0) + 1
        
        
        boxes = [[] for _ in range(len(nums)+ 1)]
        
        for keys, value  in count.items():
            boxes[value].append(keys)
        
       
        for i in range (len(boxes)-1, -1, -1):
            for num in boxes[i]:
                result.append(num)
                if len(result) == k:
                    return result 

          




