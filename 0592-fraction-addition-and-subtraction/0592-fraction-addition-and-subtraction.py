import math

class Solution:
    def fractionAddition(self, expression: str) -> str:
        num = 0
        den = 1
        i = 0
        n = len(expression)

        while i < n:
            currNum = 0
            currDeno = 0
            isNeg = (expression[i] == '-')
            if expression[i] == '+' or expression[i] == '-':
                i += 1

            # Parse the numerator
            while i < n and expression[i].isdigit():
                currNum = (currNum * 10) + (ord(expression[i]) - ord('0'))
                i += 1

            if isNeg:
                currNum *= -1

            i += 1  # Skip the '/'
            
            # Parse the denominator
            while i < n and expression[i].isdigit():
                currDeno = (currDeno * 10) + (ord(expression[i]) - ord('0'))
                i += 1

            # Update the numerator and denominator
            num = num * currDeno + currNum * den
            den = den * currDeno

        # Compute GCD to simplify the fraction
        gcd = math.gcd(abs(num), den)
        num //= gcd
        den //= gcd

        return f"{num}/{den}"
