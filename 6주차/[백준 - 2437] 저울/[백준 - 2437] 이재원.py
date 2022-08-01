import sys
read = sys.stdin.readline

N = int(read().strip("\n"))
a = list(map(int, read().strip("\n").split()))

a.sort()
sum = 0
answer = 0

if a[0] > 1:
    answer = 1
else:
    for i in a:
        if sum + 1 < i:
            break
        sum += i

# answer에 값이 담기지 않았을 때 (배열 내 최댓값보다 작은 모든 값을 구현 가능)
# 에는 모든 값의 합 + 1이 답이 됨.
answer = sum + 1

print(answer)
