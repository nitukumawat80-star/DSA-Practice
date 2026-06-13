class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bic = {')' : '(' , '}' : '{' , ']' : '['}
        s1 = []
        for i in s:
            if i in "([{":
                s1.append(i)

            else:
                if len(s1) > 0 and s1[-1] == bic[i]:
                    s1.pop()

                else:
                    s1.append(i)


        if not s1:
            return True

        else:
            return False