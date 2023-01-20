print("\n手机店正在打折，活动进行中\n")
Week = input("请输入星期几：")
Time = int(input("请输入时间(范围是0-23)："))

if (Week == "2" and (Time>=10 and Time <=11)) or (Week == "5" and (Time>=14 and Time <=15)):
    print("恭喜你，打折啦！")
else:
    print("对不起，期待下次吧！")