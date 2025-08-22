def reverseW(s: str) -> str:
    def cleanSpaces(chars):
        n = len(chars)
        i, j = 0, 0
        while j < n:
            while j < n and chars[j] == " ":
                j += 1
            while j < n and chars[j] != " ":
                chars[i] = chars[j]
                i += 1
                j += 1
            while j < n and chars[j] == " ":
                j += 1
            if j < n:
                chars[i] = " "
                i += 1
        return chars[:i]
    def reverse(chars, left, right):
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
    chars = list(s)
    chars = charsSpaces(chars)
    reverse(chars, 0, len(chars) - 1)
    n = len(chars)
    start = 0
    for end in range(n + 1):
        if end == n or chars[end] == " ":
            reverse(chars, start, end - 1)
            start = end + 1

    return "".join(chars)


if __name__ == "__main__":
    s = "   hello   world   from   Java   "
    print(reverseW(s))
