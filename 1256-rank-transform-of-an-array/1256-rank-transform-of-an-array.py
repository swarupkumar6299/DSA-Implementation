class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {} #Duplicate to store rank by mapping
        unique_number = sorted(list(set(arr))) #remove duplicate and sort elements
        #Assign rank to sorted unique elements
        for index in range(len(unique_number)):
            rank[unique_number[index]] = index + 1 
        #Replace each element in the original array with its rank
        for index in range(len(arr)):
            arr[index] = rank[arr[index]]
        return arr 

        