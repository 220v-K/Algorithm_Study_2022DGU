#include <string>
#include <vector>
#include <queue>

class Solution {
public:
    int maxResult(vector<int>& nums, int k) {
       //우선 순위 큐를 이용해 누적되는 합과 인덱스를 저장
        priority_queue<pair<int, int>> pq; 
        pq.push({ nums[0], 0 });
        for (int i = 1; i < nums.size(); i++) {
            while (!pq.empty() && pq.top().second < i - k) 
                pq.pop();  
            pq.push({ nums[i] + pq.top().first, i });
        }

        while (pq.top().second != nums.size() - 1) pq.pop();
        return pq.top().first;
    }

};