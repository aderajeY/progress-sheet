class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # get the frequent dictionary
        # sort out the k highest value keys
        # use quick sort to find the kth largest element [DO NOT NEED TO SORT THEM ALL]
        # return the left hand side of the Kth largest pivot
        freq  = collections.Counter(nums)
        key = list(freq.keys()) # the number
        val = list(freq.values()) # the frequent

        def partition(nums, left, right,key):
            p = right
            right -=1
            while left <= right:
                while left<=right and nums[left]>=nums[p]:
                    left +=1
                while left <= right and nums[right]<=nums[p]:
                    right -=1
                if left <= right:
                    nums[left],nums[right] = nums[right],nums[left]
                    key[left],key[right] = key[right],key[left]
            
            nums[left], nums[p] = nums[p],nums[left]
            key[left], key[p] = key[p],key[left]
            return left


        def quickSort(nums,left,right):
            if not nums or len(nums)<=1: return nums
            if left >= right: return nums
            p = partition(nums,left,right,key)
            if p == k-1:
                return key[:k]
            elif p > k-1:
                return quickSort(nums, left, p-1)
            else: return quickSort(nums, p+1, right)

        quickSort(val, 0, len(val)-1)
        return key[:k]