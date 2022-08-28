#include <string>
#include <vector>
#include <algorithm>
using namespace std;

long long cal(long long a, long long b, char oper) {
    if (oper == '+')
        return a + b;
    else if (oper == '-')
        return a - b;
    else if (oper == '*')
        return a * b;
}

long long solution(string expression) {
    long long answer = 0;
    vector<char> op = { '*','+','-' };
    vector<long long> num;
    vector<char> oper;

    int value = 0;
    for (int i = 0; i < expression.length(); i++)
    {
        if (expression[i] >= '0' && expression[i] <= '9')
            value = value * 10 + (expression[i] - '0');
        else {
            num.push_back(value);
            value = 0;
            oper.push_back(expression[i]);
        }
    }
    num.push_back(value);

    do
    {
        vector<long long> temp = num;
        vector<char> temp_op = oper;

        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < temp_op.size(); j++) {
                if (temp_op[j] == op[i]) {
                    temp[j] = cal(temp[j], temp[j + 1], op[i]);
                    temp.erase(temp.begin() + j + 1);
                    temp_op.erase(temp_op.begin() + j);
                    j--;
                }
            }
        }

        if (abs(temp.front()) > answer)
            answer = abs(temp.front());
    } while (next_permutation(op.begin(), op.end()));
    return answer;
}