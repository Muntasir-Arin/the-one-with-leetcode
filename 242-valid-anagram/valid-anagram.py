class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1 = defaultdict(int)
        for i in s:
            dict1[i] += 1
        for j in t:
            dict1[j] -= 1
            if dict1[j]<0:
                return False
        return True

        