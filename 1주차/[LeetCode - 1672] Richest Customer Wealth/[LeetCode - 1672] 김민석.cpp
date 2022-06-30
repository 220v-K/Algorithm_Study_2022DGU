class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int result = 0;
        for (int i = 0; i < accounts.size(); i++)
        {
            result = max(result, accumulate(accounts[i].begin(), accounts[i].end(), 0));
        }
        return result;
    }
};