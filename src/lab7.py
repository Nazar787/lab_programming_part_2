def rabin_karp(haystack: str, needle: str) -> list[int]:
    if not needle or not haystack or len(needle) > len(haystack):
        return []

    base = 256
    prime = 101
    m = len(needle)
    n = len(haystack)

    needle_hash = 0
    window_hash = 0
    h = 1


    for _ in range(m - 1):
        h = (h * base) % prime

    for i in range(m):
        needle_hash = (base * needle_hash + ord(needle[i])) % prime
        window_hash = (base * window_hash + ord(haystack[i])) % prime

    result = []

    for i in range(n - m + 1):
        if needle_hash == window_hash:
            if haystack[i:i + m] == needle:
                result.append(i)

        if i < n - m:
            window_hash = (
                base * (window_hash - ord(haystack[i]) * h) + ord(haystack[i + m])
            ) % prime
            if window_hash < 0:
                window_hash += prime

    return result
