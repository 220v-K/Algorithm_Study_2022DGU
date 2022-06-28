class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        vector<int> temp(128);
        for (const auto c : magazine)
        {
            temp[c]++;
        }
        for (const auto c : ransomNote)
        {
            temp[c]--;
            if (temp[c] < 0)
                return false;
        }
        return true;
    }
};