class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums)+1)]
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i], 0) + 1
            
        for key, val in d.items():
            bucket[val].append(key)

        final = []
        for i in range(len(bucket) - 1, 0, -1):
            for j in bucket[i]:
                final.append(j)
                if len(final) == k:
                    return final

