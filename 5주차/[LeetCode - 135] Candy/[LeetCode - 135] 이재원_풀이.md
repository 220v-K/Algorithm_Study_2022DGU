# LeetCode - 135. Candy



## 접근

rating 리스트 두 번째부터 검사 시작.

현재 index의 rating < 다음 index의 rating 인지를 검사.

만약 그렇다면, 직전 아이가 받은 사탕 + 1 해서 줌.



현재 index의 rating > 다음 index의 rating 이라면

count++ 하며 계속 비교.

그러다 현재 index의 rating <= 다음 index의 rating이 되어 내리막길이 끝나면

count 수 - 1 부터 시작해서 다음 index부터 사탕을 지급

내려가는 비교 시작하던 index에는 그 `이전 index의 사탕 + 1`과 `count` 중 더 큰 것을 지급

(count = 5, 마지막 `현재 index의 rating > 다음 index의 rating` 의 현재 index = 3 이라면

index = 4 부터 사탕을 4, 3, 2, 1 순으로 지급.

index = 3 에는 `index=2가 받은 사탕 + 1` 과 `count(5)` 중 더 큰 것을 지급.)



현재 index의 rating = 다음 index의 rating 의 경우는

직전 index rating < 현재 index rating이라면 `직전 아이 개수+1` 개 지급

직전 index rating = 현재 index rating이라면 1개 지급

직전 index rating > 현재 index rating일 순 없음. 이미 지급되었어야 정상.

​	그리고 다음 index rating < 다다음 index rating이라면 다음 index에도 1개 지급 후 반복 재개

나머지 경우는 반복 재개.



----



접근은.. 저런 식으로 하면 됨.

근데 이제 코드를 짤 때, index가 넘어가버리거나, 맨 처음 index나 마지막 index를 처리하는 과정,

그리고 현재 index의 rating > 다음 index의 rating 일 때 직전 index rating = 현재 index rating 인지 조사하고 예외처리 해야 하는 것.

1개짜리 배열이 들어올 때.

등등을 예외처리로 빼줬음.



```python
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = []
        leng = len(ratings)
        endIndex = 0

        i = 1

        # index 0 candy
        if leng > 1:
            if ratings[0] <= ratings[1]:
                candy.append(1)
            else:
                count = 2
                endIndex = 1

                for j in range(0, leng - 1):
                    if ratings[j] <= ratings[j+1]:
                        endIndex = j
                        break
                    if j == leng - 2:
                        endIndex = j + 1
                        break

                count = endIndex + 1

                candy.append(count)
                i = endIndex + 1

                for num in range(count-1, 0, -1):
                    candy.append(num)

            # from 1 to (leng - 2) index
            while i < leng - 1:
                if ratings[i] < ratings[i+1]:
                    if ratings[i-1] == ratings[i]:
                        candy.append(1)
                    else:
                        candy.append(candy[-1] + 1)

                elif ratings[i] > ratings[i+1]:
                    count = 2
                    endIndex = i + 1

                    if i != leng - 2:
                        for j in range(i, leng - 1):
                            if ratings[j] <= ratings[j+1]:
                                endIndex = j
                                break
                            if j == leng - 2:
                                endIndex = j + 1
                                break
                        count = endIndex - i + 1

                    if ratings[i] == ratings[i-1]:
                        candy.append(count)
                    else:
                        candy.append(max(candy[-1] + 1, count))

                    for num in range(count-1, 0, -1):
                        candy.append(num)

                    i = endIndex

                else:   # ratings[i] == ratings[i+1]
                    if ratings[i-1] < ratings[i]:
                        candy.append(candy[-1] + 1)
                    else:  # ratings[i-1] == ratings[i]:
                        candy.append(1)
                    # else:   # ratings[i-1] > ratings[i]
                        # 지급되었어야 정상
                    if i+2 != leng:
                        if ratings[i+1] < ratings[i+2]:
                            candy.append(1)
                            i += 1

                i += 1

            # last number of children
            if len(candy) != leng:
                if ratings[-2] < ratings[-1]:
                    candy.append(candy[-1] + 1)
                else:  # ratings[-2] == ratings[-1]
                    candy.append(1)

        else:
            candy.append(1)

        return sum(candy)
```





