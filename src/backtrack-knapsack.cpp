#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <iomanip>
#include <algorithm>

using namespace std;
using namespace chrono;

long long n, capacity;
vector<long long> weight, value;
long long bestValue = 0;

long long bound(int i, long long currentWeight, long long currentValue) {
    long long remainingValue = currentValue;
    long long remainingWeight = currentWeight;
    
    vector<pair<double, long long>> remaining;
    for (int j = i; j < n; j++) {
        remaining.push_back({(double)value[j] / weight[j], j});
    }
    sort(remaining.begin(), remaining.end(), [](const pair<double,long long>& a, const pair<double,long long>& b) {
        return a.first > b.first;
    });
    
    for (const auto& item : remaining) {
        int idx = item.second;
        if (remainingWeight + weight[idx] <= capacity) {
            remainingWeight += weight[idx];
            remainingValue += value[idx];
        } 
        else {
            long long remain = capacity - remainingWeight;
            remainingValue += (long long)(value[idx] * ((double)remain / weight[idx]));
            break;
        }
    }
    
    return remainingValue;
}

void backtrack(int i, long long currentWeight, long long currentValue) {
    if (i == n) {
        if (currentValue > bestValue) {
            bestValue = currentValue;
        }
        return;
    }
    
    if (bound(i, currentWeight, currentValue) <= bestValue) {
        return;
    }
    
    backtrack(i + 1, currentWeight, currentValue);
    
    if (currentWeight + weight[i] <= capacity) {
        backtrack(i + 1, currentWeight + weight[i], currentValue + value[i]);
    }
}

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
    
    infile >> n;
    weight.resize(n);
    value.resize(n);
    for (int i = 0; i < n; i++) {
        int id;
        infile >> id >> value[i] >> weight[i];
    }
    infile >> capacity;
    infile.close();
    
    auto start = high_resolution_clock::now();
    
    bestValue = 0;
    backtrack(0, 0, 0);
    
    auto end = high_resolution_clock::now();
    double timeMs = duration<double, milli>(end - start).count();
    
    cout << "Algorithm: Backtrack" << endl;
    cout << "Dataset: " << argv[1] << endl;
    cout << "Item count: " << n << endl;
    cout << "Capacity: " << capacity << endl;
    cout << "Optimal value: " << bestValue << endl;
    cout << "Time: " << fixed << setprecision(3) << timeMs << " ms" << endl;
    
    return 0;
}