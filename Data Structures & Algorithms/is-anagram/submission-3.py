class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1

        for c in t:
            if c not in d:
                return False
            else:
                if d[c] == 0:
                    return False
                d[c] -= 1
        return sum(d.values()) == 0