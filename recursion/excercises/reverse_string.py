def reverse_sting(string):
    if string == "":
        return ""
    return string[-1] + reverse_sting(string[:-1])


print(reverse_sting("python"))
