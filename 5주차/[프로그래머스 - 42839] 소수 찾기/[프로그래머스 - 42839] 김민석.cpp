#include <string>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

bool isPrime(int num) {
	if (num < 2) return false;
	for (int i = 2; i <= sqrt(num); i++)
	{
		if (num % i == 0) return false;
	}
	return true;
}

int solution(string numbers) {
    int answer = 0;
	vector<char> num;
	vector<int> allnum;

	for (int i = 0; i < numbers.size(); i++)
	{
		num.push_back(numbers[i]);
	}
	sort(num.begin(), num.end());

	do
	{
		string temp = "";
		for (int i = 0; i < num.size(); i++)
		{
			temp.push_back(num[i]);
			allnum.push_back(stoi(temp));
		}
	} while (next_permutation(num.begin(), num.end()));

	sort(allnum.begin(), allnum.end());
	//불필요한 값들 제거
	allnum.erase(unique(allnum.begin(), allnum.end()), allnum.end());

	for (int i = 0; i < allnum.size(); i++)
	{
		if (isPrime(allnum[i]))
			answer++;
	}
    return answer;
}