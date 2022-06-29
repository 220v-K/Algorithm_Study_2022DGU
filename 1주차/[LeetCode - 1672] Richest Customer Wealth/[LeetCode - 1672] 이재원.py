class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = [sum(List) for List in accounts]
        wealth.sort(reverse=True)
        return wealth[0]
