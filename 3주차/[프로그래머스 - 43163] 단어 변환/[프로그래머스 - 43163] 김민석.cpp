#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int answer = 51;
int Checking[51];

bool checkstring(string temp1, string temp2) {
    int cnt = 0;

    for (int i = 0; i < temp1.size(); i++)
    {
        if (temp1[i] != temp2[i]) cnt++;
    }
    if (cnt == 1)
        return true;
    else
        return false;
}

void dfs(string str, string target, vector<string> words, int cnt) {
    if (answer <= cnt) //횟수가 더 크면 탐색 x
        return;

    if (str == target)
    {
        answer = min(answer, cnt); // 최소값 유지
        return;
    }

    for (int i = 0; i < words.size(); i++)
    {
        if (Checking[i] == 0 && checkstring(str, words[i])) {
            Checking[i] = 1;
            dfs(words[i], target, words, cnt + 1);
            Checking[i] = 0;
        }
    }
    return;
}
int solution(string begin, string target, vector<string> words) {
    dfs(begin, target, words, 0);
    
    if (answer == 51)
    {
        return 0;
    }
    return answer;
}
