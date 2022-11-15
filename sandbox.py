alphabets = ['a', 'b', 'c', 'ch', 'dd', 'd', 'e', 'f', 'ff', 'g', 'ng', 'h', 'i', 'j', 'l', 'll', 'm', 'n', 'o', 'p',
             'ph', 'r', 'rh', 's', 't', 'th', 'u', 'w', 'y']
alpha_index = {}
for idx, val in enumerate(alphabets):
    alpha_index[val] = idx


def comp(s):
    ret = []
    i = 0
    while i < len(s):
        if i + 1 < len(s) and s[i] + s[i + 1] in alpha_index.keys():
            ret.append(alpha_index[s[i] + s[i + 1]])
            i += 2
        else:
            ret.append(alpha_index[s[i]])
            i += 1

    return tuple(ret)


strings = ['abcd', 'dd', 'dda', 'abcdd']
a = strings.sort(key=comp)
print(strings)
