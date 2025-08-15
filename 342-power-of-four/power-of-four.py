import math
class Solution(object):
    def isPowerOfFour(self, n):
        if n <= 0:
            return False
        result = math.log(n, 4)
        return result.is_integer()
        