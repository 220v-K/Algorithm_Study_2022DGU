#include <string>
#include <vector>
#include <algorithm>

using namespace std;
vector<string> answer;
bool dfs(vector<vector<string>> tickets, int curcnt, vector<bool> visit, string start) {
    if (curcnt == tickets.size()) return true;

    for (int i = 0; i < tickets.size(); i++)
    {
        bool temp = false;
        if (!visit[i] && start == tickets[i][0]) {
            visit[i] = true;
            answer.push_back(tickets[i][1]);
            temp = dfs(tickets, curcnt + 1, visit, tickets[i][1]);
            if (temp) return true;
            visit[i] = false;
        }
    }
    answer.pop_back();
    return false;
}

vector<string> solution(vector<vector<string>> tickets) {
    vector<bool> visit(tickets.size(), false);
    sort(tickets.begin(), tickets.end());
    answer.push_back("ICN");
    dfs(tickets, 0, visit , "ICN");
    return answer;
}

// A -> B, C 인경우 B로 가야할것 같지만 B에서 더이상 진행 할 수 없으면 여기로 가면 안됨.  
//vector<string> answer;
//string start = "ICN";
//answer.push_back("ICN");
//while (!tickets.empty()) {
//    string next_Airport;
//    int index = 0;
//
//    for (int i = 0; i < tickets.size(); i++)
//    {
//        if (start == tickets[i][0]) {
//            next_Airport = tickets[i][1];
//            break;
//        }
//    }
//    for (int j = 0; j < tickets.size(); j++)
//    {
//        if (start == tickets[j][0] && next_Airport >= tickets[j][1]) {
//            next_Airport = tickets[j][1];
//            index = j;
//        }
//    }
//    tickets.erase(tickets.begin() + index);
//    start = next_Airport;
//    answer.push_back(next_Airport);
//}
//
//return answer;