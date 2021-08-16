def mutate_string(string, position, character):
    sl = list(string)
    sl[position] = character
    s_new = ''.join(sl)
    return s_new


s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)