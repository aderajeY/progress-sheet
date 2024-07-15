class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        d = defaultdict(list)

        for num in nums:
            elems = heappop(d[num-1]) + 1 if d[num-1] else 1
            heappush(d[num], elems)
        
        return all(elem >= 3 for arr in d.values() for elem in arr)
        