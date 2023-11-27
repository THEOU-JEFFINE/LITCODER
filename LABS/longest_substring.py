import sys


def longest_substring(s):
    start = 0
    max_length = 0
    char_index_map = {}

    for index, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1

        char_index_map[char] = index
        max_length = max(max_length, index - start + 1)

    return max_length


input_string = input()
result = longest_substring(input_string)
print(result)
