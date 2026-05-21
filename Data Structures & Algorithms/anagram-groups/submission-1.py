class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for s in strs:
            ss=''.join(sorted(s))
            if ss not in res:
                res[ss]=[]
            if ss in res:
                res[ss].append(s)
        return list(res.values())
        