import random

A = [1,2,3,4,5,6,7,8]
B = [8,7,6,5,4,3,2,1]
C = [1,2,4,5,6,3,3]
#C= A[:3]

#lista = list(range(3,9))


#print(random.sample(lista,len(lista)))
#print(list(set(C)))

result = []
for item in C:
    if item not in result:
        result.append(item)

print(result)


print(random.sample(list(range(1,9)),8))
