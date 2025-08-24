"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Example:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""
brute force method :
    def moveZeroes(nums):
        
        i=0
        for j in range (0,len(nums)):
            if nums[j]!= 0:
                nums[i] = nums[j]
                i+=1

        while i <len(nums):
            nums[i]=0
            i += 1
     

	nums = [0, 1, 0, 3, 12]
	movezeroes(nums)  # Call the function directly
	print(nums)  # This will output: [1, 3, 12, 0, 0]
