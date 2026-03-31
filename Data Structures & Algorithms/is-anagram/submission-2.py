class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        e = {}
        for i in s:
            d[i] = 1 + d.get(i, 0)
        for j in t:
            e[j] = 1 + e.get(j, 0)
        if len(s) != len(t):
            return False
        try:
            for k in d:
                if d[k] != e[k]:
                    return False
        except KeyError:
            return False
        return True