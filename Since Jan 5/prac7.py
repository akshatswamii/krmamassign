def all_freq(str1, str2):
    indices = []
    i = str1.find(str2)
    while i != -1:
        indices.append(i)
        i = str1.find(str2, i + 1)
    if len(indices) > 0:
        return indices
    else:
        return -1
print(all_freq("Akshat is at College","at"))
