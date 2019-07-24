#jsha509
#Code answer for question 1 of assignment 2

nAndM = input()
splitnAndM = nAndM.split(" ")
n = int(splitnAndM[0])
m = int(splitnAndM[1])

numList = []


for x in range(n):
    numList.append(int(input()))

smallest = sum(numList)

for i in range(n):
    tempSmallest = 0
    if ((i+m)<n):
        for x in range(m):
            tempSmallest += numList[i+x]
        if tempSmallest < smallest:
            smallest = tempSmallest
        
                
print(smallest)


