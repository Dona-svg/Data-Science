import numpy as np
from matplotlib import pyplot as plt
x =np.array([2001,2002,2003,2004,2005,2006,2007])
y =np.array([24000,22500,19700,17500,14500,10000,5800])

plt.plot(x,y,'-.',color='r',marker='*',ms='20',mec='g',mfc='g')
plt.xlabel("Year")
plt.ylabel("Car Value")
plt.title ("Value Depreciation",loc="left")
plt.show()