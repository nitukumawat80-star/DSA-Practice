class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        scount , pcount = {} , {}
        for i in range(len(p)):
            pcount[p[i]] = pcount.get(p[i] , 0) + 1
            scount[s[i]] = scount.get(s[i] , 0) + 1

        if pcount == scount:
            rev = [0]
        else:
            rev = []

        l = 0
        for i in range(len(p) , len(s)): 
            scount[s[i]] = scount.get(s[i] , 0) + 1
            scount[s[l]] -= 1

            if scount[s[l]] == 0:
                scount.pop(s[l])
            l += 1
            if scount == pcount:
                rev.append(l)


        return rev