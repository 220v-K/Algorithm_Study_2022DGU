#include <string>
#include <vector>

using namespace std;

void fuc(vector<int> numbers, int target, int sum, int index);
int answer = 0;

int solution(vector<int> numbers, int target) {

    fuc(numbers, target, 0, 0);

    return answer;
}

void fuc(vector<int> numbers, int target, int sum, int index) {
    //³¡±îÁö Å½»ö
    if (index == numbers.size())
    {
        if (sum == target)
        {
            answer++;
        }
        return;
    }
    fuc(numbers, target, sum + numbers[index], index + 1);
    fuc(numbers, target, sum - numbers[index], index + 1);
}