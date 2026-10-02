def hcf(n1, n2):
    small = min(n1, n2)

    large = max(n1, n2)

    if (small) == 0:
        return large

    return hcf(small, large % small)


print(hcf(50, 15))
