#include <string>
#include <vector>

using namespace std;

string solution(vector<int> numbers, string hand) {
    string answer = "";
    int leftHand = 10, rightHand = 12, leftDist = 0, rightDist = 0;

    for (int i = 0; i < numbers.size(); i++)
    {
        if (numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7)
        {
            answer += "L";
            leftHand = numbers[i];
        }
        else if (numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9)
        {
            answer += "R";
            rightHand = numbers[i];
        }
        else
        {
            if (numbers[i] == 0)
                numbers[i] = 11;
            int tmp_l = abs(leftHand - numbers[i]);
            int tmp_r = abs(rightHand - numbers[i]);

            leftDist = (tmp_l / 3) + (tmp_l % 3);
            rightDist = (tmp_r / 3) + (tmp_r % 3);

            if (leftDist == rightDist)
            {
                if (hand == "right")
                {
                    answer += "R";
                    rightHand = numbers[i];
                }
                else
                {
                    answer += "L";
                    leftHand = numbers[i];
                }
            }
            else if (leftDist < rightDist)
            {
                answer += "L";
                leftHand = numbers[i];
            }
            else
            {
                answer += "R";
                rightHand = numbers[i];
            }
        }
    }
    return answer;
}
