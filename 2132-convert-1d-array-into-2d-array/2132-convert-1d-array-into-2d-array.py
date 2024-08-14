class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # step1:- check the no. of the element in the original; matches m*n
        # If not, return an empty list
        if len(original) != m*n:
            return[]
        #step: initalize an empty list to store the 2D array
        result = []
        #steps fill the 2D array row by row
        for i in range(m):
        #slice the original array to get the current row 
            row = original [i*n:(i+1)*n]
        #append the row to the result list
            result.append(row)
        #step4 Return the constructed 2D 
        return result

        