class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        k = len(heights) -1
        best = 0

        while i < k: 


            if heights[i] > heights[k]:
                area= min(heights[i], heights[k]) * ( k - i)
                if area > best:
                    best = area
                
                k = k-1
            elif heights[k] > heights[i]:
                area= min(heights[i], heights[k]) * ( k - i)
                if area > best:
                    best = area
                i = i+1

            
            elif heights[k] == heights[i]:
                area= min(heights[i], heights[k]) * ( k - i)
                if area > best:
                    best = area
                i = i+1
                k = k-1

        return best


        