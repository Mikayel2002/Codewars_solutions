# Given a string s. You have to return another string such that even-indexed and
# odd-indexed characters of s are grouped and groups are space-separated

def sort_my_string(s):
    str_1 = ""
    str_2 = ""

    for i in range(len(s)):
        if i % 2 == 0:
            str_1 += s[i]
        else:
            str_2 += s[i]

    return f"{str_1} {str_2}"


print(sort_my_string("CodeWars"))
