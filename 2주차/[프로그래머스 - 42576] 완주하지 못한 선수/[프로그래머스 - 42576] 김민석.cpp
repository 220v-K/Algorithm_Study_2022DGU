
#include <string>
#include <vector>
#include<algorithm>
using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());

    int i = 0;
    for (i =0; i < completion.size(); i++)
    {
        if (participant[i] != completion[i])
            break;
    }
    return participant[i];
}