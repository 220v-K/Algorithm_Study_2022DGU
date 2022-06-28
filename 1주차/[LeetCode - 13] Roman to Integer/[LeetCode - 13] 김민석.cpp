class Solution {
public:
    int romanToInt(string s) {
        map<char, int> m;
        m['I'] = 1;
        m['V'] = 5;
        m['X'] = 10;
        m['L'] = 50;
        m['C'] = 100;
        m['D'] = 500;
        m['M'] = 1000;
        int sum = 0;
        int len = s.length();
        for (int i = 0; i < len; i++)
        {
            if (s[i] == 'I' && (i+1) < len && s[i+1] == 'V')
            {
                sum += 4;
                i++;
            }
            else if (s[i] == 'I' && (i + 1) < len && s[i+1] == 'X')
            {
                sum += 9;
                i++;
            }
            else if (s[i] == 'X' && (i + 1) < len && s[i+1] == 'L')
            {
                sum += 40;
                i++;
            }
            else if (s[i] == 'X' && (i + 1) < len && s[i+1] == 'C')
            {
                sum += 90;
                i++;
            }
            else if (s[i] == 'C' && (i + 1) < len && s[i+1] == 'D')
            {
                sum += 400;
                i++;
            }
            else if (s[i] == 'C' && (i + 1) < len && s[i+1] == 'M')
            {
                sum += 900;
                i++;
            }
            else 
            {
                sum += m[s[i]];
            }
        }
        return sum;
    }
};