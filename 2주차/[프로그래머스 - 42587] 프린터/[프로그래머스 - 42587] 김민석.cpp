#include <string>
#include <vector>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    while (!priorities.empty()) {
        for (int i = 1; i < priorities.size(); i++)
        {
            if (priorities[0] < priorities[i]) {
                priorities.push_back(priorities[0]);
                priorities.erase(priorities.begin());
                i = 0;
                if (location == 0) location = priorities.size() - 1;
                else location--;
            }
        }
        priorities.erase(priorities.begin());
        answer++;
        if (location == 0) return answer;
        else location--;

    }
}