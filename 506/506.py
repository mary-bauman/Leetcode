class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        newScore = [""]*len(score)
        place = sorted(score, reverse = True)
        for i,s in enumerate(score):
            newScore[i] = str(place.index(s)+1)
            if newScore[i] == "1": newScore[i] = "Gold Medal"
            if newScore[i] == "2": newScore[i] = "Silver Medal"
            if newScore[i] == "3": newScore[i] = "Bronze Medal"
        return newScore
