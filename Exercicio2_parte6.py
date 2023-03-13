# insertior sort
# possui testes de tempo
import datetime
import random

v = []
for i in range(1000):
    rand = random.randint(0,999999)
    v.append(rand)

n = len(v)

st = datetime.datetime.now()
for i in range(0, n - 1):
    for j in range(i + 1, 0, -1):
        if int(v[j - 1]) > int(v[j]):
            temp = v[j - 1]
            v[j - 1] = v[j]
            v[j] = temp

        else:
            break

et = datetime.datetime.now()

tempo = et - st
print(v)
print(tempo)
