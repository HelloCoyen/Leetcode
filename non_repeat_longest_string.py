# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 22:25:51 2019

@author: Administrator
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s:
            lenght = 1
            strlist = list(s)
            laststring = strlist[0]
            print("last string:",laststring)
#            scan = 0
            for i in range(len(s)-1):
                nextc = strlist[i+1]
                print("next char:" ,nextc)
                newstring = laststring + nextc
                if newstring.count(nextc) == 1:
                    laststring = newstring
                    lenght = max(lenght, len(laststring))
                    print('last string:',laststring)
                elif newstring[0] == nextc:
                    laststring = newstring[1:]
                    lenght = max(lenght, len(laststring))
                    print('last string:',laststring)
                else:
                    laststring = newstring[newstring.index(nextc)+1:]
                    lenght = max(lenght, len(laststring))
                    print('last string:',laststring)
        else:
            lenght = 0
        return lenght

Solution().lengthOfLongestSubstring("dvfd")

