class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pointer = 0
        while pointer < n:
            cur = nums[pointer]
            if cur - 1 != pointer and cur != nums[cur -1]:
                nums[pointer], nums[cur - 1] = nums[cur - 1], nums[pointer]
            else:
                pointer += 1
        res = []
        for j in range(n):
            if nums[j] != j + 1:
                res.append(j + 1)
                
        return res