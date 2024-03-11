class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        ans = list()
        for i in range(n):
            for j in range(n):
                if j != i:
                    tmp =  words[i] + words[j]
                    if tmp == tmp[::-1]:
                        ans.append([i, j])
        return ans
