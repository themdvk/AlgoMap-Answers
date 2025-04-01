class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        common = min(len(word1), len(word2))
        for i in range(common):
            ans = ans + word1[i:i+1]
            ans = ans + word2[i:i+1]
        if len(word1)>len(word2):
            ans = ans + word1[common:]

        if len(word2)>len(word1):
            ans = ans + word2[common:]

        return ans
