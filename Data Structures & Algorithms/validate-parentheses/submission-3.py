class Solution:
    def isValid(self, s: str) -> bool:
        ls = []
        parmap = {"]":"[", ")":"(", "}":"{"}
        if s[0] not in ("[", "{", "("):
            return False
        for i in s:
            if i in ("[", "{", "("):
                ls.append(i)
            elif i in ("]", "}", ")"):
                if not ls or ls[-1] != parmap[i]:
                    return False
                ls.pop()

        return ls == []