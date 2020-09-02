coding=UTF-8

"""re1 输入一个正整数判断它是不是素数"""
from math import sqrt
num = int(input("num: "))
end = int(sqrt(num))
prime = True
for x in range (2, end + 1):
    if num % x == 0:
        prime = False
        break
if prime and num != 1:
    print('%d是素数' % num) 
else:
    print('%d不是素数' % num) 



"""re2 输入两个正整数计算它们的最大公约数和最小公倍数"""
x = int(input("x: "))
y = int(input("y: "))
if x > y:
    x, y = y, x
for factor in range (x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print("%d和%d的最大公约数是%d" % x, y, factor)
        print("%d和%d的最小公倍数是%d" % x, y, x * y // factor)
        break
        


"""re3
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
for i in range(5):
    print('%s%s' * (' ' * (4-i), '*' * (i+1)))
for i in range(5):
    print ('%s%s' * (' ' * (4-i), '*' * (1+2*i)))




"""ex1 找出所有水仙花数
它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$
"""

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)



"""ex2 
正整数的反转
"""

num = int(input('num= '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num) 


"""exe3
Hundred dollar buy hundred chicken
Total $100. Rooster $5, hen $3, chick 3 for $1. 
"""

for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + 1* z/3 == 100:
            print('rooster:%d, hen:%d, and chick: %d'% (x, y, z))




"""ex4 Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注
"""

from random import randint
money = 1000
while money > 0:
    print('Total assets：', money)
    needs_go_on = False
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
        elif current == first:
            print('玩家胜')
            money += debt
        else:
            needs_go_on = True
print('你破产了, 游戏结束!')




"""exe1 The first 20 numbers of Fibonacci sequence"""
a = 0
b = 1
for _ in range(0, 20):
    a, b = b, a + b
    print(a, end=' ')



"""exe2 找出10000以内的完美数"""
for num in range(1, 10000): 
    sum = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum = i + sum
    if sum == num:
        print('%d' % num)
    


"""exe3 输出100以内所有的素数"""
for num in range(2, 100): 
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    if count < 3:
        print("%d" % num, end=" ")




"""method 2"""
from math import sqrt
for num in range(2, 100): 
    count = 0
    sqrt_num = int(sqrt(num))
    for i in range(1, sqrt_num + 1):
        if num % i == 0:
            count += 1        
    if count == 1:
        print("%d" % num, end=" ")












    
  
