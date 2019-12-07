def shift_left(a, b):
    n = 0
    for i in range(len(a) + len(b)):
        if len(a) >= len(b) and str(a) != str(b):
            a = a[1:len(a)]
            n += 1
        elif len(a) < len(b) and str(a) != str(b):
            b = b[1:len(b)]
            n += 1
        else:
            continue
    return n
