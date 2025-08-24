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

Check if the current string starts with our commonstrings
If it DOESN'T start with it, make commonstrings shorter by removing the last character
Keep doing this until the string DOES start with commonstrings

"""
Longest Common Prefix – Dry Run Example

Input: ["flower", "flow", "flight"]

Step | Current prefix | Current s | s.startswith(prefix)? | Action | Result
---- | -------------- | --------- | -------------------- | ------ | ------
Init | "flower"       | —         | —                     | Set prefix to first string | "flower"
1    | "flower"       | "flow"    | False                 | Trim last char            | "flowe"
2    | "flowe"        | "flow"    | False                 | Trim last char            | "flow"
3    | "flow"         | "flow"    | True                  | Stop trimming             | "flow"
4    | "flow"         | "flight"  | False                 | Trim last char            | "flo"
5    | "flo"          | "flight"  | False                 | Trim last char            | "fl"
6    | "fl"           | "flight"  | True                  | Stop trimming             | "fl"
End  | "fl"           | —         | —                     | Return prefix             | "fl"

Final Answer: "fl"
"""
