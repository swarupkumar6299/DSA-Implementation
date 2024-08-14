class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # step1:- Count the frequency of each element in nums
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1
        #step2: creat the 2d array minimal rows
        #initial a list to hold the rows of  the 2D array
        result=[]
        #step3:- distribute elements across row.
        while freq:
        #initalize a list to hold the rows of the 2D array
            row = []
        #itrate over the unique element avilable in frequency.
            for key in list (freq.keys()):
        #add the element to the current row
                row.append(key)
        #decrease the frequency of the element
                freq[key]-=1
        #if the frequncy of an element become the zero, remove it from the frequency 
                if freq[key]==0:
                    del freq[key]
        #Append the construct row to the result
            result.append(row)
        return result
     
         
        