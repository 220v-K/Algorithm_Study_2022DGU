#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int nextindex(vector<int> &app, int start, int findnum) {
	for (int i = start; i < app.size(); i++)
	{
		if (app[i] == findnum) return i;
	}
	return 0;
}
int main() {
	int n, k, answer = 0, cur = 0;
	cin >> n >> k;
	vector<int> app(k);	// 전기용품 이름
	vector<int> current(n);//현재 콘센트에 꽂은 전기용품
	vector<int> num(k + 1);	//전기용품의 갯수
	for (int i = 0; i < k; i++)
	{
		cin >> app[i];
	}

	for (int i = 0; i < app.size(); i++)
	{
		num[app[i]]++;
	}
	for (int i = 0; i < app.size(); i++)
	{
		if (cur < n && find(current.begin(), current.end(), app[i]) == current.end())	//콘센트가 비어있을 경우
		{
			current[cur++] = app[i];
			num[app[i]]--;
			continue;
		}

		if (find(current.begin(), current.end(), app[i]) != current.end()) {
			num[app[i]]--;
		}
		else
		{
			vector<int> temp;
			for (int j = 0; j < current.size(); j++)
			{
				if (num[current[j]] == 0) {
					answer++;
					current[j] = app[i];
					break;
				}
				temp.push_back(nextindex(app, i, current[j]));
			}
			if (temp.size() != current.size()) continue;
			int min = max_element(temp.begin(), temp.end()) - temp.begin();
			current[min] = app[i];
			num[current[min]]--;
			answer++;
		}
	}
	cout << answer << endl;
	return 0;
}