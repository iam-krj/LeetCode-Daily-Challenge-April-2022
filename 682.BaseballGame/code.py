class Solution:
    def calPoints(self, ops: List[str]) -> int:
        result=[]
        for i in ops:
            if i =="+":
                result.append(result[-1]+result[-2])
            elif i=="D":
                result.append(2*result[-1])
            elif i=="C":
                result.pop()
            else:
                result.append(int(i))
        print(result)
        return sum(result)
            
        
