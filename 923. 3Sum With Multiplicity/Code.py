class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        do=[0]*300
        res=0
        for i in range(len(A)):
            res+=do[target-A[i]] if target-A[i]>=0 else 0
            res%=(10**9+7)
            for j in range(i):
                do[A[i]+A[j]]+=1
                
        return res % (10**9+17)
                
     
                
      
    