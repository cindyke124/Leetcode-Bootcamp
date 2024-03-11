class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_len = 0
        for left in range(len(s)):
            for right in range(left,len(s)):
                count = {}
                for i in range(left, right+1):
                    if s[i] not in count:
                        count[s[i]] = 0
                    count[s[i]] += 1
                max_count = max(count.values())
                if  k >= right - left + 1 - max_count:
                    max_len = max(max_len, right-left+1)
        return max_len
