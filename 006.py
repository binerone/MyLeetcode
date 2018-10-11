class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) > 0 and numRows != 0:
            start = numRows
            mid = numRows - 2 if numRows-2>0 else 0
            ln = len(s)
            n = ln // (start+mid) + 1
            out  = ''
            f = 0
            for line in range(numRows):
                for i in range(n):
                    if f < ln:
                        try:
                            base = i*(start+mid)
                            if line == 0 or line == (numRows-1):
                                out += s[line+base]
                            else:
                                out += s[line+base]
                                out += s[line+base+(numRows-line-1)*2]
                                # 这里一开始忘记-1，出错
                        except Exception as e:
                            pass
                    else:
                        break
            return out
        else:
            return ''


if __name__ == '__main__':
    ss = Solution()
    s = "PAYPALISHIRING"
    numRows = 3
    print(ss.convert(s, numRows))