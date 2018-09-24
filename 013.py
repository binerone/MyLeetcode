class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        str = list(s)
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        r = 0
        for x in range(len(str) - 1):
            if dic[str[x]] < dic[str[x + 1]]:
                r -= dic[str[x]]
            else:
                r += dic[str[x]]
        r += dic[str[len(str) - 1]]
        return r