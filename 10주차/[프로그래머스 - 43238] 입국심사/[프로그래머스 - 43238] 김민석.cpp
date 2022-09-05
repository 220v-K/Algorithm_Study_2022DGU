#include <string>
#include <vector>
#include <algorithm>
using namespace std;
/*
모든 사람이 심사 받는데 걸리는 시간의 최솟값 = > 시간
최소 시간(기다리는 사람 1명 심사관 심사 시간 1분)은 1분, 
최대 시간(기다리는 사람 n명이 심시 시간이 가장긴 심사관에게 다 가는경우)은 times[times.size()-1] * n분 (times 정렬)
start = 1 ,end = times[tiems.size() -1] * n
mid 시간 (이 시간동안 처리 할 수있는 사람의 수 측정)

mid가 n보다 작으면 start 처리
mid가 n보다 크면 end 처리
start < end 라면 반복
*/
long long solution(int n, vector<int> times) {
    long long answer = 0;
    sort(times.begin(), times.end());

    long long start = 1;
    long long end = (long long)times[times.size() - 1] * n; 
    long long mid;

    while (start <= end)
    {
        mid = (start + end) / 2;
        long long count = 0;

        for (int i = 0; i < times.size(); i++)
        {
            count += mid / times[i];
        }
        if (count < n) {
            start = mid + 1;
        }
        else {
            if (mid <= end)
                answer = mid;

            end = mid - 1;
        }  
    }
  
    return answer;
}

