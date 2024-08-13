class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #convert both input string to integer
        int_num1 = int(num1)
        int_num2 = int(num2)
        # Multiply the two integers
        product = int_num1 * int_num2
        #convert the product back to a string
        return str(product)        