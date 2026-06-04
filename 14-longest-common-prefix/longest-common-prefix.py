class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        reve = ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        for i in range(len(first)):
            if first[i] != last[i]:
                return reve
            reve += first[i]
        return reve