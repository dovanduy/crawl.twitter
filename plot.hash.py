#!/usr/bin/python 

import matplotlib.pylab as plt
import sys, math

x = [] 
for line in sys.stdin:
    ### print line
    x.append(line.strip())

x = [math.log(float(s)) for s in x]
idx = range(1, len(x) + 1)
idx = [math.log(float(s)) for s in idx]

plt.clf()
plt.plot(idx, x)
plt.title('Log/Log plot of hash tag frequencies')
plt.xlabel('Hash Tags (Omitted) Index')
plt.ylabel('Frequency')
plt.savefig('hash.png', format='png')
