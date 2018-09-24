class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        o = ''
        if len(strs) > 0:
            minlen = min([len(s) for s in strs])
            for i in range(0, minlen):
                tmp = strs[0][i]
                for s in strs:
                    if s[i] != tmp:
                        return o
                o = o + tmp
        return o


if __name__ == '__main__':
    s = Solution()
    strs = ["dog","racecar","car"]
    print(s.longestCommonPrefix(strs))