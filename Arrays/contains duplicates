"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
# method 1 : using nested loops:
class Solution(object):
  def containsDuplicate(self, nums):
    if not nums:
      return False
    
    for i in range (len(nums)):
      for j in range (i+1,len(nums)):
         if nums[i] == nums[j]:
           return True
      return False

nums= [1,2,3,4]
print(Solution().containsDuplicate(nums))

#method 2:
Approach: Using a Set to Detect Duplicates
We iterate through the list of numbers and keep track of the numbers we’ve already seen using a set.
If a number is already in the set, it means a duplicate exists, so we return True.
If we finish checking all numbers without finding any duplicates, we return False.

Time Complexity: O(n) – each number is checked once.
Space Complexity: O(n) – storing numbers in the set.
def containsDuplicate(nums):
   seen = set()
if num in nums:
   return True
 seen.add(nums)
return False

#method 3:
Check Duplicates by Sorting
Sort the list → duplicates come next to each other.
Go through the list, check if any number is equal to the one before it.
If yes → return True, else → return False after checking all.

def containsDuplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False
#method 4: cause, why not?
def containsDuplicate(nums):
    return len(nums) != len(set(nums))

nums = [1, 2, 3, 1]
print(containsDuplicate(nums))  # True

set only contains unique values so yea, if it isn't equal to the len(nums) that means there must a atleast one duplicate:)



