#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.empty()) return 0;
        int answer = 0;
        int temp = 1;
        int len = nums.size();
        sort(nums.begin(), nums.end());
        unique(nums.begin(), nums.end());
        for (int i = 0; i < len - 1; i++)
        {   
            if(answer < temp ) { 
                answer = temp;   
            }
            if (nums[i] + 1 == nums[i + 1])
            {
                temp++;
            }
            else {
                temp = 1;
            }
            
        }
        if (answer < temp) {
            answer = temp;
        }
        return answer;
    }
};