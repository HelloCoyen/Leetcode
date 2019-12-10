# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 08:55:13 2019

@author: wuhaoyu
"""
import pysnooper
​
class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        p = self._compile(p)
        # s,p至少一个不为空
        if p or s:
            # p为空
            if s and not p:
                return 0
            # s为空
            elif not s and p:
                if (set(p[::2]) == {"*"} or set(p[1::2]) == {"*"}) and p[-1] == "*":
                    return 1
                else:
                    return 0
            # 均不为空
            else:
                ls = list(s)
                ls.reverse()
                ts = ls.pop()
                iep = iter(enumerate(p))
                rpt = next(iep)
                rp = rpt[1]
                lp = ''
                while len(ls) != 0:
                    if rp == '.' or rp == ts:
                        ts = ls.pop()
                        lp = rp
                        try:
                            rpt = next(iep)
                            rp = rpt[1]
                        except:
                            return [0, 1][len(ls)==0]
                    elif rp == '*':
                        if lp == ls[-1] or lp == '.':
                            ts = ls.pop()
                            lp = rp
                            rpt = next(iep)
                            rp = rpt[1]
                        else:
                            lp = rp
                            rpt = next(iep)
                            rp = rpt[1]
                    else:
                        try:
                            nnpt = next(iep)
                            nnp = nnpt[1]
                            if nnp != '*':
                                return 0
                            else:
                                rp = next(iep)
                                lp = p[rp[0]-1]
                        except:
                            return 0
                print('跳出去了')
                trp = []
                while True:
                    try:
                        rpt = next(iep)
                        rp = rpt[1]
                        trp.append(rp)
                    except:
                        pn = ''.join(trp)
                        print('未匹配模子：',pn)
                        break
                if not pn:
                    return 1
                else:
                    lp = p[rpt[0]-len(rp)]
                    if lp != '*':
                        return self.isMatch('', pn)
                    else:
                        return self.isMatch(s[-1], pn)

    def _compile(self, p):
        p = p.replace("**","*")
        if "**" in p:
            return self._compile(self, p)
        else:
            return p

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

#ls = list(s)
#                ls.reverse()
#                iep = iter(enumerate(p))
#                lp = ''
#                npt = next(iep)
#                np = npt[1]
#                while len(ls) != 0:
#                    print("当前校验：",ls[-1],"\t上一个模子:",lp, "\t当前模子:",np)
#                    # npt可以正常迭代
#                    if np in [ls[-1], '.']:
#                        ls.pop()
#                        try:
#                            npt = next(iep)
#                            np = npt[1]
#                            lp = p[np[0]-1]
#                        except :
##                            print('模子已耗尽，末位检验')
##                            if np == '*':
##                                if lp == ls[-1] or lp == '.':
##                                    ls.pop()
##                                else:
##                                    return 0
##                            else:
##                                return 0
#                    elif np == '*':
#                        if lp == ls[-1] or lp == '.':
#                            ls.pop()
#                        else:
#                            try:
#                                npt = next(iep)
#                                np = npt[1]
#                                lp = p[np[0]-1]
#                            except :
##                                print('模子已耗尽，末位检验')
##                                if np == '*':
##                                    if lp == ls[-1] or lp == '.':
##                                        ls.pop()
##                                    else:
##                                        return 0
##                                else:
##                                    return 0
#                    else:
#                        try:
#                            nnpt = next(iep)
#                            nnp = nnpt[1]
#                            print("当前校验：",ls[-1],"\t上一个模子:",lp, "\t当前模子:",np,"\t下个一个模子：",nnp)
#                            if nnp != '*':
#                                return 0
#                        except:
#                            return 0
#                print('跳出去了')
#                rp = []
#                while True:
#                    try:
#                        lp = np
#                        npt = next(iep)
#                        np = npt[1]
#                        print("当前校验已完成,输出剩余模子\t当前模子:",np,"\t上一个模子:",p[npt[0]-1])
#                        rp.append(np)
#                    except:
#                        rp = ''.join(rp)
#                        print('未匹配模子：',rp)
#                        break
#
#                if not rp:
#                    return 1
#                else:
#                    lp = p[npt[0]-len(rp)]
#                    if lp != '*':
#                        return self.isMatch('', ''.join(rp))
#                    else:
#                        return self.isMatch(s[-1], ''.join(rp))
#        else:
#            return 1

a = 1
if a != 2:
    print(3)
elif a == 2:
    print(2)
elif a == 1:
    print(1)