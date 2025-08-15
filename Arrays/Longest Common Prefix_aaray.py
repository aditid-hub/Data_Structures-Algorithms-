"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:  # more explicit
          return ""

        commonstring = strs[0]

        for s in strs[1:]:
            while not s.startswith(commonstring):
              commonstring = commonstring[:-1]
           
        return commonstring
