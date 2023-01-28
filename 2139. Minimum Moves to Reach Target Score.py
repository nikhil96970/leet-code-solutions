class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        m=0
        while target>1 and maxDoubles>0:
            if target%2!=0:
                target-=1
                
            elif maxDoubles>0:
                target//=2
                maxDoubles-=1
            m+=1
        return m+target-1

  
                
                
