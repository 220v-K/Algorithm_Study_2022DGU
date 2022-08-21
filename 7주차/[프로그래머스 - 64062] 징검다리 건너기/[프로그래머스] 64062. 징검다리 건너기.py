def solution(stones, k):
    def consecutive(A):
        cnt = 0
        for stone in stones:
            if stone <= A:
                cnt += 1
            else:
                cnt = 0
            # k를 초과하면 컷 (효율)
            if cnt >= k:
                return cnt
        return cnt

    high = 200000000
    low = 0
    answer = 0
    while low <= high:
        mid = int((high+low) / 2)
        num = consecutive(mid)

        if num >= k:
            high = mid - 1
        elif num < k:
            low = mid + 1

    return low
