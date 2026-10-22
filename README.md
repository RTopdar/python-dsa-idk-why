# Python DSA Practice

Random DSA/problem-solving scripts. Learning Python, trying stuff out.

## Basics

- [fizz-buzz.py](fizz-buzz.py) — FizzBuzz from 1 to 100
- [print_recursion.py](print_recursion.py) — Recursive number printing and factorial
- [hcf.py](hcf.py) — Highest common factor using recursion
- [power.py](power.py) — Power function using divide and conquer
- [recursive_power_of_2.py](recursive_power_of_2.py) — Check whether a number is a power of 3
- [recursion_fibbonacci.py](recursion_fibbonacci.py) — Tribonacci and Fibonacci with recursion
- [palindrome_check.py](palindrome_check.py) — Check whether a number is a palindrome
- [odd-number-count-in-interval-range.py](odd-number-count-in-interval-range.py) — Count odd numbers in a range (asks for input)
- [count-digits-that-divide-number.py](count-digits-that-divide-number.py) — Check which digits divide the number
- [subtract-product-sum-of-integer.py](subtract-product-sum-of-integer.py) — Product minus sum of a number's digits
- [convert-to-sentence-case.py](convert-to-sentence-case.py) — Fix sentence casing in a string
- [string_last_letter.py](string_last_letter.py) — Filter words that end in "e"

## Arrays

- [bubble_sort.py](bubble_sort.py) — Sort a list with bubble sort
- [how-many-numbers-smaller-than-current-number.py](how-many-numbers-smaller-than-current-number.py) — Count smaller numbers for each element
- [kids-with-candies.py](kids-with-candies.py) — Kids with candies (LeetCode-style)
- [running_sum.py](running_sum.py) — Running sum of an array
- [greatest_subarray.py](greatest_subarray.py) — Maximum sum subarray (brute force)
- [max_area.py](max_area.py) — Container with most water (simplified)
- [sort_by_parity.py](sort_by_parity.py) — Move even numbers to the front
- [intersection_of_arrays.py](intersection_of_arrays.py) — Intersection of two arrays
- [remove_duplicates_from_sorted_array.py](remove_duplicates_from_sorted_array.py) — Remove duplicates from a sorted array
- [remove_duplicates_from_unsorted_array.py](remove_duplicates_from_unsorted_array.py) — Remove duplicates from an unsorted array
- [remove-duplicates-coming-in-array-more-than-twice.py](remove-duplicates-coming-in-array-more-than-twice.py) — Keep at most two copies of each value
- [median_of_sorted_arrays.py](median_of_sorted_arrays.py) — Median of two sorted arrays
- [two_sum.py](two_sum.py) — Two sum (brute force and hash map version)
- [twosuminputarraysorted.py](twosuminputarraysorted.py) — Two sum on a sorted array (two pointers)

## Strings

- [common_prefix.py](common_prefix.py) — Longest common prefix of a list of strings
- [anagram.py](anagram.py) — Check anagrams and group words that are anagrams of each other
- [firstuniquechar.py](firstuniquechar.py) — Index of the first non-repeating character
- [longest_unique_substrings.py](longest_unique_substrings.py) — Longest substring with no repeated characters
- [three_good_substrings.py](three_good_substrings.py) — 3-character substrings with all distinct characters (includes a test runner)

## dsa_speedrun_1

- [dsa_speedrun_1/movezeroes.py](dsa_speedrun_1/movezeroes.py) — Move zeroes to the end in place
- [dsa_speedrun_1/stocksell.py](dsa_speedrun_1/stocksell.py) — Best time to buy and sell a stock
- [dsa_speedrun_1/twosum.py](dsa_speedrun_1/twosum.py) — Two sum with a hash map

## speedrun_2

Practice set with built-in tests: arrays, strings, sets, dictionaries, loops (easy to medium).
Each file has the problem statement, an empty function and 5–8 test cases (examples + edge cases).
Write your solution in place of `pass`, then run the file to check every case.

```bash
uv run speedrun_2/01_two_sum.py   # run one problem's tests
uv run speedrun_2/run_all.py      # scoreboard for all problems
```

Current output of `run_all.py`:

```text
 7/7   01_two_sum.py
 7/7   02_contains_duplicate.py
 7/7   03_move_zeroes.py
 7/7   04_best_time_to_buy_sell_stock.py
11/11  05_maximum_subarray.py
 6/6   06_product_except_self.py
 6/6   07_missing_number.py
 7/7   08_merge_intervals.py
 8/8   09_valid_palindrome.py
 7/7   10_reverse_words.py
 0/7   11_valid_anagram.py
 0/7   12_first_unique_char.py
 0/8   13_longest_substring_no_repeat.py
 0/7   14_string_compression.py
 0/7   15_longest_common_prefix.py
 0/6   16_intersection_of_arrays.py
 0/7   17_longest_consecutive_sequence.py
 0/7   18_happy_number.py
 0/6   19_find_all_duplicates.py
 0/6   20_group_anagrams.py
 0/6   21_top_k_frequent.py
 0/6   22_majority_element.py
 0/6   23_word_frequency.py
 0/7   24_isomorphic_strings.py
 0/7   25_subarray_sum_equals_k.py
 0/5   26_fizzbuzz.py
 0/7   27_spiral_matrix.py
 0/5   28_pascals_triangle.py
 0/7   29_rotate_array.py
 0/8   30_valid_parentheses.py
 0/7   31_three_sum.py
 0/6   32_ransom_note.py
 0/6   33_word_pattern.py
 0/7   34_roman_to_integer.py
 0/7   35_sort_colors.py
 0/7   36_pivot_index.py
 0/7   37_summary_ranges.py
 0/5   38_jewels_and_stones.py
 0/5   39_set_mismatch.py
 0/7   40_is_subsequence.py
 0/5   41_rotate_image.py
 0/5   42_find_disappeared_numbers.py
 0/6   43_merge_sorted_arrays.py
 0/7   44_longest_repeating_replacement.py
 0/5   45_valid_sudoku.py
 0/6   46_find_all_anagrams.py
 0/6   47_unique_emails.py
 0/7   48_second_largest.py

Solved 10/48 problems
```

- [speedrun_2/_runner.py](speedrun_2/_runner.py) — Shared test runner (PASS/FAIL per case, counter, timing)
- [speedrun_2/run_all.py](speedrun_2/run_all.py) — Runs every problem and prints how many are solved
- [speedrun_2/01_two_sum.py](speedrun_2/01_two_sum.py) — Two Sum (Easy, Arrays / Dictionaries)
- [speedrun_2/02_contains_duplicate.py](speedrun_2/02_contains_duplicate.py) — Contains Duplicate (Easy, Arrays / Sets)
- [speedrun_2/03_move_zeroes.py](speedrun_2/03_move_zeroes.py) — Move Zeroes (Easy, Arrays / Two pointers)
- [speedrun_2/04_best_time_to_buy_sell_stock.py](speedrun_2/04_best_time_to_buy_sell_stock.py) — Best Time to Buy and Sell Stock (Easy, Arrays / Loops)
- [speedrun_2/05_maximum_subarray.py](speedrun_2/05_maximum_subarray.py) — Maximum Subarray (Medium, Arrays / Kadane)
- [speedrun_2/06_product_except_self.py](speedrun_2/06_product_except_self.py) — Product of Array Except Self (Medium, Arrays / Prefix)
- [speedrun_2/07_missing_number.py](speedrun_2/07_missing_number.py) — Missing Number (Easy, Arrays / Sets / Math)
- [speedrun_2/08_merge_intervals.py](speedrun_2/08_merge_intervals.py) — Merge Intervals (Medium, Arrays / Sorting / Loops)
- [speedrun_2/09_valid_palindrome.py](speedrun_2/09_valid_palindrome.py) — Valid Palindrome (Easy, Strings / Two pointers)
- [speedrun_2/10_reverse_words.py](speedrun_2/10_reverse_words.py) — Reverse Words in a String (Easy, Strings)
- [speedrun_2/11_valid_anagram.py](speedrun_2/11_valid_anagram.py) — Valid Anagram (Easy, Strings / Dictionaries)
- [speedrun_2/12_first_unique_char.py](speedrun_2/12_first_unique_char.py) — First Unique Character (Easy, Strings / Dictionaries)
- [speedrun_2/13_longest_substring_no_repeat.py](speedrun_2/13_longest_substring_no_repeat.py) — Longest Substring Without Repeating Characters (Medium, Strings / Sets / Sliding window)
- [speedrun_2/14_string_compression.py](speedrun_2/14_string_compression.py) — String Compression (Easy, Strings / Loops)
- [speedrun_2/15_longest_common_prefix.py](speedrun_2/15_longest_common_prefix.py) — Longest Common Prefix (Easy, Strings / Loops)
- [speedrun_2/16_intersection_of_arrays.py](speedrun_2/16_intersection_of_arrays.py) — Intersection of Two Arrays (Easy, Sets)
- [speedrun_2/17_longest_consecutive_sequence.py](speedrun_2/17_longest_consecutive_sequence.py) — Longest Consecutive Sequence (Medium, Sets)
- [speedrun_2/18_happy_number.py](speedrun_2/18_happy_number.py) — Happy Number (Easy, Sets / Loops)
- [speedrun_2/19_find_all_duplicates.py](speedrun_2/19_find_all_duplicates.py) — Find All Duplicates (Easy, Sets / Loops)
- [speedrun_2/20_group_anagrams.py](speedrun_2/20_group_anagrams.py) — Group Anagrams (Medium, Dictionaries / Strings)
- [speedrun_2/21_top_k_frequent.py](speedrun_2/21_top_k_frequent.py) — Top K Frequent Elements (Medium, Dictionaries / Sorting)
- [speedrun_2/22_majority_element.py](speedrun_2/22_majority_element.py) — Majority Element (Easy, Dictionaries)
- [speedrun_2/23_word_frequency.py](speedrun_2/23_word_frequency.py) — Word Frequency (Easy, Dictionaries / Strings)
- [speedrun_2/24_isomorphic_strings.py](speedrun_2/24_isomorphic_strings.py) — Isomorphic Strings (Easy, Dictionaries / Strings)
- [speedrun_2/25_subarray_sum_equals_k.py](speedrun_2/25_subarray_sum_equals_k.py) — Subarray Sum Equals K (Medium, Dictionaries / Prefix sum)
- [speedrun_2/26_fizzbuzz.py](speedrun_2/26_fizzbuzz.py) — FizzBuzz (Easy, Loops)
- [speedrun_2/27_spiral_matrix.py](speedrun_2/27_spiral_matrix.py) — Spiral Matrix (Medium, Loops / 2D arrays)
- [speedrun_2/28_pascals_triangle.py](speedrun_2/28_pascals_triangle.py) — Pascal's Triangle (Easy, Loops / Arrays)
- [speedrun_2/29_rotate_array.py](speedrun_2/29_rotate_array.py) — Rotate Array (Medium, Arrays)
- [speedrun_2/30_valid_parentheses.py](speedrun_2/30_valid_parentheses.py) — Valid Parentheses (Easy, Strings / Stack / Dictionaries)
- [speedrun_2/31_three_sum.py](speedrun_2/31_three_sum.py) — 3Sum (Medium, Arrays / Sorting / Two pointers)
- [speedrun_2/32_ransom_note.py](speedrun_2/32_ransom_note.py) — Ransom Note (Easy, Dictionaries / Strings)
- [speedrun_2/33_word_pattern.py](speedrun_2/33_word_pattern.py) — Word Pattern (Easy, Dictionaries / Strings)
- [speedrun_2/34_roman_to_integer.py](speedrun_2/34_roman_to_integer.py) — Roman to Integer (Easy, Dictionaries / Loops)
- [speedrun_2/35_sort_colors.py](speedrun_2/35_sort_colors.py) — Sort Colors (Medium, Arrays / Two pointers)
- [speedrun_2/36_pivot_index.py](speedrun_2/36_pivot_index.py) — Find Pivot Index (Easy, Arrays / Prefix sum)
- [speedrun_2/37_summary_ranges.py](speedrun_2/37_summary_ranges.py) — Summary Ranges (Easy, Arrays / Loops / Strings)
- [speedrun_2/38_jewels_and_stones.py](speedrun_2/38_jewels_and_stones.py) — Jewels and Stones (Easy, Sets / Strings)
- [speedrun_2/39_set_mismatch.py](speedrun_2/39_set_mismatch.py) — Set Mismatch (Easy, Sets / Arrays)
- [speedrun_2/40_is_subsequence.py](speedrun_2/40_is_subsequence.py) — Is Subsequence (Easy, Strings / Two pointers)
- [speedrun_2/41_rotate_image.py](speedrun_2/41_rotate_image.py) — Rotate Image (Medium, Loops / 2D arrays)
- [speedrun_2/42_find_disappeared_numbers.py](speedrun_2/42_find_disappeared_numbers.py) — Find All Disappeared Numbers (Easy, Sets / Arrays)
- [speedrun_2/43_merge_sorted_arrays.py](speedrun_2/43_merge_sorted_arrays.py) — Merge Two Sorted Arrays (Easy, Arrays / Two pointers)
- [speedrun_2/44_longest_repeating_replacement.py](speedrun_2/44_longest_repeating_replacement.py) — Longest Repeating Character Replacement (Medium, Strings / Dictionaries / Sliding window)
- [speedrun_2/45_valid_sudoku.py](speedrun_2/45_valid_sudoku.py) — Valid Sudoku (Medium, Sets / Loops / 2D arrays)
- [speedrun_2/46_find_all_anagrams.py](speedrun_2/46_find_all_anagrams.py) — Find All Anagrams in a String (Medium, Strings / Dictionaries / Sliding window)
- [speedrun_2/47_unique_emails.py](speedrun_2/47_unique_emails.py) — Unique Email Addresses (Easy, Strings / Sets)
- [speedrun_2/48_second_largest.py](speedrun_2/48_second_largest.py) — Second Largest Distinct (Easy, Arrays / Loops)

## Other

- [main.py](main.py) — Entry point (minimal)
- [pyproject.toml](pyproject.toml) — Project config
- [uv.lock](uv.lock) — Locked dependencies for `uv`

## Running

```bash
python <script>.py
```

Or use `uv` for dependency management:

```bash
uv run <script>.py
```

---

IDK why this repo exists, but here we are.
