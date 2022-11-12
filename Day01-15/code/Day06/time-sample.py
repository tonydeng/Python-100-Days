"""
- 时间相关模块 time
https://docs.python.org/zh-cn/3/library/time.html
"""

import time
a=time.time()
time.sleep(1) # 该函数也会保证调用它的线程至少会睡眠 secs 秒
b=time.time()
print(b-a)

# 返回当前时间的时间戳（1970纪元后经过的浮点秒数）
seconds = time.time()  
# 比如，1667565389.835823 
print(seconds)  
# 将时间戳转换为当前时区的struct_time
localtime = time.localtime(seconds) 
# time.struct_time(tm_year=2022, tm_mon=7, tm_mday=6, tm_hour=14, tm_min=49, tm_sec=49, tm_wday=2, tm_yday=187, tm_isdst=0)
print(localtime)  
# 2022
print(localtime.tm_year)
# 7 
print(localtime.tm_mon) 
# 6
print(localtime.tm_mday) 
# 将struct_time转换为字符串
asctime = time.asctime(localtime)
# Wed Jul  6 14:49:49 2022
print(asctime)
# 将struct_time转换为指定格式的字符串
strtime = time.strftime('%Y-%m-%d %H:%M:%S', localtime) 
# 2022-07-06 14:49:49
print(strtime)
# 将指定字符串按指定格式转换为struct_time
mydate = time.strptime('2018-1-1', '%Y-%m-%d') 
# time.struct_time(tm_year=2018, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=1, tm_isdst=-1)
# tm_year是年，tm_mon是月，tm_mday是日，tm_hour是时，tm_min是分，tm_sec是秒，tm_wday是星期几，tm_yday是一年中的第几天，tm_isdst是夏令时
print(mydate)

ns=time.time_ns()
print("time_ns() value is '{}', time() value is '{}'".format(str(ns), str(seconds)))
