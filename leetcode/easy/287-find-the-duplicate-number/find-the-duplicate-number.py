class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        pointer = 0
        while pointer < n:
            cur = nums[pointer]
            if cur - 1 != pointer and cur != nums[cur -1]:
                nums[pointer], nums[cur - 1] = nums[cur - 1], nums[pointer]
            else:
                pointer += 1
        for j in range(n):
            if nums[j] != j + 1:
                return nums[j]
                
