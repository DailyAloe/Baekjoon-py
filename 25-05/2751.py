import sys
input = sys.stdin.readline

numList = []
howmany = int(input())
for i in range(howmany):
    num = int(input())
    numList.append(num)
numList.sort()
print('\n'.join(map(str,numList)))

#tm5323의 코드 변형
import sys
input = sys.stdin.readline

a=[None]*2000001 #bool array를 -1,000,000~1,000,000까지 커버하도록 만듦
for _ in range(int(input())):
    i = int(input())
    a[i+1000000]=1 #-1,000,000은 0번 인덱스에 위치하도록
print("\n".join(str(i) for i in range(-1000000,1000001,1) if a[i+1000000]))
#for -> if -> 명령(str)
