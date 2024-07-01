class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        # Stack to maintain the elements for which we are looking for the next greater element
        stack = []

        # Traverse nums2 from right to left
        for num in reversed(nums2):
            # While the stack is not empty and the top of the stack is less than or equal to num
            while stack and stack[-1] <= num:
                stack.pop()
            # If stack is not empty, the top of the stack is the next greater element
            # Otherwise, there is no greater element, so store -1
            next_greater[num] = stack[-1] if stack else -1
            # Push the current element onto the stack
            stack.append(num)

        # Generate the result for nums1 based on the next_greater dictionary
        result = [next_greater[num] for num in nums1]

        return result
            
            
        
        