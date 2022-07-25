class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp=[0]*len(nums)
        dp[0]=nums[0]
        q=deque([(nums[0],0)])
        
        for i in range(1,len(nums)):
            dp[i]=nums[i]+q[0][0]
            
            while q and q[-1][0]<dp[i]:
                q.pop()
                
            q.append((dp[i],i))
            
            if i-k==q[0][1]:
                q.popleft()
                
        return dp[-1]