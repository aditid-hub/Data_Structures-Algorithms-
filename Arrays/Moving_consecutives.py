"""
Problem Number 485 - Maximum Consecutive Ones:
Given a binary array nums, return the maximum number of consecutive 1's in the array.

"""
def findMaxConsecutiveOnes(nums):
    max_count = 0
    current_count = 0

    for i in range(0, len(nums)):
        if nums[i] == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count

nums = [1,1,0,1,1,1]
print(findMaxConsecutiveOnes(nums))

"""
    Index	Value	current_count	max_count	Action
    0	1	1	1	Start streak
    1	1	2	2	Extend streak
    2	0	0	2	Reset streak
    3	1	1	2	New streak
    4	1	2	2	Extend streak
    5	1	3	3	Extend & update max

"""