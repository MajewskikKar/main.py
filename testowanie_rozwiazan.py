import itertools
import math
from szukanie_liter import diction, rectangles_cen, rectangles_cen_one
import numpy as np
pairs = [] #lista przechowująca wartości w formie jednego wyrażenia (np. dla punktu o wrtosciach (11,30) będzie to (1130). Bez tego nie użyjemy później funkcji argwhere do szukania sąsiadujących ze sobą par.
pairs1 = [] #lista przechowująca wartości w oryginalnej formie (x,y)

#funkcja służy do sprawdzenia odległości między punktami
for x,y in itertools.combinations(sorted(rectangles_cen),2): #"2" jest metodą sprawdzania, gdzie bierzemy pod uwagę każde dwa punkty
    if math.dist(x, y)<120: # przyjęty dystans to 115 pikseli. W takich watrościach, punkty będą ze sobą sąsiadujące.
        # sortujemy wartości, aby zgadzały się z kierunkiem słów ->>pionowo lub poziomo
        if sum(x)<sum(y):
            pairs.append((int(str(x[0]) + str(x[1])),int(str(y[0]) + str(y[1]))))
            pairs1.append([x,y])
        else:
            pairs.append((int(str(y[0]) + str(y[1])),int(str(x[0]) + str(x[1]))))
            pairs1.append([y,x])


pairs_np = np.array(pairs) #przerobienie par na numpy aby użyć funkcji argwhere
print(pairs)

for count, value in enumerate(pairs_np):
    a = np.argwhere(pairs_np == value[1])
    print(a)
    if len(a)>0 and a[0][0] == 0:
        szukana = pairs[a[0][0]+1][1]
        print(szukana)
    if szukana:
        f = np.append(pairs[count], szukana)
        b = np.argwhere(pairs_np == f[-1])
        if len(b) > 0 and b[1][0] == 0:
            szukana = pairs[a[0][0]+1][0]
            pass
    szukana = None

for elem in f:
    print(diction[elem])

