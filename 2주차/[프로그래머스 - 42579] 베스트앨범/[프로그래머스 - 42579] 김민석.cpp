#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    map<string, int> genres_map; //장르당 최종 플레이 값
    map<string, map<int, int>> playlist; //장르 -> 고유번호, 플레이 횟수
    for (int i = 0; i < genres.size(); i++)
    {
        genres_map[genres[i]] += plays[i];
        playlist[genres[i]][i] = plays[i];
    }
    while (genres_map.size() > 0)
    {
        int max = 0;
        string temp_gen;
        for (auto gen : genres_map)
        {
            if (max < gen.second) {
                max = gen.second;
                temp_gen = gen.first;
            }
        }
        for (int i = 0; i < 2; i++)
        {
            int index = -1, playVal = 0;
            for (auto pl : playlist[temp_gen])
            {
                if (playVal < pl.second) {
                    playVal = pl.second;
                    index = pl.first;
                }
            }
            if (index == -1) break; //장르에 단 한가지의 노래밖에 없을 경우
            answer.push_back(index);
            playlist[temp_gen].erase(index);
        }
        genres_map.erase(temp_gen);
    }
    
    return answer;
}
