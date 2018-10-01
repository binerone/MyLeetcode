class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        o = 0
        a, b = abs(dividend), abs(divisor)
        t = 0
        if b == 1:
            o = a
        else:
            while not (t > a):
                t = t + b
                o += 1
            o = o - 1
        if dividend * divisor < 0:
            o = -o
        if not (o >= -(2 ** 31) and o <= (2 ** 31 - 1)):
            o = 2 ** 31 -1
        return o


if __name__ == '__main__':
    s = Solution()
    divisor = 3
    dividend = 10
    print(s.divide(dividend, divisor))