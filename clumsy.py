class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 2:
            return N
        if N <= 4:
            return N+3
        
        if N % 4 == 0:
            return N+1
        elif N % 4 <= 2:
            return N+2
        return N-1
val=Solution()
n=int(input())
print(val.clumsy(n))
