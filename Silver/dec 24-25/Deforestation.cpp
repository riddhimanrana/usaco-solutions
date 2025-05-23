#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class FenwickTree {
    vector<int> tree;
    int size;
public:
    FenwickTree(int n) : size(n), tree(n + 1, 0) {}

    void update(int index, int value) {
        for (++index; index <= size; index += index & (-index))
            tree[index] += value;
    }

    [[nodiscard]] int query(int index) {
        int sum = 0;
        for (++index; index > 0; index -= index & (-index))
            sum += tree[index];
        return sum;
    }

    [[nodiscard]] int rangeQuery(int left, int right) {
        if (left > right) return 0;
        return query(right) - query(left - 1);
    }
};

struct Interval {
    long long start, end;
    int count;

    Interval(long long s, long long e, int c) : start(s), end(e), count(c) {}

    bool operator<(const Interval& other) const {
        if (end == other.end)
            return start < other.start;
        return end < other.end;
    }
};

int getLowerBoundIndex(const vector<long long>& array, long long key) {
    return lower_bound(array.begin(), array.end(), key) - array.begin();
}

int getUpperBoundIndex(const vector<long long>& array, long long key) {
    return upper_bound(array.begin(), array.end(), key) - array.begin();
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int testCases;
    cin >> testCases;

    while (testCases--) {
        int numTrees, numIntervals;
        cin >> numTrees >> numIntervals;

        vector<long long> treePositions(numTrees);
        for (int i = 0; i < numTrees; ++i) {
            cin >> treePositions[i];
        }
        sort(treePositions.begin(), treePositions.end());

        vector<Interval> intervals;
        intervals.reserve(numIntervals);
        for (int i = 0; i < numIntervals; ++i) {
            long long start, end;
            int count;
            cin >> start >> end >> count;
            intervals.emplace_back(start, end, count);
        }
        sort(intervals.begin(), intervals.end());

        FenwickTree fenwickTree(numTrees);
        vector<bool> selected(numTrees, false);

        for (const auto& [intervalStart, intervalEnd, intervalCount] : intervals) {
            int leftIdx = getLowerBoundIndex(treePositions, intervalStart);
            int rightIdx = getUpperBoundIndex(treePositions, intervalEnd) - 1;

            if (leftIdx > rightIdx || leftIdx >= numTrees || rightIdx < 0) {
                continue;
            }

            if (int currentSelectedInInterval = fenwickTree.rangeQuery(leftIdx, rightIdx);
                intervalCount - currentSelectedInInterval > 0) {

                int needed = intervalCount - currentSelectedInInterval;

                for (int i = rightIdx; i >= leftIdx && needed > 0; --i) {
                    if (!selected[i]) {
                        selected[i] = true;
                        fenwickTree.update(i, 1);
                        needed--;
                    }
                }
            }
        }

        int totalSelected = 0;

        if (numTrees > 0) {
            totalSelected = fenwickTree.query(numTrees - 1);
        }

        cout << numTrees - totalSelected << '\n';
    }

    return 0;
}
