#include <iostream>
#include <vector>
#include <algorithm>
// 製品の構造体
struct Product {
    int time1; // 工程1での製造時間
    int time2; // 工程2での製造時間
    int profit; // 利益
};

int maxTime1 = 7; // 工程1の最大時間
int maxTime2 = 14; // 工程2の最大時間
// 製品〇〇と△△のデータ｛工程1,工程2,売上(千円)｝
Product product0 = {2, 3, 4}; // 〇〇
Product product1 = {2, 5, 5}; // △△

int main() {
    // DPテーブルの初期化
    std::vector<std::vector<int>> dp(maxTime1 + 1, std::vector<int>(maxTime2 + 1, 0));

    // DPテーブルの更新
    for (int time1 = 0; time1 <= maxTime1; ++time1) {
        for (int time2 = 0; time2 <= maxTime2; ++time2) {
            if (time1 >= product0.time1 && time2 >= product0.time2) {
                dp[time1][time2] = std::max(dp[time1][time2], dp[time1 - product0.time1][time2 - product0.time2] + product0.profit);
            }
            if (time1 >= product1.time1 && time2 >= product1.time2) {
                dp[time1][time2] = std::max(dp[time1][time2], dp[time1 - product1.time1][time2 - product1.time2] + product1.profit);
            }
        }
    }

    // 最大利益を求める
    int maxProfitValue = dp[maxTime1][maxTime2];

    // 製造個数を求める
    int numProduct0 = 0;
    int numProduct1 = 0;
    for (int time1 = maxTime1, time2 = maxTime2; time1 > 0 && time2 > 0;) {
        if (time1 >= product0.time1 && time2 >= product0.time2 && dp[time1][time2] == dp[time1 - product0.time1][time2 - product0.time2] + product0.profit) {
            ++numProduct0;
            time1 -= product0.time1;
            time2 -= product0.time2;
        } else if (time1 >= product1.time1 && time2 >= product1.time2 && dp[time1][time2] == dp[time1 - product1.time1][time2 - product1.time2] + product1.profit) {
            ++numProduct1;
            time1 -= product1.time1;
            time2 -= product1.time2;
        } else {
            break;
        }
    }

    std::cout << "最大利益: " << ((double)maxProfitValue*0.1) << "万円\n";
    std::cout << "〇〇の個数: " << numProduct0 << "\n";
    std::cout << "△△の個数: " << numProduct1 << "\n";

    return 0;
}
