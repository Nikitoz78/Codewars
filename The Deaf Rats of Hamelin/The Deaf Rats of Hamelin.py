def find_p(a):
    if a.find('P') == 0:
        return a
    elif a.find('P') == (len(a)-1):
        return a[::-1]
    else:
        s = a.find('P')
        return a[s:]+a[s-1::-1]


def count_deaf_rats(town):
    k = 0
    town = town.replace(' ', '')
    rats = find_p(town)
    for i in range(1, len(rats), 2):
        if rats[i] == 'O' and rats[i + 1] == '~':
            continue
        else:
            k += 1
    return k
