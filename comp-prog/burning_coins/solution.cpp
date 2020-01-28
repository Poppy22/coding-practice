#include <iostream>
#include <vector>

using namespace std;

int N;
vector<int> v;
vector<vector<int> > dp;

void read_data() {
	cin >> N;
	v = vector<int>(N);
	for (int i = 0; i < N; i++) {
		cin >> v[i];
	}
}


int solve() {

	// unused edge cases
	if (N == 1) {
		return v[0];
	}

	if (N == 2) {
		return  max(v[0], v[1]) - min(v[0], v[1]);
	}

	/*
		dp1[i][j] = maximum value for the first player at step i, choosing coin j
		dp2[i][j] = maximum value for the second player at step i, choosing coin j
	*/
	vector<vector<long long>> dp1(N, vector<long long> (N));
	vector<vector<long long>> dp2(N, vector<long long> (N));

	/* base case: if there was only one coin, the first player would take it */
	for(int i = 0; i < N; ++i) {
		dp1[i][i] = v[i];
		dp2[i][i] = 0;
	}

	for (int k = 2; k <= N; ++k) {
		for (int i = 0, j = k - 1; i <= N - k; ++i, ++j) {
			if (dp2[i + 1][j] + v[i] > dp2[i][j - 1] + v[j]) {
				dp1[i][j] = dp2[i + 1][j] + v[i];
				dp2[i][j] = dp1[i + 1][j];
			} else {
				dp1[i][j] = dp2[i][j - 1] + v[j];
				dp2[i][j] = dp1[i][j - 1];
			}
		}
	}

	return dp1[0][N - 1];
}

int main() {
	int tests;
	cin >> tests;
	for (unsigned int i = 0; i < tests; i++) {
		read_data();
		cout << solve() << endl;
	}
	return 0;
}