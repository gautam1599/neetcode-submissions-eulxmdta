class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=set()
        for n in nums:
            if n in res:
                res.remove(n)
            else:
                res.add(n)
        return list(res)[0]