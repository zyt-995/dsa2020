def main():
    import sys
    M = 23 * 28 * 33  # 21252

    for line in sys.stdin:
        data = line.strip().split()
        if not data:
            continue
        p, e, i, d = map(int, data)

        a = p % 23
        b = e % 28
        c = i % 33

        term1 = a * 924 * 6  # 924=28*33, inv(924,23)=6
        term2 = b * 759 * 19  # 759=23*33, inv(759,28)=19
        term3 = c * 644 * 2  # 644=23*28, inv(644,33)=2

        sum_total = term1 + term2 + term3
        x0 = sum_total % M

        if x0 <= d:
            x = x0 + M
        else:
            x = x0

        print(x - d)


if __name__ == "__main__":
    main()