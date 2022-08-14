#include <string>
#include <vector>
#include <stack>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
	stack<int> s;

	for (int i = 0; i < moves.size(); i++)
	{
		int doll = -1;
		for (int j = 0; j < board.size(); j++)
		{
			if (board[j][moves[i] - 1] != 0) {
				doll = board[j][moves[i] - 1];
				board[j][moves[i] - 1] = 0;
				break;
			}
		}
		if (doll == -1) continue;

		if (s.empty()) s.push(doll);
		else
		{
			if (s.top() == doll) { s.pop(); answer += 2; }
			else s.push(doll);
		}
	}

    return answer;
}