def find_needle(haystack):
    for i in haystack:
        if i == "needle":
            return f"found the needle at position {haystack.index(i) + 1}"


print(find_needle(haystack=["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))
