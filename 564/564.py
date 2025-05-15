class Solution:
    def nearestPalindromic(self, n: str) -> str:
        is_odd = (len(n) % 2 == 1)

        root_len = ceil(len(n) / 2)
        root = n[:root_len]

        if is_odd:
            end = int(n[root_len-1:])
        else:
            end = int(n[root_len:])

        large_root = int(root)
        small_root = int(root)

        if int(root[::-1]) <= end:
            large_root += 1

        if int(root[::-1]) >= end:
            small_root -= 1

        def construct_palindrome(odd: bool, s: str) -> str:
            if odd: return s + s[-2::-1]
            else: return s + s[::-1]

        large_root = str(large_root)
        small_root = str(small_root)

        if len(large_root) > root_len:
            if is_odd: large_root = large_root[:-1] # too many zeros
            larger = construct_palindrome(not is_odd, large_root)
        else:
            larger = construct_palindrome(is_odd, large_root)

        if len(small_root) < root_len:
            if not is_odd: small_root += '9' # not enough nines
            smaller = construct_palindrome(not is_odd, small_root)
        else:
            smaller = construct_palindrome(is_odd, small_root)
            if not is_odd and small_root == '0': smaller = '9'

        if int(larger) - int(n) < int(n) - int(smaller):
            return larger
        else:
            return smaller
