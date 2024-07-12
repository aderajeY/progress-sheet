class Solution:
    def cyclicSort(self, newTenantPrevHome, newTenant, nums):
        newHome = newTenant - 1
        if newHome >= len(nums):
            nums[newTenantPrevHome] = 0
            return
        elif nums[newHome] == newTenant:        
            if newTenantPrevHome != newHome:
                nums[newTenantPrevHome] = 0
            return

        nums[newTenantPrevHome] = 0
        if nums[newHome] != 0:
            self.cyclicSort(newHome, nums[newHome], nums)
        nums[newHome] = newTenant
        return

    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i, num in enumerate(nums):
            self.cyclicSort(i, num, nums)
        
        for i, num in enumerate(nums):
            if num == 0:
                return i +1
        return len(nums) + 1