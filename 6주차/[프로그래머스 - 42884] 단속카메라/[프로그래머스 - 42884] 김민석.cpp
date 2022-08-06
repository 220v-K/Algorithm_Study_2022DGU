#include <string>
#include <vector>
#include <algorithm>

using namespace std;
bool cmp(const vector<int>& a, const vector<int>& b)
{
    return a[1] < b[1];
}
int solution(vector<vector<int>> routes) {
    int answer = 0;
    int C_location = -30001;
    sort(routes.begin(), routes.end(), cmp);
    for (int i = 0; i < routes.size(); i++)
    {
        if (routes[i][0] > C_location) {
            C_location = routes[i][1];
            answer++;
        }
    }

    return answer;
}