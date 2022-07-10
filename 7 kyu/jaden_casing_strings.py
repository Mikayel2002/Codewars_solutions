def to_jaden_case(str_1):
    cap_word_list = map(lambda x: x.capitalize(), str_1.split(" "))

    return " ".join(cap_word_list)


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
