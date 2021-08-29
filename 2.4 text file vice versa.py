with open(r"C:\1\dataset_24465_4.txt", "r") as inf:
    l = inf.readlines()
    with open(r"C:\1\solve.txt", "a") as ouf:
        for line in reversed(l):
            ouf.write(line)