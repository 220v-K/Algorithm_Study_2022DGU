#include <string>
#include <vector>
using namespace std;

class Solution {
public:
   int candy(vector<int>& ratings) {
        int answer = 0;
        vector<int> candyleft(ratings.size(), 1);
        vector<int> candyright(ratings.size(), 1);

        for (int i = 1; i < ratings.size(); i++)
        {
            if (ratings[i] > ratings[i - 1])
                candyleft[i] = candyleft[i - 1] + 1;
            else
                candyleft[i] = 1;
        }

        for (int i = ratings.size() - 2; i > -1; i--)
        {
            if (ratings[i] > ratings[i + 1])
                candyright[i] = candyright[i + 1] + 1;
            else
                candyright[i] = 1;
        }

        for (int i = 0; i < ratings.size(); i++)
        {
            answer += max(candyleft[i], candyright[i]);
        }
        return answer;
    }
};
