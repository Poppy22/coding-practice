// Search snippets
#include <stdlib.h>
#include <iostream>
#include <map>
#include <vector>
#include <set>

using namespace std;

int tests, words;
set<int> positions;
map<int, int> word_index;
vector<int> occurences;

/*  Time complexity: O(n)
	Search from left to right for sequences that respect the task. When a sequence is found,
	try to shorten it as much as possible by eliminating words from the left side.
*/
int solve() {
	if (words == 1) {
		return 1; // edge case
	}

	vector<int> found(words, 0); // keeps track of how mnay words of each type there are in the current selection
	int found_words = 0; // keeps track of how many of the searched words are found
	int result = (1 << 30); // maximum possible result
	set<int>::iterator last_pos = positions.begin(); // beginning of the previous selection

	for (auto const& p : positions) {
		if (found[word_index[p]] == 0) {
			found_words += 1; // add a new word found
		}
		found[word_index[p]]++; // keep track of the frequencies of words in the current selection

		if (found_words == words) { // if the current selection has all needed words
			// see if you can remove some words from the left - if they also appear in the middle
			while (*last_pos != p && found[word_index[*last_pos]] > 1) {
				found[word_index[(*last_pos)]]--;
				last_pos++; // move to the next position
			}
			result = min(result, p - *last_pos + 1);
		}
	}

	return result;
}

void read_data() {
	cin >> tests;
	for (unsigned int i = 0; i < tests; i++) {
		cin >> words;
		int w;
		for (unsigned j = 0; j < words; j++) {
			cin >> w;
			occurences.push_back(w);
		}

		for (unsigned j = 0; j < words; j++) {
			int p;
			for (unsigned k = 0; k < occurences[j]; k++) {
				cin >> p;
				positions.insert(p);
				word_index[p] = j;
			}
		}

		cout << solve() << endl;
		positions.clear();
		occurences.clear();
		word_index.clear();
	}

}

int main() {
	read_data();
	return 0;
}