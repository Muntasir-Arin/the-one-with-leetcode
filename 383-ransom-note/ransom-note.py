class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = defaultdict(int)
        for s in magazine:
            hashmap[s] += 1
        for c in ransomNote:
            hashmap[c] -= 1
            if hashmap[c] < 0:
                return False
        return True