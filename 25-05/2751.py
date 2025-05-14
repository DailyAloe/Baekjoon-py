import sys
input = sys.stdin.readline

numList = []
howmany = int(input())
for i in range(howmany):
    num = int(input())
    numList.append(num)
numList.sort()
print('\n'.join(map(str,numList)))
