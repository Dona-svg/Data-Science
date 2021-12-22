import numpy as np
import matplotlib.pyplot as plt

plt.subplot(1,2,1)
x=np.array(['MON','TUE','WED','THU','FRI'])
y=np.array([300,450,150,400,650])
plt.plot(x,y,':',color='c',marker='h',mfc='m',mec='b')
plt.xlabel("Days of week")
plt.ylabel("Sales of Drink")
plt.title ("Sales Data1",loc="right")


plt.subplot(1,2,2)
x=np.array(['MON','TUE','WED','THU','FRI'])
y=np.array([400,500,350,300,500])
plt.plot(x,y,'--',color='y',marker='d',mfc='g',mec='r')
plt.xlabel("Days of week")
plt.ylabel("Sales of Drink")
plt.title ("Sales Data2",loc="right")
plt.show()
