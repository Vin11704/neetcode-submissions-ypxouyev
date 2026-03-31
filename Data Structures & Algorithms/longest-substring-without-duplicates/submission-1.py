class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        ans = 0
        cset = defaultdict(int)
        for r in range(len(s)):
            while s[r] in cset.keys():
                cset.pop(s[l])
                l += 1
            cset[s[r]] = 1
            ans = max(ans, r-l+1)

        return ans
            