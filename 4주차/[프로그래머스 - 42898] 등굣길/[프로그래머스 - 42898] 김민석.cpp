#include <string>
#include <vector>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    int road[101][101] = { 0 };
    int num = 1000000007;

    for (int i = 0; i < puddles.size(); i++)
    {
        road[puddles[i][1]][puddles[i][0]] = -1;
    }
    road[1][1] = 1;

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++) {
            if (road[i][j] == -1) continue;
            int a = 0, b = 0;
            if (road[i - 1][j] != -1) a = road[i - 1][j];// À§ÂÊ ¿õµ¢ÀÌ
            if (road[i][j - 1] != -1) b = road[i][j - 1];// ¿ÞÂÊ ¿õµ¢ÀÌ
            road[i][j] += (a + b) % num;
        }
    }
    return road[n][m];
}