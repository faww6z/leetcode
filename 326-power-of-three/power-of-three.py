class Solution(object):
    def isPowerOfThree(self, n):
        #return True if n== 3^something
        if n<= 0:
            return False
        while n % 3 == 0:
            n//=3

        return n == 1
        