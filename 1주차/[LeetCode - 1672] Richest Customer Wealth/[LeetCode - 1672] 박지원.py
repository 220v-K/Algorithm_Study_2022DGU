class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        acc_len = len(accounts)
        print(acc_len)
        
        money = len(accounts[0])
        print(money)        
        
        a = []
        
        for i in range(0, acc_len):
            a.append(sum(accounts[i]))
        
        a.sort(reverse = True)
        
        return a[0]