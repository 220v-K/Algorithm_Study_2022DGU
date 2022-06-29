class Solution {
public:
    int romanToInt(string s) {
        vector<int> num;
    int sum = 0;

    for (int i = 0; i < s.length(); i++) {
        switch (s[i]) {
            case 'I':
                num.push_back(1);
                break;
            case 'V':
                num.push_back(5);
                break;
            case 'X':
                num.push_back(10);
                break;
            case 'L':
                num.push_back(50);
                break;
            case 'C':
                num.push_back(100);
                break;
            case 'D':
                num.push_back(500);
                break;
            case 'M':
                num.push_back(1000);
                break;
            default:
                break;
        }
    }

    for (int i = 0; i < num.size(); i++) {
        if (i != num.size() - 1) {
            bool isReverse = (num[i] < num[i + 1]);

            if (isReverse) {
                num.insert(num.begin() + i, num[i + 1] - num[i]);
                num.erase(num.begin() + i + 1);
                num.erase(num.begin() + i + 1);
            }
        }
    }

    for (int i = 0; i < num.size(); i++) {
        sum += num[i];
    }

    return sum;
    }
};