def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    if len(needle) > len(haystack):
        return -1

    needle_ptr = 0
    i = 0
    while i < len(haystack):
        item_value = haystack[i]
        if item_value == needle[needle_ptr]:
            needle_ptr += 1

            if needle_ptr == len(needle):
                return i - len(needle) + 1
        else:
            if needle_ptr != 0:
                i -= needle_ptr
            needle_ptr = 0

        i += 1

    return -1


input_data = (
    ("leetcode", "leeto"),
    ("sadbutsad", "sad"),
    ("hello", "ello"),
    ("mississippi", "issip"),
)
expected_output = (
    -1,
    0,
    1,
    4
)

actual = strStr(*input_data[3])
pass
