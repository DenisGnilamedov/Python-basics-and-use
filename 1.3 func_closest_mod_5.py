def closest_mod_5(x):
    y = x
    if y % 5 == 0:
        return y
    while y % 5 != 0:
        y += 1
    return y


print(closest_mod_5(6))