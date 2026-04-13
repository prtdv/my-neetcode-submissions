class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        max_rows=len(matrix)
        row=0
        
        while row<max_rows and target>matrix[row][-1]: #order matters
                row+=1

        if row>=max_rows:
            return False
        

        l=0
        r=len(matrix[row])-1
        
        while l<=r:
            m=int((l+r)/2)
            if target==matrix[row][m]:
                return True
            elif target<matrix[row][m]:
                r=m-1
            else:
                l=m+1

        return False
        

        

            
        
