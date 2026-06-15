class MyStack(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        self.s1.append(x)

        while self.s2:
            self.s1.append(self.s2.pop(0))
        
        self.s1 , self.s2 = self.s2 , self.s1

        
        

    def pop(self):
        """
        :rtype: int
        """


        

        return self.s2.pop(0)
        

    def top(self):
        """
        :rtype: int
        """
        

        return self.s2[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.s1 and not self.s2


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()