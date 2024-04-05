class Solution(object):
    def lengthOfLongestSubstring(self, s):
        count = 0
        substr = ""
        for char in s:
            if char not in substr:
                substr += char
                count = max(count,len(substr))
            else :
                index = substr.index(char)
                substr = substr[index + 1:] + char
        return count
                
