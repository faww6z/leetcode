class Solution(object):
    def largestGoodInteger(self, num):
        for i in range(9, -1, -1):
            check = (str(i) * 3)
            if check in num:
                return check
        else: 
            return ""
        