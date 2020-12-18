from matplotlib import pylab as pit
import numpy as np

a = int(input('개수 입력'))

x = np.arange(1, a+1)
y = np.log(x)

pit.plot(x, y, 'or')
pit.annotate('Maximum number of data', xy=(a, np.log(a)), xytext=(0, 0), arrowprops={'color': 'blue'})
pit.xlabel('Number of times to perform')
pit.ylabel('Number of data')
pit.title('a dichotomous graph')
pit.show()
