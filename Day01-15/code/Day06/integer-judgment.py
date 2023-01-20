# 小A的喜好
def a(x):
    if (x % 2 == 0) and (4 < x <=12):
        return 1
    else:
        return 0

#Uim的喜好
def b(x):
    if x % 2 == 0 or 4 < x <= 12:
        return 1
    else:
        return 0

# 八尾勇的喜好
def c(x):
    if (x % 2 == 0 and not (4 < x <= 12)) or (not (x % 2 == 0) and 4 < x <= 12):
        return 1
    else:
        return 0
        
# 正妹的喜好
def d(x):
    if not (x % 2 == 0) and not (4 < x <= 12):
        return 1
    else:
        return 0

if __name__ == '__main__':
    x = int(input('请输入一个数字(0-1000)之间：'))
    if x >= 0 and x <= 1000:
        print(a(x),b(x),c(x),d(x))
    else:
        print('输入的数字不在范围内,请重新执行！')











    '''可以不用函数，直接写
    if x % 2 == 0 and 4 < x <= 12:
        a = 1
    else:
        a = 0
    if x % 2 == 0 or 4 < x <= 12:
        b = 1
    else:
        b = 0
    if (x % 2 == 0 and not (4 < x <= 12)) or (not (x % 2 == 0) and 4 < x <= 12):
        c = 1
    else:
        c = 0
    if not (x % 2 == 0) and not (4 < x <= 12):
        d = 1
    else:
        d = 0
    print(a, b, c, d)
    '''
       