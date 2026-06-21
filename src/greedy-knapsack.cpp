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
    
    long long n, capacity;
    infile >> n;
    
    vector<long long> weight(n), value(n);
    for (int i = 0; i < n; i++) {
        int id;
        infile >> id >> value[i] >> weight[i];
    }
    infile >> capacity;
    infile.close();
    
    auto start = high_resolution_clock::now();
    
    vector<int> order(n);
    for (int i = 0; i < n; i++) order[i] = i;
    sort(order.begin(), order.end(), [&](int a, int b) {
        return (double)value[a] / weight[a] > (double)value[b] / weight[b];
    });
    
    long long currentWeight = 0;
    long long totalValue = 0;
    for (int i : order) {
        if (currentWeight + weight[i] <= capacity) {
            currentWeight += weight[i];
            totalValue += value[i];
        }
    }
    
    auto end = high_resolution_clock::now();
    double timeMs = duration<double, milli>(end - start).count();
    
    cout << "Algorithm: Greedy" << endl;
    cout << "Dataset: " << argv[1] << endl;
    cout << "Item count: " << n << endl;
    cout << "Capacity: " << capacity << endl;
    cout << "Optimal value: " << totalValue << endl;
    cout << "Time: " << fixed << setprecision(3) << timeMs << " ms" << endl;
    
    return 0;
}