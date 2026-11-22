import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy import integrate

f= lambda x: 1/((x**5)+1)
x=np.linspace(-0.5,4,100)
y=f(x)
F= integrate.cumulative_trapezoid(y,x,initial=0)
dy=np.gradient(y,x)
plt.figure(figsize=(10,6))
plt.plot(x,y,label="f(x)",color="blue")
plt.plot(x,F,label="F(x)",color="red")
plt.plot(x,dy,label="df",color="green")
plt.legend()
plt.grid(True)
plt.show()
"""print("Value of the integral is:",val)
#plt.plot(x,norm.pdf(x,mu,sigma))
plt.title("Normal Distribution with $\mu=0$ and $\sigma=1$")
plt.xlabel("x")
plt.ylabel("Density")"""

