# LeetCode - 1696. Jump Game VI

## 접근1

DP.. Top-Down 방식으로 재귀를 이용해 구현.

i번째부터 점프를 시작할 때의 최대 score를 `score[i]` 라고 저장 (메모이제이션)

그렇게 score[0]을 구해가는 방법.

```python
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        lenOfnum = len(nums)

        # index 'i' 부터 시작했을 때의 최대 score
        score = {lenOfnum-1: nums[lenOfnum-1]}

        # end index부터 반대로 순회


        def dp(i):
            a = score.get(i, None)
            if i + 1 == lenOfnum:
                return nums[lenOfnum-1]
            if a != None:
                return a

            tempScore = set()
            for j in range(1, k+1):
                if i+j < lenOfnum:
                    tempScore.add(dp(i+j))

            score[i] = max(tempScore) + nums[i]

            return score[i]
        
        return dp(0)
```

시간초과.



## 접근2

그렇다면... Bottom-Up 방식으로 풀어야 시간초과가 안 나는걸까?

Bottom-Up 방식의 for문으로 바꿔봄.

```python
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        lenOfnum = len(nums)

        # index 'i' 부터 시작했을 때의 최대 score
        score = {lenOfnum-1: nums[lenOfnum-1]}

        # end index - 1 부터 반대로 순회
        for i in range(lenOfnum-2, -1, -1):
            tempScore = set()
            for j in range(1, k+1):
                if i+j < lenOfnum:
                    tempScore.add(score[i+j])

            score[i] = max(tempScore) + nums[i]

        return score[0]
```

근데도 시간초과.



## 접근3, 포기

그럼 뭔가 계산과정을 줄일 게 없나 생각해보자..

하고 짜다가.. 도저히 해결법이 안 나옴.

하고 discuss를 봤다..

deque(queue)를 써서 풀이하더라.

https://leetcode.com/problems/jump-game-vi/discuss/1261753/JS-Python-Java-C%2B%2B-or-Easy-DP-Deque-Solution-w-Explanation

```python
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        deq = deque([n-1])
        for i in range(n-2, -1, -1):
            if deq[0] - i > k:
                deq.popleft()
            nums[i] += nums[deq[0]]
            
            while len(deq) and nums[deq[-1]] <= nums[i]:
                deq.pop()
            deq.append(i)
        return nums[0]
```

Topic쪽 보니까, 우선순위 큐(힙) 이 있던데..

좀 더 공부해야겠음 ㅎㅎ;
