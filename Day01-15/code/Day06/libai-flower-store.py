'''
李白街上走，提壶去买酒。
遇店加一倍，见花喝一斗。
三遇店和花，喝光壶中酒。
试问此壶中，原有多少酒。
'''


def buy_flower(wine):
    if wine == 0:
        print("酒壶中没有酒了，不能再买花了")
        return 0
    print("当前酒有{}斗，见花喝一斗".format(wine))
    return wine-1
    

def buy_store(wine):
    print("当前酒有{}斗，遇店加一倍".format(wine))
    return wine*2

if __name__ == "__main__":
    print(buy_flower(
            buy_flower(
                buy_store(
                    buy_flower(
                        buy_store(
                            buy_flower(
                                buy_store(0.875)
                                )
                            )
                        )
                    )
                )
            )
        )



# cnt = 0


# def main():
#     start = 2

#     flower_cnt = 3
#     store_cnt = 3

#     get_ret(start, flower_cnt, store_cnt, '')


# def get_ret(start, flower_cnt, store_cnt, string):
#     if start == 0 and store_cnt == 0 and flower_cnt == 0:
#         # print(string) # 输出的结果就是走过的路径
#         global cnt
#         cnt += 1

#     if start <= 0:
#         return

#     # 遇到花
#     if flower_cnt > 0:
#         deal_flower(start, flower_cnt, store_cnt, string)
#     # 遇到店
#     if store_cnt > 0:
#         deal_store(start, flower_cnt, store_cnt, string)


# # 处理花的问题
# def deal_flower(start, flower_cnt, store_cnt, string):
#     start -= 1
#     flower_cnt -= 1
#     string += 'b'
#     get_ret(start, flower_cnt, store_cnt, string)


# # 处理店的问题
# def deal_store(start, flower_cnt, store_cnt, string):
#     start *= 2
#     store_cnt -= 1
#     string += 'a'
#     get_ret(start, flower_cnt, store_cnt, string)


# if __name__ == '__main__':
#     main()
#     print(cnt)
