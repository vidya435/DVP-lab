import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def sinplot(n=10):
    X=np.linspace(0,20,50)
    for i in range(1,n+1):
        plt.plot(X,np.sin(X+i*0.5)*(n+2-i))
sinplot()
plt.title("Vidya B M-1KI23Cs178")
sns.set_context("talk")
plt.show()