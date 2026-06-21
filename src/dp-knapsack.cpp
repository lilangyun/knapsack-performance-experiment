#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <iomanip>
#include <algorithm>

using namespace std;
using namespace chrono;

int main(int argc, char* argv[]) {
    if (argc < 2) {
        cout << "Usage: " << argv[0] << " <datafile>" << endl;
        return 1;
    }
    
    ifstream infile(argv[1]);
    if (!infile.is_open()) {
        cout << "Failed to open file: " << argv[1] << endl;
        return 1;
    }
    
    int n;
    long long capacity;
    infile >> n;
    
    vector<long long> weight(n), value(n);
    for (int i = 0; i < n; i++) {
        int id;
        infile >> id >> value[i] >> weight[i];
    }
    infile >> capacity;
    infile.close();
    
    auto start = high_resolution_clock::now();
    
    vector<long long> dp(capacity + 1, 0);
    
    for (int i = 0; i < n; i++) {
        for (long long w = capacity; w >= weight[i]; w--) {
            dp[w] = max(dp[w], dp[w - weight[i]] + value[i]);
        }
    }
    
    auto end = high_resolution_clock::now();
    double timeMs = duration<double, milli>(end - start).count();
    
    cout << "Algorithm: Dynamic Programming" << endl;
    cout << "Dataset: " << argv[1] << endl;
    cout << "Item count: " << n << endl;
    cout << "Capacity: " << capacity << endl;
    cout << "Optimal value: " << dp[capacity] << endl;
    cout << "Time: " << fixed << setprecision(3) << timeMs << " ms" << endl;
    
    return 0;
}