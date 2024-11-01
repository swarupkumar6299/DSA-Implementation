class Solution:

    #We have two parts in this recursive solution
    def sortArray(self, nums: List[int]) -> List[int]:

        #Part 1 --> MERGE
        #We use THREE POINTERs ijk 
        #and THREE while loops (for left out items in left or right arrays)
        def merge(arr,L, M, R):
            left = arr[L: M+1]
            right = arr[M+1: R+1]

            i = L #pointer for main array
            j = 0 #pointer for left part of array
            k = 0 #pointer for right part of array

            #Comparing and merging (sorting happens)
            while j < len(left) and k <len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1

            # Copy the remaining elements of the left half, if any
            #The reason we use nums here is, we are just attaching left out items.
            #Also remember only one of these TWO situations can happen.
            while j < len(left):
                nums[i] = left[j]
                
                j += 1
                i += 1

            # Copy the remaining elements of the left half, if any
            while k < len(right):
                nums[i] = right[k]
                
                k += 1
                i += 1


        #Part 2 --> MERGESORT
        #Firstly, DIVIDE and call mergesort for parts. Then MERGE(arr, l, m, r). 
        #BASE CASE is when size of array = 1 meaning left_pointer = right_pointer. 
        def mergeSort(arr, l , r):
            if l == r:
                return arr
            m = (l+r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)
            return arr

        return mergeSort(nums, 0, len(nums) - 1)

        


        