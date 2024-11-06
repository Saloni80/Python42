import matplotlib.pyplot as plt
plt.plot([1,2,3],[4,5,6], color="red")
plt.xlim(1,5)
plt.ylim(1,6)
plt.xlable('x-axis')
plt.ylable('y-axis')
plt.tittle("Demo Graph")
plt.legend(["values"])
plt.show()