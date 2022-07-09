#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    queue<int> day;

    for (int i = 0; i < progresses.size(); i++)
    {
        day.push((99 - progresses[i]) / speeds[i] + 1); //speeds가 1일경우 포함
    }
    
    while (!day.empty())
    {
        int count = 1;
        int temp = day.front();
        day.pop();
        while (!day.empty() && day.front() <= temp)
        {
            count++;
            day.pop();
        }
        answer.push_back(count);
    }
    return answer;
}