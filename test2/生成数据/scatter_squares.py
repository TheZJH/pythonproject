import matplotlib.pyplot as plt

"""
plt.scatter(2, 4, s=200)
plt.show()
"""
"""
# scatter()绘制一系列点
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values, y_values, s=100)
plt.show()
"""

# 自动计算数据
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, s=40)

# 设置坐标的取值范围
plt.axis([0, 1100, 1100000])
plt.show()
