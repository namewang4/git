import matplotlib.pyplot as plt
input_value = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_value,squares,linewidth=5)
"""绘折线图函数，横坐标如果忽略，则从0开始"""
plt.scatter(input_value,squares,s=100)
"""散点图,s为点的大小"""
"""设定绘制线条的粗细"""

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values,s=1)

#设置图标标题，并给坐标轴加上标签
plt.title("squaresvalue",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("squaresvalue",fontsize=14)

#设置刻度标记数字的大小
plt.tick_params(axis='both',labelsize=8)

#设置坐标轴的取值范围
plt.axis([0,1100,0,1100000])

plt.show()
