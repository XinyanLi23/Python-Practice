"""ex1for-in用for循环实现1~100求和"""
sum = 0      ###初始赋值
for x in range(101):
    sum += x
print(sum)



"""ex2 用for循环实现1~100之间的偶数求和"""
sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)



"""ex3 猜数字游戏"""
import random
answer = random.randint(1, 100)
counter = 0      ###初始赋值
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')



# """ex4while
# 输出乘法口诀表(九九表)
# """

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d' % (i, j, i * j), end='\t')   ###阶梯排列 "\t" is a tab, "\n" is a newline, and "\r" is a carriage return.
#     print()




"""exe1 输入一个正整数判断它是不是素数"""
from math import sqrt
num = int(input("num: "))
end = int(sqrt(num))    ###
prime = True
for x in range(2, end + 1):
    if num % x == 0:
        prime = False
        break
if prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)


# True, 23443, "dfdfd"
# False, '', 0, False

test = 0
if test:
    print("It is true")
else:
    print(False)



"""exe2 输入两个正整数计算它们的最大公约数和最小公倍数"""

x = int(input("x: "))
y = int(input("y: "))
if x > y:
    # 通过下面的操作将y的值赋给x, 将x的值赋给y
    x, y = y, x
# 从两个数中较的数开始做递减的循环
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break




"""exe3
*
**
***
****
*****
    *
   **
  ***
 ****
*****
    *
   ***
  *****
 *******
*********
"""

for i in range(5):
    print('*' * (i+1))
for i in range (5):
    print("%s%s" % (' ' * (4-i), '*' * (i+1)))
for i in range (5):
    print("%s%s" % (' ' * (4-i), '*' * (1+2*i)))

