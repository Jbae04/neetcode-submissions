class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        S, T = {}, {}

        for i in range(len(s)):
            S[s[i]] = 1 + S.get(s[i],0) # we get the first letter in the string s, if we dont see it assign 0
            T[t[i]] = 1 + T.get(t[i],0) # and then add to the count so 1+ 0 then that first letter is 1 on the counter
        return S == T                        