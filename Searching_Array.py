# The Linear Search implementation 
#Time complexity: O(n)
#Space Complexity: C
def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return-1
# Driver Code
arr  = [20,30,40,50,60]
x = 60
#function call
result = linearSearch(arr,x)
print(result)