"""
- 数学相关模块 math
https://docs.python.org/zh-cn/3/library/math.html
"""

import math # 导入math模块
import random # 导入random模块

print(math.sqrt(4)) # 计算4的平方根

a=3
print(a**2) # 计算3的平方
b=4
print(b**2) # 计算4的平方
c=math.sqrt(a**2+b**2)
print(c)

print(random.random()) # 生成一个0到1之间的随机小数
print(random.randint(1,10)) # 生成一个1到10之间的随机整数
print(random.uniform(1,10)) # 生成一个1到10之间的随机小数