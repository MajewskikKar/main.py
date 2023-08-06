import itertools
import math
from szukanie_liter import diction, rectangles_cen, rectangles_cen_one
import numpy as np
pairs = []
pairs1 = []
for x,y in itertools.combinations(sorted(rectangles_cen),2):
    if math.dist(x, y)<90:
        if sum(x)<sum(y):
            pairs.append((int(str(x[0]) + str(x[1])),int(str(y[0]) + str(y[1]))))
            pairs1.append([x,y])
        else:
            pairs.append((int(str(y[0]) + str(y[1])),int(str(x[0]) + str(x[1]))))
            pairs1.append([y,x])
pairs1_np = np.array(pairs1)
for count, value in enumerate(pairs1_np):
    if value[1] in pairs1_np[count:]:
        i, j = np.where(a == value[1])
# for count, value in enumerate(pairs1):
#     print(value[1])
#     print(diction[value[1]])
    #if value[1] in nump[:count]:
     #   print(pairs1.index(value[1]))

