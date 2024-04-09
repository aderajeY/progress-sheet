class Solution(object):
    def intersect(self, nums1, nums2):
        
        sortedArr1 = sorted(nums1)
        sortedArr2 = sorted(nums2)
       
        i = 0
        j = 0
        # Create a output list to store the output...
        output = []
        while i < len(sortedArr1) and j < len(sortedArr2):
            # If sortedArr1[i] is less than sortedArr2[j]...
            # Leave the smaller element and go to next(greater) element in nums1...
            if sortedArr1[i] < sortedArr2[j]:
                i += 1
            # If sortedArr1[i] is greater than sortedArr2[j]...
            # Go to next(greater) element in nums2 array...
            elif sortedArr2[j] < sortedArr1[i]:
                j += 1
            # If both the elements intersected...
            # Add this element to output & increment both i and j.
            else:
                output.append(sortedArr1[i])
                i += 1
                j += 1
        return output 