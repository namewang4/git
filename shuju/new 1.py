import matplotlib.pyplot as plt
from random_walk import RandomWalk 
input_value = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_value,squares,linewidth=5)
"""绘折线图函数，横坐标如果忽略，则从0开始"""
plt.scatter(input_value,squares,s=100)
"""散点图,s为点的大小"""
"""设定绘制线条的粗细"""
"""绘制线的颜色可以使用c=(0,0,0.8)这种表示"""
"""数据点的轮廓edgecolor，删除none"""
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

# plt.scatter(x_values,y_values,c='red',edgecolors="none",s=1)
# plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,
    # edgecolors="none",s=1)
# """将参数 c 设置成了一个y值列表，并使用参数 cmap 告诉 pyplot 使用哪个颜色映射。这些代
# 码将y值较小的点显示为浅蓝色，并将y值较大的点显示为深蓝色"""

#设置图标标题，并给坐标轴加上标签
plt.title("squaresvalue",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("squaresvalue",fontsize=14)

#设置刻度标记数字的大小
plt.tick_params(axis='both',labelsize=8)


while True:
	rw = RandomWalk()
	rw.fill_walk()
	r_point_numbers = list(range(rw.num_points))
	print(r_point_numbers[0])
	plt.scatter(rw.x_values,rw.y_values,c=r_point_numbers,cmap = plt.cm.Blues,s=1)
	#突出起点和终点
	plt.scatter(0,0,c='red',edgecolors='none',s=20)
	plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=10)
	plt.show()
	keep_running = input("是否继续生成，是输入y,否输入n")
	if keep_running == "n":
		break
#设置坐标轴的取值范围
# plt.axis([-2000,2000,-2000,2000])
plt.savefig('ceshi.png',bbox_inches='tight')
plt.show()

#保存的话使用第一个实参指定要以什么样的文件名保存图表，这个文件将存储到scatter_squares.py所在的
#目录中；第二个实参指定将图表多余的空白区域裁剪掉。如果要保留图表周围多余的空白区域，
#可省略，plt.show() 后调用了 plt.savefig() ，在 plt.show() 后实际上已经创建了一个新的空白的图片
#（坐标轴），这时候你再 plt.savefig() 就会保存这个新生成的空白图片。

