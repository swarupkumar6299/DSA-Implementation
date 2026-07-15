class Solution:
    def isPrime(self, num: int) -> int:
        if num == 1:
            return False
        cnt = 0
        for i in range(2, num):
            if num % i == 0:
                cnt+=1
            if cnt > 1:
                return False
        return True

    def gcdOfOddEvenSums(self, n: int) -> int:
        gcd = 1
        primeNum = list()
        sumOdd, sumEven = 0, 0
        for i in range(1, n * 2 + 1):
            if self.isPrime(i):
                primeNum.append(i)
            if i % 2 == 0:
                sumEven+=i
            else:
                sumOdd+=i
            
        i = 0
        while i < len(primeNum):
            if sumOdd == 1 and sumEven == 1:
                break
            if sumEven % primeNum[i] == 0 and sumOdd % primeNum[i] == 0:
                gcd *= primeNum[i]
                sumOdd//=primeNum[i]
                sumEven//=primeNum[i]
                i = 0
                continue
            i+=1
        return gcd