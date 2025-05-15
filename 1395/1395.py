#inspired by https://leetcode.com/u/toho42/
class Solution:
    def numTeams(self, rating: List[int]) -> int:

        dp, count = [[0,0] for _ in range(len(rating))], 0

        for i in range(1, len(rating)):
            greaterThans, lessThans = 0,0

            for j in range(i):
                if rating[i] > rating[j]:
                    greaterThans += 1
                elif rating[i] < rating[j]:
                    lessThans += 1

            dp[i] = [greaterThans, lessThans]

            for j in range(i):
                if rating[i] > rating[j]:
                    count += dp[j][0]
                elif rating[i] < rating[j]:
                    count += dp[j][1]
        print(dp)
        return count
