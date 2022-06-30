class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        vector<vector<int>> value(mat.size(),vector<int>(2,0));
        vector<int> result(k);
        int i, j;
        for (i = 0; i < mat.size(); i++)
        {
            int count = 0;
            for (j = 0; j < mat[i].size(); j++)
            {
                if (mat[i][j] == 1) count++;
            }
            value[i][0] = count;
            value[i][1] = i;
        }
        sort(value.begin(), value.end());

        for (int i = 0; i < k; i++)
        {
            result[i] = value[i][1];
        }
        return result;
    }
};