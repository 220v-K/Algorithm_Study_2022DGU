#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int time = 0;
    vector<int> timer;
    int curWeight = 0;
    
    queue<int> bridge;
    
    do
    {
        if(!timer.empty())
            for (int i = 0; i < timer.size(); i++)
            {
                timer[i]++;
            }
        time++;
        if (timer[0] > bridge_length && !timer.empty())
        {
            curWeight -= bridge.front(); 
            bridge.pop(); 
            timer.erase(timer.begin());
        }
        if (curWeight + truck_weights[0] <= weight && !truck_weights.empty()) {
            bridge.push(truck_weights[0]);
            curWeight += truck_weights[0];
            truck_weights.erase(truck_weights.begin());
            timer.push_back(1);
        }

    } while (!bridge.empty());
    return time;
}