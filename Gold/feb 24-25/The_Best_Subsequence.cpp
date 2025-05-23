#include <iostream>
#include <vector>
#include <string>
#include <utility>

int main() {
    int n_val, m, q;
    std::cin >> n_val >> m >> q;

    long long n = n_val;
    std::vector<std::pair<int, int>> updates(m);
    for (int i = 0; i < m; ++i) {
        std::cin >> updates[i].first >> updates[i].second;
    }

    std::vector<int> diff_array(n_val + 2, 0);
    for (const auto& [l, r] : updates) {
        diff_array[l]++;
        if (r + 1 <= n_val) {
            diff_array[r + 1]--;
        } else if (r + 1 == n_val + 1) {
            diff_array[r + 1]--;
        }
    }

    std::vector<int> fj_string_bits(n_val + 1);
    int current_sum = 0;
    for (int i = 1; i <= n_val; ++i) {
        current_sum += diff_array[i];
        fj_string_bits[i] = current_sum % 2;
    }

    for (int query_index = 0; query_index < q; ++query_index) {
        int l_query, r_query, k_query;
        std::cin >> l_query >> r_query >> k_query;

        std::string result_subsequence;
        result_subsequence.reserve(k_query);
        int current_l_index = l_query;

        for (int j = 1; j <= k_query; ++j) {
            int best_index = -1;

            for (int i = current_l_index; i <= r_query - (k_query - j); ++i) {
                if (fj_string_bits[i] == 1) {
                    best_index = i;
                    break;
                }
            }

            if (best_index != -1) {
                result_subsequence += '1';
                current_l_index = best_index + 1;
            } else {
                for (int i = current_l_index; i <= r_query - (k_query - j); ++i) {
                    if (fj_string_bits[i] == 0) {
                        best_index = i;
                        break;
                    }
                }

                if (best_index != -1) {
                    result_subsequence += '0';
                    current_l_index = best_index + 1;
                }
            }
        }

        constexpr long long MOD_VALUE = 1000000007;
        long long decimal_value = 0;
        long long power_of_2 = 1;

        for (int i = static_cast<int>(result_subsequence.length()) - 1; i >= 0; --i) {
            if (result_subsequence[i] == '1') {
                decimal_value = (decimal_value + power_of_2) % MOD_VALUE;
            }
            power_of_2 = (power_of_2 * 2) % MOD_VALUE;
        }

        std::cout << decimal_value << '\n';
    }

    return 0;
}
