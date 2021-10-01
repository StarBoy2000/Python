from itertools import product

k, m = list(map(int, input().split()))
List = []
for _ in range(k):
    List.append(list(map(int, input().split()[1:])))
Nlist = list(product(*List))

sumList = []
for item in Nlist:
    sumi = 0
    for sub in item:
        sumi += pow(sub, 2) 
    sumList.append(sumi)
    
print(max([i%m for i in sumList]))
 