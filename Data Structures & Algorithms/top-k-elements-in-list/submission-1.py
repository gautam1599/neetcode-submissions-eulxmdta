class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        for n in nums:
            hm[n]=hm.get(n,0)+1
        freq=sorted(hm.items(),key=lambda x:x[1], reverse=True)
        return [item[0] for item in freq[:k]]