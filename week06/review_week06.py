#%%
import matplotlib.pyplot as plt
values = [5,3,2,1,0.5]
labels = ['A','B','C','D','E']
Fig, Ax = plt.subplots()
Ax.pie(values,labels=labels,autopct='%0.1f%%')
Ax.set_xlabel('X-axis')
Ax.set_ylabel('Y-axis')
plt.show()