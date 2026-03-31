class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # d = {}
        # e = {}
        # for i in s:
        #     d[i] = 1 + d.get(i, 0)
        # for j in t:
        #     e[j] = 1 + e.get(j, 0)
        # if len(s) != len(t):
        #     return False
        # try:
        #     for k in d:
        #         if d[k] != e[k]:
        #             return False
        # except KeyError:
        #     return False
        # return True
        h_set = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            h_set[s[i]] = h_set.get(s[i], 0) + 1
            h_set[t[i]] = h_set.get(t[i], 0) - 1

        return all(v == 0 for v in h_set.values())