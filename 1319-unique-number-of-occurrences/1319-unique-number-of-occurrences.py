from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        
        # Count the occurrences of each element
        for i in arr:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        # Get the list of occurrences
        list_hashmap = list(hashmap.values())
        
        # Check if all occurrences are unique by converting to a set
        return len(list_hashmap) == len(set(list_hashmap))
