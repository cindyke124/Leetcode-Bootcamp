class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        dp = [0] + [float("inf")] * time
        for i in range(1, time + 1):
            for c in clips:
                a = c[0]
                b = c[1]
                if a < i <= b:
                    dp[i] = min(dp[i], dp[a]+1)
        
        if dp[time] == float("inf"):
            return -1
        return dp[time]
