import math
T = int(input())
for i in range(T):
    N = int(input())
    pages = N*1000
    note_books = math.floor(pages/100)
    print(note_books)
