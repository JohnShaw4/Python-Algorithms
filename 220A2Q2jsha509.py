#jsha509
#Code answer for question 2 of assignment 2

k = int(input())

sep = input()

songs = []

for i in range(4):
    line = input()
    lineSplit = line.split(sep)
    songs.append(lineSplit)

songsSort = sorted(songs, key=lambda x: (-int(x[2]), x[0]))

for i in range(k):
    print(songsSort[i][0], end ="")
    print(sep, end ="")
    print(songsSort[i][1], end ="")
    print(sep, end ="")
    print(songsSort[i][2])
