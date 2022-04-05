class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0 , len(height) -1
        area = 0
        for i in range(0, len(height) -1):
            while left<right:
                temp=min(height[left],height[right])
                area=max(area,temp*(right-left))
                if(height[left]<height[right]):
                    left+=1
                else:
                    right-=1
        return area