class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = -987654321
        
        for i in accounts:
            res = max(res, sum(i))
            
        return res