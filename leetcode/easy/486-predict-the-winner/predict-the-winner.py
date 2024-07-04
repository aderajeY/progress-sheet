class Solution:
    def calculate_scores(self, nums, left, right, player):
        if left == right:
            return nums[left] if player == 1 else -nums[left]
        if player == 1:
            return max(nums[left] + self.calculate_scores(nums, left+1, right, 2),
             nums[right] + self.calculate_scores(nums, left, right-1, 2))
        else:
            return min(self.calculate_scores(nums, left+1, right, 1) - nums[left],
             self.calculate_scores(nums, left, right-1, 1) - nums[right])

    def predictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        return self.calculate_scores(nums, 0, len(nums)-1, 1) >= 0