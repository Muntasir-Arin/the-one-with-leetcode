class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        s2t = defaultdict(str)
        t2s = defaultdict(str)
        for i in range(n):
            if s[i] in s2t and s2t[s[i]] != t[i] or t[i] in t2s and t2s[t[i]] != s[i]:
                return False
            s2t[s[i]] = t[i]
            t2s[t[i]] = s[i]
        return True