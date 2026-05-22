'''
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 0:
            return 0
        else:
            return self.fib(n-1) + self.fib(n-2)
        
'''

# Method 2

'''
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a,b = 1,1
        sum = 0
        if n==0:
            return 0
        elif n<=2:
            return 1
        else:
            for i in range(n-2):
                sum = a + b
                a = b
                b = sum
        return sum
'''
