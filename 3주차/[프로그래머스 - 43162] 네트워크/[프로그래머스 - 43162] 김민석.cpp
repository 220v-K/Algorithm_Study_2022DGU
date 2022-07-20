#include <string>
#include <vector>

using namespace std;
vector<int> CheckingCpt(200);
void fuc(int n, vector<vector<int>> computers, int index);

int solution(int n, vector<vector<int>> computers) {
	int answer = 0;

	for (int i = 0; i < n; i++)
	{
		if (CheckingCpt[i] == 0) {
			fuc(n, computers, i);
			answer++;
		}
	}
	return answer;
}

void fuc(int n, vector<vector<int>> computers, int index)
{
	CheckingCpt[index] = 1;
	for (int i = 0; i < n; i++)
	{
		if (CheckingCpt[i] == 0 && computers[index][i] == 1)
			fuc(n, computers, i);
	}

}
