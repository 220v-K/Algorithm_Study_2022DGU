## 접근1

우선 제일 먼저 생각난 접근은,

리스트를 정렬한 후 하나씩 pop하며 제일 긴 연속된 횟수를 산정하는 것.

그러나 시간복잡도가 O(n)으로 제한되어 있으므로, 

O(nlogn)인 sort() 함수를 써서 정렬할 수 없음.



그래서 다음에 든 생각은 삽입, 삭제에 적은 시간이 드는 최소 힙을 이용하는 것.

그러나 최소 힙의 삽입, 삭제도 O(logn)이므로, 총 O(nlogn)이 되어 O(n)보다 커지게 됨.



그러면.. 더 빠른 남은 건 Hash밖에 없는데..

해시로 어떻게 접 근 을 할 까...

1. 리스트에서 최솟값, 최댓값 찾기 - O(n)
2. 딕셔너리에 리스트의 값들을 key값으로 지정하여 추가 - O(n)
3. 최솟값부터 최댓값까지 dictionary에 key값이 있는 지 검사하며, 최대로 반복되는 횟수 측정 - O(n)

이렇게 하면 될 듯?



```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        mini = min(nums)
        maxi = max(nums)

        dict1 = dict(zip(nums, range(len(nums))))

        maxLengSeq = 0
        tempMax = 0

        for i in range(mini, maxi+1):
            if i in dict1:
                tempMax += 1
                if maxLengSeq < tempMax:
                    maxLengSeq = tempMax
            else:
                tempMax = 0

        return maxLengSeq
```

근데 시간초과됨. ㅠㅠ



아마 최댓값이 너무 크거나 최솟값이 너무 작으면 그걸 다 순회하면서 시간초과가 되는 듯..



## 접근2

그렇다면 다른 접근으로 가 보 자.

모든 key값을 순회하면서, 그 key값부터 시작하는 가장 긴 시퀀스의 길이를 조사하는 것으로.

근데 여기까지 와서 왜 굳이 딕셔너리로 했지? 집합으로 하면 되는데?

라고 생각나서 이번엔 집합으로 해보겠음.

1. 집합에 리스트를 때려넣음
2. 모든 집합 원소를 순회
   - 그 원소부터 연속되는 다음 원소가 없을 때까지 순회.
   - 그리고 그 길이와 원래 저장된 길이 중 큰 것을 저장.



```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        maxlength = 0

        for i in s:
            j = i
            Fin = False

            while not Fin:
                if j in s:
                    j += 1
                else:
                    maxlength = max(maxlength, j - i)
                    Fin = True
        
        return maxlength
```

그리고 또 시간초과 뜸. ㅠ



## 접근3

사실 이건.. 한 원소의 순회 과정에서 정해지지 않은 개수의 원소를 돌아보니 완벽한 O(n)이라고 할 수 있는지..

그럼 순회할 때마다 집합에서 제거하는 방식으로 가면 속도가 좀 개선되지 않을까.

근데 이러면 이제 한 원소를 검사할 때 앞뒤로 쭉 지워나가는 방식으로 두 쪽 다 검사해야됨.



이렇게 하니까.. 풀렸네? ㅋㅋ

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        maxlength = 0

        for i in nums:
            j = i + 1
            k = i
            tempMax = 0
            Fin = False

            while not Fin:
                if j in s:
                    s.remove(j)
                    j += 1
                elif k in s:
                    s.remove(k)
                    k -= 1
                else:
                    maxlength = max(maxlength, j - k - 1)
                    Fin = True
        
        return maxlength
```

