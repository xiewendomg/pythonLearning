import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,10.1000)#作图变量的自变量
y = np.sin(x)+1 #因变量y
z = np.cos(x**2)+1 #因变量z
#print(y)

plt.figure(figsize = (8,4) )
plt.plot(x,y,label = '$\sin x+1$',color = 'red',linewidth=2)
plt.plot(x,z,label = '$\cos x^2+1$',color = 'gray',linewidth=2)
#plt.plot(x,z,color='b--',lable='$\cos x^2+1$')
plt.xlabel('Time(s)')
plt.ylabel('Volt')
plt.title('A Simple Example')
plt.ylim(0,2.2)
plt.legend()
plt.show()