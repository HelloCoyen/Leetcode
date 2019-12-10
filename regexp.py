# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 08:55:13 2019

@author: wuhaoyu
"""
class Solution:
    def isMatch(self, text, pattern):
        ''' 如果模字符串为空，取匹配字符的逻辑值的非'''
        if not pattern:
            return not text

        ''' 第一个字符的匹配结果'''
        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            ''' 如果模字符串长度大于2，且第二个模字符为*'''
            ''' 当模字符串当度大于2，且第二个模字符为星时：
            检验首字符是否匹配成功。 1 0 
            检验第三个字符开始的余模字符串是否匹配匹配字符串。 1 0
            检验第二个字符串开始的匹配字符串是否匹配模字符串。 1 0
            当第二个模字符为*号时，只有第二个字符串开始匹配字符串必须和模字符
            串匹配上，否则不匹配。
            如果能匹配上，那首字符必须匹配或者第三个字符开始的余模字符串匹配匹
            配字符串。
            '''
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            ''' 模字符串长度为1，或第二个模字符不为* '''
            ''' 当模字符串长度为1时，返回匹配字符的首字符匹配结果并上余字符串
            与""的匹配结果
                当第二模字符不为*，返回匹配字符的首字符匹配结果并上余字符串
            与余模字符串的匹配结果'''
            ''' '''
            return first_match and self.isMatch(text[1:], pattern[1:])

c = Solution().isMatch("aa",'a');c
c = Solution().isMatch("aa",'a*');c
c = Solution().isMatch("ab",'.*');c
c = Solution().isMatch("aab",'c*a*b');c
c = Solution().isMatch("mississippi",'mis*is*p*.');c
c = Solution().isMatch("aaa", "ab*a*c*a");c
c = Solution().isMatch("a","ab*a");c
c = Solution().isMatch("aaa","ab*a*c*a");c
c = Solution().isMatch("bbbba", ".*a*a");c
c = Solution().isMatch("aaaaaaaaaaaaaaaaaaa", ".*a*a");c
c = Solution().isMatch("", "");c
c = Solution().isMatch("", ".*a*a");c
c = Solution().isMatch("aaaaaaaaaaaaaaaaaaa", "");c

