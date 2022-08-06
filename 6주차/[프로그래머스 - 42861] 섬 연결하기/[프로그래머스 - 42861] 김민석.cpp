#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp(const vector<int>& a, const vector<int>& b)
{
    return a[2] < b[2];
}
int highnode(int n, vector<int> &temp) {
    if (n == temp[n]) return n;
    else return temp[n] = highnode(temp[n], temp);
}
bool make_bridge(int n, int m, vector<int> &temp) {
    n = highnode(n, temp);
    m = highnode(m, temp);
    if (n == m) return false;
    else {
        if (n > m) temp[n] = m;
        else temp[m] = n;
    }
    return true;
}
int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    vector<int> temp;
    sort(costs.begin(), costs.end(), cmp);
    for (int i = 0; i < n; i++)
        temp.push_back(i);

    for (int i = 0; i < costs.size(); i++)
    {
        if (make_bridge(costs[i][0], costs[i][1], temp)) {
            answer += costs[i][2];
        }
    }
    
    return answer;
}