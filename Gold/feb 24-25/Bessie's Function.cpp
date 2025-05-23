#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;

    std::vector<int> f(N + 1);
    for (int i = 1; i <= N; i++) {
        std::cin >> f[i];
    }

    std::vector<long long> c(N + 1);
    for (int i = 1; i <= N; i++) {
        std::cin >> c[i];
    }

    std::vector<int> state(N + 1, 0);
    std::vector<bool> inCycle(N + 1, false);
    std::vector<int> comp(N + 1, -1);
    int compCount = 0;
    std::vector<std::vector<int>> cycles;

    auto dfs = [&](int u, auto& self) -> void {
        state[u] = 1;
        int nxt = f[u];
        if (state[nxt] == 0) {
            self(nxt, self);
        } else if (state[nxt] == 1) {
            compCount++;
            std::vector<int> cyc;
            int cur = nxt;
            cyc.push_back(cur);
            inCycle[cur] = true;
            comp[cur] = compCount - 1;
            for (int v = f[cur]; v != cur; v = f[v]) {
                cyc.push_back(v);
                inCycle[v] = true;
                comp[v] = compCount - 1;
            }
            cycles.push_back(std::move(cyc));
        }
        state[u] = 2;
    };

    for (int i = 1; i <= N; i++) {
        if (state[i] == 0) dfs(i, dfs);
    }

    std::vector<std::vector<int>> children(N + 1);
    for (int i = 1; i <= N; i++) {
        if (!inCycle[i])
            children[f[i]].push_back(i);
    }

    std::vector<std::vector<long long>> dp(N + 1, std::vector<long long>(2, 0));

    auto dfsTree = [&](int u, auto& self) -> void {
        for (int v : children[u]) {
            self(v, self);
        }
        long long costNotFixed = 0, costFixed = 0;
        costFixed = c[u];
        for (int v : children[u]) {
            costNotFixed += dp[v][1];
            costFixed += std::min(dp[v][0], dp[v][1]);
        }
        dp[u][0] = costNotFixed;
        dp[u][1] = costFixed;
    };

    std::vector<bool> visitedTree(N + 1, false);

    auto markTree = [&](int u, auto& self) -> void {
        visitedTree[u] = true;
        for (int v : children[u]) {
            if (!visitedTree[v])
                self(v, self);
        }
    };

    for (int i = 1; i <= N; i++) {
        if (!inCycle[i] && !visitedTree[i]) {
            dfsTree(i, dfsTree);
            markTree(i, markTree);
        }
    }

    std::vector<long long> Fval(N + 1, 0), Uval(N + 1, 0);
    for (int i = 1; i <= N; i++) {
        if (inCycle[i]) {
            long long addFixed = 0, addUnfixed = 0;
            for (int v : children[i]) {
                addFixed += std::min(dp[v][0], dp[v][1]);
                addUnfixed += dp[v][1];
            }
            Fval[i] = ((f[i] == i) ? 0 : c[i]) + addFixed;
            Uval[i] = addUnfixed;
        }
    }

    long long ans = 0;
    std::vector<bool> processedCycle(N + 1, false);

    for (int compId = 0; compId < compCount; compId++) {
        const auto& cyc = cycles[compId];
        int L = static_cast<int>(cyc.size());

        for (int v : cyc) processedCycle[v] = true;

        constexpr long long INF = 1LL << 60;
        long long bestCycle = INF;

        std::vector<std::vector<long long>> dpCycle(L, std::vector<long long>(2, INF));
        dpCycle[0][0] = Uval[cyc[0]];
        dpCycle[0][1] = INF;

        for (int i = 1; i < L; i++) {
            dpCycle[i][0] = dpCycle[i - 1][1] + Uval[cyc[i]];
            dpCycle[i][1] = std::min(dpCycle[i - 1][0], dpCycle[i - 1][1]) + Fval[cyc[i]];
        }

        if (dpCycle[L - 1][1] < INF)
            bestCycle = std::min(bestCycle, dpCycle[L - 1][1]);

        dpCycle.assign(L, std::vector<long long>(2, INF));
        dpCycle[0][1] = Fval[cyc[0]];
        dpCycle[0][0] = INF;

        for (int i = 1; i < L; i++) {
            dpCycle[i][0] = dpCycle[i - 1][1] + Uval[cyc[i]];
            dpCycle[i][1] = std::min(dpCycle[i - 1][0], dpCycle[i - 1][1]) + Fval[cyc[i]];
        }

        long long candidate = std::min(dpCycle[L - 1][0], dpCycle[L - 1][1]);
        bestCycle = std::min(bestCycle, candidate);

        // Special case for self-loops
        if (L == 1) {
            bestCycle = Fval[cyc[0]];
        }

        ans += bestCycle;
    }

    std::cout << ans << '\n';
    return 0;
}
