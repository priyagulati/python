import matplotlib.pyplot as plt
input_values=[1,2,3,4,5,6]
squares=[1,4,9,16,25,36]
plt.plot(input_values,squares,linewidth=4)

#Set the chart title and label axes
plt.title("square numbers",fontsize=20)
plt.xlabel("value",fontsize=16)
plt.ylabel("square of values", fontsize=16)
plt.show()

