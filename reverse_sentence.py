def revers_words(s):
    s=" ".join(s.split()[::-1])
    return s

print(revers_words("this is an sentence"))