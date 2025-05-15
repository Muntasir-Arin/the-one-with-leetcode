class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        flag = groups[0]
        res = [words[0]]

        for i in range(1, len(words)):
            if groups[i]!=flag:
                res+= [words[i]]
                flag = groups[i]


        return res

