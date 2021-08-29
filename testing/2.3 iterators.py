lst = [1, 2, 3, 4, 5, 6]
book = {
    'title': 'The Langoliers',
    'author': 'Stephen King',
    'year_published': 1990
}
string = "Hello, world!"

iterator = iter(book)
print(next(iterator)) # title
print(next(iterator)) # author
print(next(iterator)) # year_published
next(iterator) # StopIteration err

# Как происходит итерация на примере цикла While:
it = iter(book)
while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break