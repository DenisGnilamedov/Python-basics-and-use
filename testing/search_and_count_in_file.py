import io
count = 0
symb_count = 0
with io.open("C:/1/QAtest.txt", encoding='utf-8') as inf:
    for line in inf:
        count += 1
        symb_count += (line.count('а'))
    print(count, symb_count)
