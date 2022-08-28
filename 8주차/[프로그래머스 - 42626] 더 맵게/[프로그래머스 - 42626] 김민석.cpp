#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int, vector<int>, greater<int>> pq;

    for (int i = 0; i < scoville.size(); i++)
    {
        pq.push(scoville[i]);
    }

    while (pq.size() > 1 && pq.top() < K)
    {
        int temp1 = 0, temp2 = 0;
        temp1 = pq.top();
        pq.pop();
        temp2 = pq.top();
        pq.pop();
        int newScovile = temp1 + (temp2 * 2);
        pq.push(newScovile);
        answer++;
    }
    if (pq.top() < K) return -1;
    return answer;
}

