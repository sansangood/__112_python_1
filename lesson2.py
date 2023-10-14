side = int(input("請輸入對邊:"))
another_side = int(input("請數入斜邊:"))

import math
radian = math.asin(side/another_side) # asin 算弧度
degree = math.degrees(radian)  # degrees 算角度
print(round(degree,ndigits=2))

