class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        #Frequency array to store the count of remainder
        remainderFreq = [0] * k

        #step1: calculate the remainder for each element and store the frequency
        for num in arr:
            remainder = (num % k + k) % k # Ensure non- negative remainder
            remainderFreq[remainder] += 1

        #step2: check if the pairing condition holds
        for i in range(k // 2 + 1):
            if i == 0:
        #Remainder i must pair with remainder k-i
                if remainderFreq[i] % 2 != 0:
                    return False
            else:
        #Remainder i must pair with remainder k-i
                if remainderFreq[i] != remainderFreq[k - i]:
                    return False
        return True
        