from matplotlib import pylab as pit
import numpy as np
import math

a = int(input('개수 입력'))

x = np.arange(1, a)
y = np.log(x)

pit.plot(x, y, 'or')
pit.xlabel('Number of times to perform')
pit.ylabel('Number of data')
pit.title('a dichotomous graph')
pit.show()
