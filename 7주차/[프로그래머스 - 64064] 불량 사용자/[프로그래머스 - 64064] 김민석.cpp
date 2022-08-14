#include <string>
#include <vector>
#include <set>

using namespace std;

vector<vector<int>> v(8); //불량 사용자 목록 저장할 벡터
bool visit[8];
set<string> s;


void dfs(int index, int n) {
	if (index == n) {
		string temp = "";
		for (int i = 0; i < 8; i++)
		{
			if (visit[i]) temp += to_string(i);
		}
		s.insert(temp);
		
		return;
	}

	for (int i = 0; i < v[index].size(); i++)
	{
		int cur = v[index][i];
		if (visit[cur]) continue;
		visit[cur] = true;
		dfs(index + 1, n);
		visit[cur] = false;
	}
	return;
}
int solution(vector<string> user_id, vector<string> banned_id) {
	int answer = 0;
	for (int i = 0; i < banned_id.size(); i++)
	{
		for (int j = 0; j < user_id.size(); j++) {
			if (banned_id[i].length() != user_id[j].length())
				continue;
			bool istrue = true;
			for (int k = 0; k < user_id[i].size(); k++)
			{
				if (banned_id[i][k] == '*') continue;
				if (banned_id[i][k] == user_id[j][k]) continue;
				istrue = false;
				break;
			}
			if (istrue) v[i].push_back(j);
		}
	}
	dfs(0, banned_id.size());
	answer = s.size();
	return answer;
}