class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        m = str(x)
        n = ''
        for mm in m:
            n = mm + n
        if n == m:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    x = 12321
    print(s.isPalindrome(x))