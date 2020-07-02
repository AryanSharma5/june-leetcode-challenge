from collections import defaultdict


PRIME = 10 ** 9 + 7
BASE = 26
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        def obtain_dup_substring(S, len_substr):
            max_base = pow(BASE, len_substr - 1, PRIME)
            hash = 0
            for char in S[:len_substr]:
                hash = (hash * BASE + ord(char)) % PRIME
            hash_to_idx = defaultdict(list)
            hash_to_idx[hash].append(len_substr - 1)
            for i, char in enumerate(S[len_substr:], start=len_substr):
                char_deleted = S[i - len_substr]
                hash -= ord(char_deleted) * max_base
                hash = (hash * BASE + ord(char)) % PRIME
                if hash in hash_to_idx:
                    substr = S[i - len_substr + 1:i + 1]
                    for end_idx in hash_to_idx[hash]:
                        if S[end_idx - len_substr + 1:end_idx + 1] == substr:
                            return substr
                    else:
                        hash_to_idx[hash].append(i)
                else:
                    hash_to_idx[hash].append(i)
            return ""

        max_possible_len, min_impossble_len = 0, len(S)
        result = ""
        while min_impossble_len - max_possible_len > 1:
            length_in_middle = (max_possible_len + min_impossble_len) // 2
            substr = obtain_dup_substring(S, length_in_middle)
            if substr:
                result = substr
                max_possible_len = length_in_middle
            else:
                min_impossble_len = length_in_middle
        return result