class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr = [[0] * n for _ in range(n)]
        r1,r2,c1,c2,num=0,n-1,0,n-1,1
        while r1<=r2 and c1<=c2:
            for i in range(c1,c2+1):
                arr[r1][i]=num
                num+=1
            
            for i in range(r1+1,r2+1):
                arr[i][c2]=num
                num+=1
            
            if r1<r2 and c1<c2:
                for i in range(c2-1,c1,-1):
                    arr[r2][i]=num
                    num+=1
                
                for i in range(r2,r1,-1):
                    arr[i][c1]=num
                    num+=1
            r1+=1
            r2-=1
            c1+=1
            c2-=1
        return arr
