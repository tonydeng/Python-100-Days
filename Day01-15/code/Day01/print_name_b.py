name = '小明'
age = 6
height = 103.2

print(name + '今年' + str(age) + '岁，身高'+str(height)+'厘米')

# 将一个人名存储成一个变量

name  = "TonY Deng"
print(name)
print(name.lower())
print(name.upper())
print(name.title())
print(name.capitalize())


name = str(input("请输入姓名："))
print(name.upper())


# 输出“《将进酒》是唐代诗人李白的诗作”
a,b,c = '李白','将进酒','唐代'

print('《{1}》是{2}诗人{0}的诗作'.format(a,b,c))