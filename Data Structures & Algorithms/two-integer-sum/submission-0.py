class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}
        for i,n in enumerate(nums):
            res=target-n
            if res in mp:
                return [mp[res],i]
            mp[n]=i
            
        