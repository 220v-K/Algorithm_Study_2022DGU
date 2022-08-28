#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <set>
using namespace std;

vector<int> solution(vector<string> gems) {
    vector<int> answer(2);
    unordered_map<string, int>m;
    set<string> num(gems.begin(), gems.end());
    int min, start = 0, end = 0;
    for (auto& s : gems)
    {
        m[s]++;
        if (m.size() == num.size()) break;
        end++;
    }
    min = end - start;
    answer[0] = start + 1;
    answer[1] = end + 1;

    while (end < gems.size())
    {
        string k = gems[start];
        m[k]--; start++;

        if (m[k] == 0) {
            end++;
            for (; end < gems.size(); end++)
            {
                m[gems[end]]++;
                if (k == gems[end])
                    break;
            }
            if (end == gems.size()) break;
        }

        if (min > end - start) {
            answer[0] = start + 1;
            answer[1] = end + 1;
            min = end - start;
        }
    }
 
    return answer;
}

