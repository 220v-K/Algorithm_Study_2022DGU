#include <string>
#include <vector>
#include <iostream>

#include <algorithm>
using namespace std;

int main() {
	int n, answer = 1;
	cin >> n;
	vector<int> weight(n);
	for (int i = 0; i < n; i++)
	{
		cin >> weight[i];
	}
	sort(weight.begin(), weight.end());

	for (int i = 0; i < weight.size(); i++)
	{
		if (answer < weight[i]) break;
		answer += weight[i];
	}

	cout << answer << endl;
	return 0;
}