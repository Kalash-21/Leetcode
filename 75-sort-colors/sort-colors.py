class Solution:
    def quick_sort(self, nums, low=0, high=None):
        # First call — set high to the last index of the array
        if high is None:
            high = len(nums) - 1
        
        # Base case: a section with 0 or 1 element is already sorted
        if low < high:
            # Partition places the pivot in its final position
            # Returns the index where the pivot landed
            pivot_index = self.partition(nums, low, high)
            
            # Recursively sort the left side (everything smaller than pivot)
            self.quick_sort(nums, low, pivot_index - 1)
            # Recursively sort the right side (everything bigger than pivot)
            self.quick_sort(nums, pivot_index + 1, high)
        
        return nums
    
    def partition(self, nums, low, high):
        # Pick the last element as the boss
        pivot = nums[high]
        # Boundary marker — points at the last slot of the "small zone"
        # Starts at -1 because the small zone is empty at the start
        i = low - 1
        
        # Scout walks through every element except the pivot itself
        for j in range(low, high):
            # Found a small one — expand the zone and park it there
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        
        # Drop the pivot right after the small zone ends
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        # Return where the pivot landed — its final correct position
        return i + 1
    
    def sortColors(self, nums):
        # Python passes self automatically when we use the dot
        # So we only
        self.quick_sort(nums)