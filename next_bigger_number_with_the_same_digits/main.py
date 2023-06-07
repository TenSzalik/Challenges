def next_bigger(n):
    if sorted(str(n), reverse=True) == list(str(n)):
        return -1

    sorted_n = sorted(str(n))
    bigger_n = n

    while True:
        bigger_n += 9
        if sorted_n == sorted(str(bigger_n)): return bigger_n
