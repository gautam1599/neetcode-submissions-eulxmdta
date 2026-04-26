class Solution:
    def countBits(self, n: int) -> List[int]:
        f=[0]*(n+1)
        for i in range(n+1):
            res=bin(i).count('1')
            f[i]=res
        return f