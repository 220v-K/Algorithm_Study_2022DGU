#include <string>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

bool cmp(const pair<int, int>& a, const pair<int, int>& b) {
    if (a.second == b.second) return a.first > b.first;
    return a.second > b.second;
}

vector<int> solution(string s) {
    vector<int> answer;
    map<int, int> m;

    string temp;
    for (int i = 1; i < s.length()-1; i++)
    {
        if (s[i] != '{' && s[i] != '}' && s[i] != ',') {
            temp += s[i];
            if (s[i + 1] != ',' && s[i + 1] != '}') continue;
            m[stoi(temp)]++;
        }
        temp.clear();
    }

    vector<pair<int, int>> v(m.begin(), m.end());
    sort(v.begin(), v.end(), cmp);

    for (auto i : v)
    {
        answer.emplace_back(i.first);
    }
    return answer;
}