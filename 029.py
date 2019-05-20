class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
       
        # this is necessary; otherwise phase 1 never terminates
        if dividend == 0: return 0

        # initialize
        i, result, p, q = map(abs, (0, 0, dividend, divisor))
        print(i, result, p, q)
        # phase 1
        while q << i <= p: 
            i += 1
            print(i, p, q)

        # phase 2
        for j in reversed(range(i)):
            if q << j <= p: p, result = p - (q << j), result + (1 << j)

        # stupid leetcode restrictions
        if (dividend > 0) != (divisor > 0) or result < -1 << 31: result = -result
        return min(result, (1 << 31) - 1)

if __name__ == '__main__':
    s = Solution()
    divisor = 3
    dividend = 10
    print(s.divide(dividend, divisor))