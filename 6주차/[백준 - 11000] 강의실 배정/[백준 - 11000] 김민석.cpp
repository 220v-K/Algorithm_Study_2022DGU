#include <string>
#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int main() {
	int n;
	pair<int, int> p[2000001];
	priority_queue<int, vector<int>, greater<int>> pq;

	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cin >> p[i].first >> p[i].second;
	}

	sort(p, p + n);

	pq.push(p[0].second);
	
	for (int i = 1; i < n; i++)
	{
		if (pq.top() <= p[i].first) {
			pq.pop();
			pq.push(p[i].second);
		}
		else
		{
			pq.push(p[i].second);
		}
	}
	cout << pq.size() << endl;

	return 0;
}