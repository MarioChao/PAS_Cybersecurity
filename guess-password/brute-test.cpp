#include <iostream>
#include <chrono>
#include <vector>
using namespace std;

namespace {
	chrono::high_resolution_clock::time_point getTime();
	void bruteforce_recur(string &chars, int digits, vector<char> &pass, int depth = 0);
	void bruteforce_it(string &chars, int digits);

	bool bruteforce_recur_guess(string &chars, int digits, vector<char> &pass, vector<char> &userPass, int depth = 0);
	bool bruteforce_it_guess(string &chars, int digits, string &userPass);

	double testBruteforceAll(string chars, int digits, bool useRecur = true);
	double testBruteforce_specific(string chars, int digits, string inputPass, bool useRecur = true);

	string getPassString(vector<char> &pass);

	void mainTestBruteforce();
	void mainTestInputPasswords();

	const string numbersOnly = "1234567890";
	const string lowercase = "abcdefghijklmnopqrstuvwxyz";
	const string lowerUpper = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
	const string numberLowerUpper = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
	const string allAscii = " !\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~";
	// string allAscii;

	long long guesses;
}

int main() {
	// allAscii = "";
	// for (int i = 32; i < 127; i++) {
	// 	allAscii += (char) i;
	// }
	// mainTestBruteforce();
	mainTestInputPasswords();
}

namespace {
	chrono::high_resolution_clock::time_point getTime() {
		return chrono::high_resolution_clock::now();
	}

	void bruteforce_recur(string &chars, int digits, vector<char> &pass, int depth) {
		if (depth == digits) {
			// Guess
			return;
		}

		// Bruteforce next digit
		for (char c : chars) {
			pass.push_back(c);
			bruteforce_recur(chars, digits, pass, depth + 1);
			pass.pop_back();
		}
	}

	void bruteforce_it(string &chars, int digits) {
		string pass(digits, chars[0]);
		vector<int> pass_digit_index(digits, 0);
		const int charsSize = (int) chars.length();
		bool isFinished = false;
		while (!isFinished) {
			// Guess
			if (true) {
				// cout << getPassString(pass) << '\n';
			}

			// Increment loop
			// from the last digit
			for (int i = digits - 1; i >= 0; i--) {
				pass_digit_index[i]++;
				// Carry
				if (pass_digit_index[i] >= charsSize) {
					pass_digit_index[i] = 0;
					pass[i] = chars[0];
					if (i == 0) {
						isFinished = true;
						break;
					}
				} else {
					pass[i] = chars[pass_digit_index[i]];
					break;
				}
			}
		}
	}

	bool bruteforce_recur_guess(string &chars, int digits, vector<char> &pass, vector<char> &userPass, int depth) {
		if (depth == digits) {
			// Guess
			guesses++;
			return pass == userPass;
		}

		// Bruteforce next digit
		bool res = false;
		for (char c : chars) {
			pass.push_back(c);
			res |= bruteforce_recur_guess(chars, digits, pass, userPass, depth + 1);
			pass.pop_back();
			if (res) return res;
		}
		return res;
	}

	bool bruteforce_it_guess(string &chars, int digits, string &userPass) {
		string pass(digits, chars[0]);
		vector<int> pass_digit_index(digits, 0);
		const int charsSize = (int) chars.length();
		bool isFinished = false;
		while (!isFinished) {
			// Guess
			if (true) {
				guesses++;
				if (pass == userPass) {
					return true;
				}
			}

			// Increment loop
			// from the last digit
			for (int i = digits - 1; i >= 0; i--) {
				pass_digit_index[i]++;
				// Carry
				if (pass_digit_index[i] >= charsSize) {
					pass_digit_index[i] = 0;
					pass[i] = chars[0];
					if (i == 0) {
						isFinished = true;
						break;
					}
				} else {
					pass[i] = chars[pass_digit_index[i]];
					break;
				}
			}
		}
		return false;
	}

	double testBruteforceAll(string chars, int digits, bool useRecur) {
		auto startTime = getTime();
		if (useRecur) {
			vector<char> pass = {};
			bruteforce_recur(chars, digits, pass);
		} else {
			bruteforce_it(chars, digits);
		}
		auto endTime = getTime();
		auto duration = chrono::duration_cast<chrono::microseconds>(endTime - startTime);
		double durationSeconds = duration.count() / (1e6);
		cout << "------------------------------\n";
		cout << "Chars: " << chars.length() << '\n';
		cout << "Digits: " << digits << '\n';
		cout << "Duration: " << durationSeconds << "s\n";
		return durationSeconds;
	}

	double testBruteforce_specific(string chars, int digits, string inputPass, bool useRecur) {
		auto startTime = getTime();
		if (useRecur) {
			vector<char> pass = {};
			vector<char> userPass;
			for (char c : inputPass) userPass.push_back(c);
			bruteforce_recur_guess(chars, digits, pass, userPass);
		} else {
			bruteforce_it_guess(chars, digits, inputPass);
		}
		auto endTime = getTime();
		auto duration = chrono::duration_cast<chrono::microseconds>(endTime - startTime);
		double durationSeconds = duration.count() / (1e6);
		cout << "------------------------------\n";
		cout << "Guess time: " << durationSeconds << "s\n";
		return durationSeconds;
	}

	string getPassString(vector<char> &pass) {
		string res = "";
		for (char c : pass) {
			res += c;
		}
		return res;
	}

	void mainTestBruteforce() {
		// testBruteforceAll(allAscii, 4, true);
		// testBruteforceAll(allAscii, 4, false);

		// testBruteforceAll(lowerUpper, 5, true);
		// testBruteforceAll(lowerUpper, 5, false);
		for (int i = 0; i < 3; i++) {
			// testBruteforceAll(numbersOnly, 9);
			// testBruteforceAll(lowercase, 6);
			// testBruteforceAll(lowerUpper, 5);
			// testBruteforceAll(numberLowerUpper, 5);
			// testBruteforceAll(allAscii, 5);
		}
	}

	void mainTestInputPasswords() {
		vector<string> inputPasses;
		{
			string inputPass;
			for (int i = 0; i < 3; i++) {
				cout << "Enter pass:\n";
				getline(cin, inputPass);
				inputPasses.push_back(inputPass);
			}
		}
		auto startTime = getTime();
		for (string inputPass : inputPasses) {
			int digits = (int) inputPass.length();
			guesses = 0;
			// testBruteforce_specific(allAscii, digits, inputPass, true);
			testBruteforce_specific(allAscii, digits, inputPass, false);
			cout << "Guesses: " << guesses << '\n';
		}
		auto endTime = getTime();
		auto duration = chrono::duration_cast<chrono::microseconds>(endTime - startTime);
		double durationSeconds = duration.count() / (1e6);
		cout << "------------------------------\n";
		cout << "Total guess time: " << durationSeconds << "s\n";
	}
}
