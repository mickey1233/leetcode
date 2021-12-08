def longestPalindrome(s) -> str:
    result_odd = ''
    result_even = ''

    for i in range(len(s)):
        left_odd = i
        right_odd = i

        while(left_odd >= 0 and right_odd < len(s) and s[left_odd] == s[right_odd]):
            left_odd -= 1
            right_odd += 1
        result_odd = max(result_odd, s[left_odd+1:right_odd], key=len)
        left_even = i
        right_even = i + 1

        while(left_even >= 0 and right_even < len(s) and s[left_even] == s[right_even]):
            left_even -= 1
            right_even += 1
        result_even = max(result_even, s[left_even+1:right_even], key=len)

    return max(result_odd, result_even, key=len)


if __name__ == "__main__":
    print(longestPalindrome("babad"))
    print(longestPalindrome("cbbd"))
    print(longestPalindrome("a"))
    print(longestPalindrome("ac"))
    print(longestPalindrome(""))
